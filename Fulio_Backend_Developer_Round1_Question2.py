"""2. WAP to get the Social Links, Email & Contacts details of a website on user input.
Input:

https://ful.io

Output:

Social links -

https://www.facebook.com/fulioTech/ https://www.linkedin.com/company/ful-io/

Email/s:

support@ful.io

Contact:

+1 343 303 6668"""



import requests
from bs4 import BeautifulSoup
import re

def extract_social_links(soup):
    social_links = []
    for a_tag in soup.find_all('a', href=True):
        if 'facebook.com' in a_tag['href'] or 'linkedin.com' in a_tag['href']:
            social_links.append(a_tag['href'])
    return social_links

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.findall(email_pattern, text)

def extract_contacts(text):
    contact_pattern = r'(\+\d{1,2}[-\s]?\d{3}[-\s]?\d{3}[-\s]?\d{4})'
    return re.findall(contact_pattern, text)

# User input
website_url = input("Enter the website URL: ")

# Fetch webpage content
response = requests.get(website_url)
html_content = response.text

# Parse HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract social links
social_links = extract_social_links(soup)

# Extract emails
emails = extract_emails(html_content)

# Extract contacts
contacts = extract_contacts(html_content)

# Print output
print("Social links:")
for link in social_links:
    print(link)

print("\nEmails:")
for email in emails:
    print(email)

print("\nContacts:")
for contact in contacts:
    print(contact)