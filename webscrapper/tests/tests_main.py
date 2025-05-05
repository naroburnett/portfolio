import pytest
from unittest.mock import patch, MagicMock
from src.__main__ import htmlScrapper, singlePageHtmlScrapper, test_url_class

# filepath: d:\natha\GitHub\BlackTie-Scrapper\tests\test_tests_main.py



@patch("src.__main__.requests.get")
@patch("src.__main__.url")
def test_htmlScrapper(mock_url, mock_requests):
    # Mock the response from requests.get
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    # Mock the url class
    mock_webpage = MagicMock()
    mock_webpage.get_soup.return_value = "<html></html>"
    mock_webpage.get_title.return_value = "Test_Title"
    mock_webpage.get_url.return_value = "https://example.com"
    mock_url.return_value = mock_webpage

    # Run the function
    htmlScrapper()

    # Assertions
    mock_requests.assert_called_once_with("https://stagingultraluxhealth.com")
    mock_webpage.get_soup.assert_called_once()
    mock_webpage.get_title.assert_called_once()


@patch("src.__main__.requests.get")
@patch("src.__main__.url")
def test_singlePageHtmlScrapper(mock_url, mock_requests):
    # Mock the input
    with patch("builtins.input", side_effect=["https://example.com", "Test_Folder"]):
        # Mock the response from requests.get
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_requests.return_value = mock_response

        # Mock the url class
        mock_webpage = MagicMock()
        mock_webpage.get_soup.return_value = "<html></html>"
        mock_webpage.get_title.return_value = "Test_Title"
        mock_url.return_value = mock_webpage

        # Run the function
        singlePageHtmlScrapper()

        # Assertions
        mock_requests.assert_called_once_with("https://example.com")
        mock_webpage.get_soup.assert_called_once()
        mock_webpage.get_title.assert_called_once()


@patch("src.__main__.url")
def test_test_url_class(mock_url):
    # Mock the input
    with patch("builtins.input", return_value="https://example.com"):
        # Mock the url class
        mock_webpage = MagicMock()
        mock_webpage.get_html.return_value.status_code = 200
        mock_webpage.get_links_count.return_value = 5
        mock_webpage.get_links.return_value = ["https://example.com/page1", "https://example.com/page2"]
        mock_url.return_value = mock_webpage

        # Run the function
        test_url_class()

        # Assertions
        mock_webpage.get_html.assert_called_once()
        mock_webpage.get_links_count.assert_called_once()
        mock_webpage.get_links.assert_called_once()