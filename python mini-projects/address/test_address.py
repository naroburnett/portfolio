from address import extract_city, \
 extract_state, extract_zipcode
import pytest

"10534 Joesph Drive, Highlands Ranch, CO 80134"

def test_extract_city():
    assert extract_city("10534 Joesph Drive, Highlands Ranch, CO 80134") == "Highlands Ranch"

def test_extract_state():
    assert extract_state("10534 Joesph Drive, Highlands Ranch, CO 80134") == "CO"

def test_extract_zipcode():
    assert extract_zipcode("10534 Joesph Drive, Highlands Ranch, CO 80134") == "80134"
pytest.main(["-v", "--tb=line", "-rN", __file__])