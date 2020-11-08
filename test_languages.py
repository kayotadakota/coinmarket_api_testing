import re
import pytest
import requests
from bs4 import BeautifulSoup as bs

@pytest.mark.parametrize('language', ['ru', 'ja', 'en', 'de'])
def test_ru_lang(language):
    url = f'https://coinmarketcap.com/{language}/'
    response = requests.get(url)
    pattern = r'\/[a-z]{2}\/'
    match = re.search(pattern, response.url)
    soup = bs(response.content, 'html.parser')

    assert response.status_code == 200
    assert match != None
    assert soup.html['lang'] == language
