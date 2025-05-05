from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Nathan", "Burnett") == "Burnett; Nathan"
    assert make_full_name("Jo Nathan", "O'Brian") == "O'Brian; Jo Nathan"

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Burnett; Nathan") == "Burnett"
    assert extract_family_name("O'Brian; Jo Nathan") == "O'Brian"

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Burnett; Nathan") == "Nathan"
    assert extract_given_name("O'Brian; Jo Nathan") == "Jo Nathan"

pytest.main(["-v", "--tb=line", "-rN", __file__])
