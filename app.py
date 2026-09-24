import requests


def prepare_demo_request():
    """
    Build an HTTP request locally without making any network call.
    """
    request = requests.Request(
        "GET",
        "https://example.com/api",
        params={"q": "demo"},
    )

    prepared = request.prepare()

    return {
        "method": prepared.method,
        "url": prepared.url,
    }
