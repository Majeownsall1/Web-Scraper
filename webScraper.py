import requests # sends HTTP requests to websites 
from bs4 import BeautifulSoup #used for parsing html and extracting data 
import os # allows a method to interact with operating systems 
import json # used to handle the Json format
import csv # used to handle CSV formats 
from datetime import datetime # provides funtions to work with the time and date 

# This application fetches the following content from a web page , title , paragraphs , links 
# The data is then saved in both Json and CSV formats 
# This application is only for educational purposes 

# Define headers with a User-Agent to mimic a real browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}



# Function to fetch content from the URL
def fetch_content(url): # Fetch data from the URL
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.content # The fetch was succesful
    except requests.exceptions.HTTPError as http_err:  # Error has occured
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e: # Error has occured
        print(f"Error fetching the webpage: {e}")
    return None




# Function to parse HTML and extract data
def parse_html(content):
    soup = BeautifulSoup(content, 'html.parser') # Parses the HTML content 
    data = {
        # Extracts the pages title , otherwise gives a response
        'title': soup.title.text if soup.title else 'No title found',

        # Finds all paragraph <p> tags and obtains text inside them 
        'paragraphs': [p.text for p in soup.find_all('p')],

        # Finds all anchors <a>
        'links': [a['href'] for a in soup.find_all('a', href=True)]
    }
    print(data)
    return data


# Function to save data to a JSON file
# opens a file in write mode "w" , puts the data dictionary into this file 
# in JSON format , making it readable
def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)



# Function to save data to a CSV file

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as f: # Opens a file in write mode "w"
        writer = csv.writer(f) # Writes header first
        writer.writerow(['Title', 'Paragraph', 'Link']) # Loops through <p> and <a> and saves to a new row in the CSV file
        for paragraph, link in zip(data['paragraphs'], data['links']):
            writer.writerow([data['title'], paragraph, link])




# Function to handle output
def handle_output(data):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S") # gets current time and date
    json_filename = f'scraped_data_{timestamp}.json' # saves the file in json
    csv_filename = f'scraped_data_{timestamp}.csv'# saves the file in CSV

    save_to_json(data, json_filename)
    save_to_csv(data, csv_filename)

    print(f"Data saved to {json_filename} and {csv_filename}")



# Main function to run the scraper
# runs the entire application , fetches content , parses it and saves the output 
def main(url):
    content = fetch_content(url)
    if content:
        data = parse_html(content)
        handle_output(data)

# Entry point of the script
# ensures script is run correctly , if so the script runs with the url
if __name__ == "__main__":
    url = 'https://runescape.com'  # Replace with the URL you want to scrape
    main(url)
