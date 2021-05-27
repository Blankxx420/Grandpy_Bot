""" Configuration files to optimize others files"""
import os

# -- FlASK -- #
S_KEY = os.environ.get('SECRET_KEY')

# -- GEO API: Mapbox-- #
GEO_API_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places/"
GEO_TOKEN = os.environ.get("GEOLOC_TOKEN")

# -- WIKI API -- #
WIKI_API_URL = "https://fr.wikipedia.org/w/api.php?"

# -- Parser -- #
PUNCTUATION = ["'", '"', ",", ".", "!", ":", ";", "?"]