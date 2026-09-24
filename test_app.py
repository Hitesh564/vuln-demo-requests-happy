from app import prepare_demo_request


def test_prepare_demo_request():
    result = prepare_demo_request()

    assert result["method"] == "GET"
    assert "q=demo" in result["url"]
