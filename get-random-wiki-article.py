### The program searches Wikipedia and fetches a random article.
# Then it asks the user if he wants to read that article or not.
# If the answer is yes, the material is shown; otherwise, another random report is presented.

# requests - sending HTTP requests
# beautifulsoup4 - scraping
# webbrowser - Python's standard library; module provides a high-level interface to allow displaying web-based documents to users. Under most circumstances, simply calling the open() function from this module will do the right thing.

import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text
    print(f"{title} \nDo you want to read it? \nY-yes \nN-no \nQ-quit")
    ans = input("").lower()
    if ans == "y":
        url = "https://en.wikipedia.org/wiki/%s" % title.replace(' ', '_')
        webbrowser.open(url)
        break
    elif ans == "n":
        print("Try again!")
        continue
    elif ans == "q":
        break
    else:
        print("Wrong letter - choose from Y-yes/N-no/Q-quit")
        continue


