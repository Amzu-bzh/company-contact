## Imports
from googlesearch import search

## Functions
def fetch_top_search_results(query, num_results=10):
    search_results = search(query, num_results=num_results)
    return search_results

## Class
class WebsiteFinder:
    def __init__(self, num_results: int = 10):
        self.num_results = 10     
    
    def search(self, query: str):
        urls = []
        if query == "" or query == None:
            raise Exception("search method in WebsiteFinder class nead parameter `query`")
        
        results = fetch_top_search_results(query=query, num_results=self.num_results)
        for idx, result in enumerate(results, 1):
            urls.append(result)
        
        return urls