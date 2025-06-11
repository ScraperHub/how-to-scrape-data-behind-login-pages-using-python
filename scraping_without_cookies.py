import requests
from requests.exceptions import RequestException

TARGET_URL = "https://www.facebook.com/hashtag/music"
HEADERS = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
  'sec-fetch-mode': 'navigate'
}
OUTPUT_FILE_NAME = "output.html"

try:
    response = requests.get(TARGET_URL, headers=HEADERS)
    response.raise_for_status()
    
    html_content = response.text
    with open(OUTPUT_FILE_NAME, "w", encoding="utf-8") as file:
        file.write(response.text)

    print(f"\nPage successfully saved to '{OUTPUT_FILE_NAME}'\n")

except RequestException as error:
    print(f"\n Failed to fetch the page: {error}\n")
