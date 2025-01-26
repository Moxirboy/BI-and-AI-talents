
import sqlite3
import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

# Database setup
def setup_database():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS jobs
                 (title TEXT, company TEXT, location TEXT, 
                  description TEXT, link TEXT,
                  PRIMARY KEY(title, company, location))''')
    conn.commit()
    return conn

# Web scraping function
def scrape_jobs():
    base_url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = []
    
    for card in soup.find_all('div', class_='card'):
        title = card.find('h2', class_='title').text.strip()
        company = card.find('h3', class_='subtitle').text.strip()
        location = card.find('p', class_='location').text.strip()
        
        # Get description from the hidden content
        description_tag = card.find('div', class_='content')
        description = description_tag.find('p').text.strip() if description_tag else ''
        
        # Get absolute URL for application link
        link_tag = card.find('a', string='Apply')
        link = urljoin(base_url, link_tag['href']) if link_tag else ''
        
        jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'description': description,
            'link': link
        })
    
    return jobs

# Incremental load and update tracking
def save_to_db(conn, jobs):
    c = conn.cursor()
    for job in jobs:
        # Use UPSERT to handle updates
        c.execute('''INSERT INTO jobs VALUES (?, ?, ?, ?, ?)
                     ON CONFLICT(title, company, location) DO UPDATE SET
                     description=excluded.description,
                     link=excluded.link''', 
                  (job['title'], job['company'], job['location'],
                   job['description'], job['link']))
    conn.commit()

# Filtering functions
def filter_jobs(conn, location=None, company=None):
    c = conn.cursor()
    query = "SELECT * FROM jobs"
    params = []
    
    if location or company:
        query += " WHERE "
        conditions = []
        if location:
            conditions.append("location LIKE ?")
            params.append(f"%{location}%")
        if company:
            conditions.append("company LIKE ?")
            params.append(f"%{company}%")
        query += " AND ".join(conditions)
    
    c.execute(query, params)
    return c.fetchall()

# CSV export function
def export_to_csv(data, filename='jobs.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Company', 'Location', 'Description', 'Link'])
        writer.writerows(data)

# Main execution
if __name__ == "__main__":
    conn = setup_database()
    
    # Scrape and update database
    jobs = scrape_jobs()
    save_to_db(conn, jobs)
    
    # Example filtering and export
    filtered_jobs = filter_jobs(conn, location="London")
    export_to_csv(filtered_jobs)
    
    conn.close()
    print("Database updated and CSV exported successfully!")
