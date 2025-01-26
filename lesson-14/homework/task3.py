from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

def scrape_demoblaze_laptops():
    # Initialize the WebDriver (ensure you have ChromeDriver installed)
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")

    # Navigate to Laptops section
    try:
        laptops_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Laptops"))
        )
        laptops_link.click()
    except Exception as e:
        print("Error clicking Laptops category:", e)
        driver.quit()
        return []

    data = []
    scraped_names = set()

    while True:
        try:
            # Wait for products to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "card-block"))
            )

            # Scrape current page
            products = driver.find_elements(By.CLASS_NAME, "card-block")
            new_items = 0

            for product in products:
                name = product.find_element(By.CLASS_NAME, "card-title").text
                price = product.find_element(By.CLASS_NAME, "price").text
                description = product.find_element(By.CLASS_NAME, "description").text

                if name not in scraped_names:
                    data.append({
                        "name": name,
                        "price": price,
                        "description": description
                    })
                    scraped_names.add(name)
                    new_items += 1

            # Check if Next button is clickable
            next_button = driver.find_element(By.ID, "next2")
            if not next_button.is_enabled():
                break

            # Click Next button
            next_button.click()
            
            # If no new items were added after clicking Next, break
            if new_items == 0:
                break

        except Exception as e:
            print("Error during scraping:", e)
            break

    driver.quit()
    return data

def save_to_json(data, filename="laptops.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    laptops_data = scrape_demoblaze_laptops()
    save_to_json(laptops_data)
    print(f"Scraped {len(laptops_data)} laptops. Data saved to laptops.json")
