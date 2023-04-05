# **DAILY NEWS SCRAPER**

This project is a daily news scraper that uses Python to download and store news in a specific folder.

------------


## Functionality

The scraper uses the ``httpx`` library to make HTTP requests to the news websites that are going to be scraped. Then, it uses the ``selectolax`` library to parse the HTML of the web pages and extract the titles and links of the news of the day.

Finally, the news is stored in a folder created by the script using the ``os`` library and with a name that reflects the current date thanks to the ``datetime`` library.

------------


## Technologies Used

The daily news scraper was developed using the following Python technologies and modules:

- Python
- httpx
- selectolax
- os
- datetime

------------


## Installation

To install the daily news scraper, first clone the repository and then install the dependencies using pip3 and the requirements.txt file:



    git clone https://github.com/ChristianLaurean/NewsScraper.git
    pip3 install -r requirements.txt

------------


## Usage

The daily news scraper is run through the command line and can be used to download and store news in a specific folder. To execute the scraper, simply use the following command:



    python3 scraper.py
    