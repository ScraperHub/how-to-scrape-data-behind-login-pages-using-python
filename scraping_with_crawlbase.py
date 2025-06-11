import json
import requests
from requests.exceptions import RequestException

API_TOKEN = "<Javascript requests token>"
TARGET_URL = "https://www.facebook.com/hashtag/music"
SCRAPER = "facebook-hashtag"
COOKIES = """
<cookies-goes-here>
"""
COUNTRY = "US"

API_ENDPOINT = "https://api.crawlbase.com/"

params = {
    "token": API_TOKEN,
    "url": TARGET_URL,
    "scraper": SCRAPER,
    "cookies": COOKIES,
    "country": COUNTRY
}

try:
    response = requests.get(API_ENDPOINT, params=params)
    response.raise_for_status()
    
    json_string_content = response.text
    json_data = json.loads(json_string_content)
    pretty_json = json.dumps(json_data, indent=2)
    print(pretty_json)

except RequestException as error:
    print(f"\nFailed to fetch the page: {error}\n")
