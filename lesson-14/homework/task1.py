from bs4 import BeautifulSoup

# Parse the HTML file
with open('weather.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Extract the table and its rows
table = soup.find('table')
tbody = table.find('tbody')
rows = tbody.find_all('tr')

weather_data = []
for row in rows:
    columns = row.find_all('td')
    day = columns[0].get_text(strip=True)
    temperature = columns[1].get_text(strip=True)
    condition = columns[2].get_text(strip=True)
    weather_data.append({
        'day': day,
        'temperature': temperature,
        'condition': condition
    })

# Display the weather data
print("5-Day Weather Forecast:")
for entry in weather_data:
    print(f"Day: {entry['day']}, Temperature: {entry['temperature']}, Condition: {entry['condition']}")

# Find the day(s) with the highest temperature
temperature_values = []
for entry in weather_data:
    temp_str = entry['temperature'].strip('°C')
    temperature_values.append(int(temp_str))

max_temp = max(temperature_values)
max_temp_days = [entry['day'] for entry, temp in zip(weather_data, temperature_values) if temp == max_temp]
print("\nDay(s) with the highest temperature:", ", ".join(max_temp_days))

# Find the day(s) with "Sunny" condition
sunny_days = [entry['day'] for entry in weather_data if entry['condition'] == 'Sunny']
print("Day(s) with 'Sunny' condition:", ", ".join(sunny_days))

# Calculate and print the average temperature
average_temp = sum(temperature_values) / len(temperature_values)
print(f"\nAverage temperature for the week: {average_temp:.1f}°C")
