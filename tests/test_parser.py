import json
from simple_rss_reader.exceptions import InvalidXML, RequestError
from root import ROOT_DIR
from simple_rss_reader.reader import SimpleRssReader

def _test_data(obj):
    assert obj["headers"]["title"] == "RSS title"
    assert obj["headers"]["link"] == "https://github.com/barakbl/simple_rss_reader"

    assert len(obj["items"]) == 2
    assert obj["items"][0]["title"] == "Item 1"
    assert obj["items"][0]["link"] == "https://github.com/barakbl/simple_rss_reader?1"

def test_load_from_string():
    with open(f"{ROOT_DIR}/tests/assets/rss.xml") as f:
        xmlstr = f.read()
    a = SimpleRssReader(xmlstr)
    d = a.to_dict()
    _test_data(d)

    j = a.to_json()
    _test_data(json.loads(j))

    for item in a.get_items():
        assert len(item) == 3

def test_load_from_string_invalid_xml_source():
    ok = False
    try:
        SimpleRssReader("NOT AN XML")
    except InvalidXML:
        ok = True
    assert ok == True

def test_load_invalid_url():
    ok = False
    try:
        SimpleRssReader("https://goog3123123213")
    except RequestError:
        ok = True
    assert ok == True
