import os

SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

GEO_API_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places/"
GEO_TOKEN = os.environ.get("GEOLOC_TOKEN")

PUNCTUATION = ["'", '"', ",", ".", "!", ":", ";", "?"]