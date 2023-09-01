import requests
import time

# Replace 'YOUR_API_KEY' with your actual Google API key

# Add your api key here
api_key = ''


search_query = "student housing near Northern Illinois University"
url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={search_query}&key={api_key}"

results = []
next_page_token = None

while len(results) < 500:
    if next_page_token:
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={next_page_token}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    if 'results' in data:
        results.extend(data['results'])

    if 'next_page_token' in data:
        next_page_token = data['next_page_token']
        # The API requires a short delay before using the next page token
        time.sleep(2)
    else:
        break

print(len(results), "results retrieved.")

# Now you can work with the list of retrieved results as needed
for result in results:
    print(result['name'], result['formatted_address'])
