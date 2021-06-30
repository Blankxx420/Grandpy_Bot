import requests
from Bot_app.map import Map


def test_get_coordinates_success(monkeypatch):

    class MockResponse:

        def __init__(self):
            self.status_code = "200"

        @staticmethod
        def json():
            return {
                "type": "FeatureCollection",
                "query": [
                    "paris"
                ],
                "features": [
                    {
                        "id": "place.14749210607497330",
                        "type": "Feature",
                        "place_type": [
                            "region",
                            "place"
                        ],
                        "relevance": 1,
                        "properties": {
                            "wikidata": "Q90",
                            "short_code": "FR-75"
                        },
                        "text_fr": "Paris",
                        "language_fr": "fr",
                        "place_name_fr": "Paris, France",
                        "text": "Paris",
                        "language": "fr",
                        "place_name": "Paris, France",
                        "bbox": [
                            2.22422400085346,
                            48.8156060108013,
                            2.46976999462145,
                            48.9020129995121
                        ],
                        "center": [
                            2.35183,
                            48.85658
                        ],
                        "geometry": {
                            "type": "Point",
                            "coordinates": [
                                2.35183,
                                48.85658
                            ]
                        },
                        "context": [
                            {
                                "id": "country.19008108158641660",
                                "wikidata": "Q142",
                                "short_code": "fr",
                                "text_fr": "France",
                                "language_fr": "fr",
                                "text": "France",
                                "language": "fr"
                            }
                        ]
                    }]
                }

    def get_coordinate(url):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', get_coordinate)

    request = Map("paris")
    assert (request.longitude, request.latitude) == (48.85658, 2.35183)


def test_get_location_coordinates_failure(monkeypatch):
    """GIVEN a monkeypatched version of requests.get()
    WHEN the HTTP response has failed
    THEN check the HTTP response"""

    class MockResponse:  # object in param?
        def __init__(self):
            self.status_code = 404

        @staticmethod
        def json():
            return {"error": "bad"}

    def mock_get_coordinates(url):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get_coordinates)

    request = Map("input")
    assert (request.longitude, request.latitude) == (None, None)
