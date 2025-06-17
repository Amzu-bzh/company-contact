## Imports
from googlesearch import search
from levenshtein_distance import levenshtein_distance

from math import sqrt

## Functions
def fetch_top_search_results(query, num_results=10):
    search_results = search(query, num_results=num_results)
    return search_results

## Class
class WebsiteFinder:
    def __init__(self, num_results: int = 10):
        self.num_results = 10     
    
    def filter(self, urls: list[str], query):
        # Filter the websites
        scores = []
        for url in urls:
            if url.find("instagram.com") != -1 or url.find("facebook.com") != -1 or url.find("x.com") != -1 or url.find("linkedin.com") != -1 or url.find("youtube.com") != -1 or url.find("tiktok.com") != -1:
                scores.append(-1) # Social medias
            elif url.find("wikipedia.com") != -1 or url.find("wikimedia.com") != -1:
                scores.append(-2) # Encyclopedias
            elif url.find("reddit.com") != -1 or url.find("quora.com") != -1 or url.find("glassdoor.com") != -1:
                scores.append(-3) # third-party platforms
            elif url.find("amazon.com") != -1 or url.find("ebay.com") != -1 or url.find("fnac.com") != -1 or url.find("boulanger.com") != -1:
                scores.append(-4) # Marketplaces
            else:
                score = levenshtein_distance(query, url.removeprefix("https://www.").removeprefix("https://").removeprefix("http://www.").removeprefix("http://").removesuffix(".com/").removesuffix(".fr/").removesuffix(".org/").removesuffix(".xyz/").removesuffix(".en/").removesuffix(".de/").removesuffix(".es/").removesuffix(".ge/")) * 1/sqrt(urls.index(url) + 3)
                print(url, score)
                scores.append(score)
        # Format the data
        # print(scores)
        sorted_scores = scores.copy()
        sorted_scores.sort(reverse=True)
        # print(sorted_scores)
        return {"social_medias": [urls[i] for i in range(len(scores)) if scores[i] == -1],
                "encyclopedias": [urls[i] for i in range(len(scores)) if scores[i] == -2],
                "forum": [urls[i] for i in range(len(scores)) if scores[i] == -3],
                "marketplaces": [urls[i] for i in range(len(scores)) if scores[i] == -4],
                "website": urls[scores.index(sorted_scores[0])]}
            
    
    def search(self, query: str):
        urls = []
        if query == "" or query == None:
            raise Exception("search method in WebsiteFinder class nead parameter `query`")
        
        results = fetch_top_search_results(query=query, num_results=self.num_results)
        for idx, result in enumerate(results, 1):
            urls.append(result)
        
        urls_formatted = self.filter(urls, query)
        
        return urls_formatted