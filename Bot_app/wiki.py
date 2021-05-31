"""
file that contains Wikipedia Api class for searching sentences
 according to coordinates
"""

import requests
from config import WIKI_API_URL


class Wiki:

    def __init__(self, latitude, longitude):
        self.json_result = None
        self.paylod = {
            "action": "query",
            "format": "json",
            "ggscoord": f"{longitude}|{latitude}",
            "generator": "geosearch",
            "prop": "extracts|info",
            "explaintext": True,  # convert HTML to plain text
            "exsentences": 3,  # how many sentence to return
            "inprop": "url",  # get url (added info to prop)
        }
        self.result()

    def result(self):
        result = requests.get(WIKI_API_URL, self.paylod)
        if result.status_code == 200:
            self.json_result = result.json()
            if 'query' in self.json_result:
                pages = self.json_result['query']['pages']
                pages = (list(pages.values()))

                title = pages[0]['title']
                sentence = pages[0]['extract']
                url = pages[0]['fullurl']

                self.json_result = {"title": title,
                                    "sentence": sentence,
                                    "url": url}

                return self.json_result
