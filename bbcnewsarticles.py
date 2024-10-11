import requests
from bs4 import BeautifulSoup
import csv

# Send a request to the BBC News page
url = "https://www.bbc.com/news"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the page")
    html_content = response.text
else:
    print("Failed to retrieve the page")
    exit()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract all article containers
articles = soup.find_all('div', class_='ssrcss-1mhwnz8-Promo')

# Prepare a list to hold all article data
articles_data = []

# Loop through each article container
for article in articles:
    # Extract headline
    headline_tag = article.find('p', class_='ssrcss-1sen9vx-PromoHeadline')
    headline = headline_tag.text.strip() if headline_tag else "Headline not found"

    # Extract article link
    link_tag = article.find('a', class_='ssrcss-1mrs5ns-PromoLink')
    link = "https://www.bbc.com" + link_tag['href'] if link_tag else "Link not found"

    # Extract posted time
    time_tag = article.find('span', class_='visually-hidden ssrcss-1f39n02-VisuallyHidden')
    posted_time = time_tag.text.strip() if time_tag else "Time not found"

    # Extract image URL
    img_tag = article.find('img', class_='ssrcss-11yxrdo-Image')
    img_url = img_tag['src'] if img_tag else "Image URL not found"

    # Append the data to the list
    articles_data.append([headline, link, posted_time, img_url])
    print(f"Headline: {headline}\nLink: {link}\nPosted Time: {posted_time}\nImage URL: {img_url}")

# Write all the data to a CSV file
with open('bbc_news_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header
    writer.writerow(['Headline', 'Link', 'Posted Time', 'Image URL'])
    # Write all article data
    writer.writerows(articles_data)

print("Data successfully written to bbc_news_data.csv")
