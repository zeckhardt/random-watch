import random
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define API endpoint and headers
BASE_URL = "https://api.themoviedb.org/3"
API_KEY = os.getenv("API_TOKEN")
HEADERS = {
    "accept": "application/json",
    "Authorization": f'Bearer {API_KEY}'
}

def fetch_url(url):
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_random_movie_title():
    page = random.randrange(500)
    url = f"{BASE_URL}/movie/popular?language=en-US&page={page}&region=US"
    response = fetch_url(url)
    results = response.get('results', [])
    random_movie = random.choice(results)
    return random_movie['title']

def get_random_show_title():
    page = random.randrange(500)
    url = f"{BASE_URL}/tv/popular?language=en-US&page={page}&region=US"
    response = fetch_url(url)
    results = response.get('results', [])
    random_show = random.choice(results)
    return random_show['name']

def main():
    print(get_random_show_title())
    print(get_random_movie_title())

if __name__ == '__main__':
    main()
