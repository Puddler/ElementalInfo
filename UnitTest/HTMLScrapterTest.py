import unittest
import Core.HTMLScraper


class HTMLScraperTest(unittest.TestCase):

    def GetHTMLNonSSL(self):
        self.assertEqual(Core.HTMLScraper.GetHTMLNonSSL("http://littlerojo.com"), '')

    def SearchWikipedia(self):
        self.assertEqual(Core.HTMLScraper.searchWikipedia("Test"), '')

if __name__ == '__main__':
    unittest.main()
