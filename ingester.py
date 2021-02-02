from typing import List, Dict

import requests

API_KEY = 'bd5450c4f8a89cb98999'
COUNTRY_ENDPOINT = "https://free.currconv.com/api/v7/countries"
CONVERSION_ENDPOINT = "https://free.currconv.com/api/v7/convert"



class Ingester:

    def get_countries(self) -> List[Dict]:
        response = requests.get(COUNTRY_ENDPOINT, params={'apiKey': API_KEY})
        results = []
        if response.status_code == 200:
            json_response = response.json()

            results = [country_dict for country_dict in json_response["results"].values()]
            return results

