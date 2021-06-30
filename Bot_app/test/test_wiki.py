import requests
from Bot_app.wiki import Wiki


def test_get_wiki_success(monkeypatch):

    class MockResponse:

        def __init__(self):
            self.status_code = 200

        @staticmethod
        def json():
            return {
                "query": {
                    "pages": {
                        "681159": {
                            "pageid": 681159,
                            "ns": 0,
                            "title": "Paris",
                            "index": -1,
                            "extract": "Paris (/pa.ʁi/) est la commune la plus peuplée et la capitale de la France."
                                       "\nElle se situe au cœur d'un vaste bassin sédimentaire aux sols fertiles"
                                       " et au climat tempéré, le bassin parisien, sur une boucle de la Seine,"
                                       " entre les confluents de celle-ci avec la Marne et l'Oise."
                                       " Paris est également le chef-lieu de la région Île-de-France"
                                       " et le centre de la métropole du Grand Paris, créée en 2016.",
                            "contentmodel": "wikitext",
                            "pagelanguage": "fr",
                            "pagelanguagehtmlcode": "fr",
                            "pagelanguagedir": "ltr",
                            "touched": "2021-06-30T14:45:08Z",
                            "lastrevid": 184122607,
                            "length": 408610,
                            "fullurl": "https://fr.wikipedia.org/wiki/Paris",
                            "editurl": "https://fr.wikipedia.org/w/index.php?title=Paris&action=edit",
                            "canonicalurl": "https://fr.wikipedia.org/wiki/Paris"
                        },
                    },
                }
            }

    longitude = 48.85658
    latitude = 2.35183

    wiki_api_url = "https://fr.wikipedia.org/w/api.php?"

    payload = {
            "action": "query",
            "format": "json",
            "ggscoord": f"{longitude}|{latitude}",
            "generator": "geosearch",
            "prop": "extracts|info",
            "explaintext": True,
            "exsentences": 3,
            "inprop": "url",
        }

    def mock_get_wiki_info(url=wiki_api_url, param=payload):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get_wiki_info)

    request = Wiki(longitude, latitude)
    result = request.json_result
    expected_result = {
        'title': 'Paris',
        'sentence': "Paris (/pa.ʁi/) est la commune la plus peuplée et la capitale de la France."
                    "\nElle se situe au cœur d'un vaste bassin sédimentaire aux sols fertiles et au climat tempéré,"
                    " le bassin parisien, sur une boucle de la Seine, entre les confluents de"
                    " celle-ci avec la Marne et l'Oise. Paris est également le chef-lieu de la région"
                    " Île-de-France et le centre de la métropole du Grand Paris, créée en 2016.",
        'url': 'https://fr.wikipedia.org/wiki/Paris'
    }

    assert result == expected_result


def test_get_wiki_failure(monkeypatch):

    class MockResponse:

        def __init__(self):
            self.status_code = 404

        @staticmethod
        def json():
            return {"error": "bad"}

    longitude = 48.85658
    latitude = 2.35183

    wiki_api_url = "https://fr.wikipedia.org/w/api.php?"

    payload = {
            "action": "query",
            "format": "json",
            "ggscoord": f"{longitude}|{latitude}",
            "generator": "geosearch",
            "prop": "extracts|info",
            "explaintext": True,
            "exsentences": 3,
            "inprop": "url",
        }

    def mock_get_wiki_info(url=wiki_api_url, param=payload):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get_wiki_info)

    request = Wiki(longitude, latitude)
    result = request.json_result

    assert result is None
