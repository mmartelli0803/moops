from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def fetch_data(url, headers=None):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"General error occurred: {req_err}")
    return None

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def fetch_imdb_top_drama_movies():
    url = "https://www.imdb.com/search/title/?genres=drama&sort=year,desc"
    html = fetch_data(url, headers=headers)
    if html is None:
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    movies = []
    for item in soup.select('.lister-item-content'):
        try:
            title = item.h3.a.text
            summary = item.find_all('p', class_='text-muted')[1].text.strip()
            year = item.h3.find('span', class_='lister-item-year').text.strip("()")
            movies.append((title, summary, year))
        except Exception as e:
            print(f"Error parsing IMDb data: {e}")
    
    return movies

def fetch_wikipedia_top_drama_movies():
    url = "https://en.wikipedia.org/wiki/List_of_drama_films"
    html = fetch_data(url, headers=headers)
    if html is None:
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    movies = []
    for item in soup.select('table.wikitable i a'):
        try:
            title = item.text.strip()
            summary = "No summary available"
            year = "Unknown"
            movies.append((title, summary, year))
        except Exception as e:
            print(f"Error parsing Wikipedia data: {e}")
    
    return movies

def get_combined_movies():
    imdb_movies = fetch_imdb_top_drama_movies()
    wikipedia_movies = fetch_wikipedia_top_drama_movies()
    combined_movies = list({(title, summary, year) for title, summary, year in imdb_movies + wikipedia_movies})
    return combined_movies

@app.route('/top-drama-movies', methods=['GET'])
def top_drama_movies():
    movies = get_combined_movies()
    result = [{"title": title, "summary": summary, "year": year} for title, summary, year in movies]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
