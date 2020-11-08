import os
import re
import json
import requests
import datetime

class TestResponse:

    def setup_method(self):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?'
        params = {
            'limit': 10,
            'sort': 'volume_24h'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': os.environ['coinmarket']
        }

        self.response = requests.get(url, headers=headers, params=params)

    def test_response_status_code(self):
        assert self.response.status_code == 200

    def test_response_time(self):
        reference = datetime.timedelta(milliseconds=500)
        assert self.response.elapsed < reference

    def test_valid_response(self):
        today = datetime.date.today()
        pattern = r'([0-9]{4})-([0-9]{2})-([0-9]{2})'
        data = json.loads(self.response.text)

        for list_ in data['data']:
            for key, value in list_.items():
                if key == 'last_updated':
                    year, month, day = map(int, re.search(pattern, value).groups())
                    latest_update = datetime.date(year, month, day)
                    assert latest_update == today

    def test_response_size(self):
        assert len(self.response.content) < 10000
