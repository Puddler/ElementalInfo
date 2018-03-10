import requests
from bs4 import BeautifulSoup


def getHTML(url):
    f = requests.get(url)
    return f.text;


def getSoupFromURL(url):
    html = getHTML(url)
    return BeautifulSoup(html, "html.parser")


def getSoupFromHTML(html):
    return BeautifulSoup(html, "html.parser")
