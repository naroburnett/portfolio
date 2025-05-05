import pytest
from unittest.mock import patch, MagicMock
from classes import url, UrlManager

# filepath: d:\natha\GitHub\BlackTie-Scrapper\src\test_classes.py



@patch("classes.requests.get")
def test_url_get_html(mock_get):
    # Mock the response from requests.get
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = "<html></html>"
    mock_get.return_value = mock_response

    # Create a url instance and call get_html
    test_url = url("https://example.com")
    response = test_url.get_html()

    # Assertions
    mock_get.assert_called_once_with("https://example.com")
    assert response.status_code == 200


@patch("classes.requests.get")
@patch("classes.BeautifulSoup")
def test_url_get_soup(mock_soup, mock_get):
    # Mock the response from requests.get
    mock_response = MagicMock()
    mock_response.text = "<html><title>Test</title></html>"
    mock_get.return_value = mock_response

    # Mock BeautifulSoup
    mock_soup.return_value.title.string = "Test"

    # Create a url instance and call get_soup
    test_url = url("https://example.com")
    soup = test_url.get_soup()

    # Assertions
    mock_get.assert_called_once_with("https://example.com")
    mock_soup.assert_called_once_with("<html><title>Test</title></html>", "html.parser")
    assert soup.title.string == "Test"


@patch("classes.requests.get")
def test_url_get_links(mock_get):
    # Mock the response from requests.get
    mock_response = MagicMock()
    mock_response.text = '<html><a href="https://example.com/page1"></a><a href="https://example.com/page2"></a></html>'
    mock_get.return_value = mock_response

    # Create a url instance and call get_links
    test_url = url("https://example.com")
    links = test_url.get_links()

    # Assertions
    mock_get.assert_called_once_with("https://example.com")
    assert links == ["https://example.com/page1", "https://example.com/page2"]


def test_url_set_and_get_url():
    # Create a url instance and set a new URL
    test_url = url("https://example.com")
    test_url.set_url("https://newexample.com")

    # Assertions
    assert test_url.get_url() == "https://newexample.com"


def test_url_clear():
    # Create a url instance and clear the URL
    test_url = url("https://example.com")
    test_url.clear()

    # Assertions
    assert test_url.get_url() is None


def test_url_manager_add_and_get_next_url():
    # Create a UrlManager instance
    manager = UrlManager("https://example.com")

    # Add URLs and get the next URL
    manager.add_url("https://example.com/page1")
    manager.add_url("https://example.com/page2")
    next_url = manager.get_next_url()

    # Assertions
    assert next_url == "https://example.com/page1"
    assert manager.has_urls_to_process() is True


def test_url_manager_is_native():
    # Create a UrlManager instance
    manager = UrlManager("https://example.com")

    # Check if URLs are native
    assert manager.is_native("https://example.com/page1") is True
    assert manager.is_native("https://otherdomain.com/page1") is False


def test_url_manager_urls_to_process_count():
    # Create a UrlManager instance
    manager = UrlManager("https://example.com")

    # Add URLs and check the count
    manager.add_url("https://example.com/page1")
    manager.add_url("https://example.com/page2")
    count = manager.urls_to_process_count()

    # Assertions
    assert count == "2 URLs left to process"