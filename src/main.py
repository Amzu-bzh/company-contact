## Imports and setup
from WebsiteFinder import WebsiteFinder
from Scraper import Scraper

websiteFinder = WebsiteFinder()
scraper = Scraper()

## Code
if __name__ == "__main__":
    # query = input("Query: ")
    query = "Créat's concept"
    print(websiteFinder.search(query=query))