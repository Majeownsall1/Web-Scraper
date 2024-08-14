README.txt

Project Overview
This Python script is a basic web scraper that retrieves the title and the first paragraphs from a specified webpage. The script uses the requests library to fetch the webpage's content and the BeautifulSoup library to parse the HTML and extract the desired data.

Prerequisites
Before running the script, ensure that the following Python packages are installed:

requests
beautifulsoup4
You can install these packages using pip:

bash
Copy code
pip install requests beautifulsoup4
How to Use
Set the URL: The script is currently set to scrape data from https://runescape.com. If you want to scrape another webpage, replace the URL in the url variable with your desired URL:

python
Copy code
url = 'https://runescape.com'  # Replace with the URL you want to scrape
Run the Script: Execute the script in your terminal or command prompt:

bash
Copy code
python script_name.py
Replace script_name.py with the name of your Python file.

View the Output: The script will print the following information to the console:

The title of the webpage.
All paragraphs found on the webpage, each printed with an index number.
Error Handling
The script includes basic error handling to catch issues with the HTTP request (e.g., network problems, invalid URLs). If an error occurs, the script will print an error message and terminate.

Example Output
If the script runs successfully, you might see output like the following:

vbnet
Copy code
Title of the page: RuneScape - Free Fantasy MMORPG Browser Game
Paragraph 1: Welcome to RuneScape, the world's most popular free-to-play MMORPG ...
Paragraph 2: Join millions of players in the best fantasy MMORPG on the web ...
...
Notes
This script only extracts text-based content (title and paragraphs) from the specified webpage. It does not handle images, links, or other elements.
The script is designed for educational purposes and simple web scraping tasks.
