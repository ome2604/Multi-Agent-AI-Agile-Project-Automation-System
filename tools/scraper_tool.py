import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, "html.parser")
    return soup.get_text()