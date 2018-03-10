from Core import HTMLScraper
from bs4 import BeautifulSoup

class Element:

    elementData = {}

    def __init__(self):
        self.getElementsFromWikipedia();

    def getElementsFromWikipedia(self):
        soup = HTMLScraper.getSoupFromURL("https://en.wikipedia.org/wiki/List_of_chemical_elements")
        table = soup.find('table', attrs={ "class" : "wikitable sortable collapsible"})
        rows = table.findAll('tr')
        rows.pop(0)
        rows.pop(0)
        rows.pop(len(rows) - 1)

        table_data = [[cell.text for cell in row("td")]
                                 for row in rows]

        self.elementData = table_data


