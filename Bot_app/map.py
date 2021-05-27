"""
Map class call api mapbox to get coordinates by checking the parsed_word
"""

import requests
from config import GEO_API_URL, GEO_TOKEN


class Map:
    """Represent the Mapbox API"""

    def __init__(self, parse_word):
        self.longitude = None
        self.latitude = None
        self.get_coordinate(parse_word)

    def get_coordinate(self, parse_word):
        """Call Mapbox Api and set longitude and latitude
        according to the parse_word
        """
        result = requests.get(
            f"{GEO_API_URL}{parse_word}.json?access_token={GEO_TOKEN}"
            f"&language=fr")

        if result.status_code == 200:
            json_result = result.json()

            if len(json_result['features']) > 0:

                self.longitude = \
                    json_result['features'][0]['geometry']['coordinates'][1]

                self.latitude = \
                    json_result['features'][0]['geometry']['coordinates'][0]