from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the page
driver.get("https://computerscience.missouristate.edu/people.htm")

# Wait for the page to load completely
time.sleep(3)  # You can adjust the time as needed for the page to fully load

# Get the page source after JavaScript has been executed
page_source = driver.page_source

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Print the text content of the page
# print(soup.get_text())
Names = []
name = soup.findAll('a', class_="NameLink")
for i in name:
    j = i.get_text()  # Extract the text directly from each <a> tag
    Names.append(j)   # Append the name to the Names list
print("Names :", Names)

# -------------------------------------------------------------------------
Emails = []
Email = soup.findAll('div', class_="Contact")
for i in Email:
    j = i.a['href'] # Extract the text directly from each <a> tag
    Emails.append(j.replace('mailto:', ''))  # Append the Email to the Emails list
print("Emails :", Emails)

with open('CSE_FACULTY.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Email"])  # Write the header row

    for name, email in zip(Names, Emails):
        writer.writerow([name, email])  # Write each name and email as a row

print("Data saved to 'professors.csv'.")

# Close the browser
driver.quit()












