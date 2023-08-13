from flask import Flask, request, jsonify
import requests
from cache import RedisCache
import json

app = Flask(__name__)
cache = RedisCache()

GNEWS_API_URL = "https://gnews.io/api/v4/search"
GNEWS_TOP_HEADLINES_URL = "https://gnews.io/api/v4/top-headlines"
API_KEY = 'ca34c717caaa6e1c1401ef9582dbaced' # Replace with your GNews API key

@app.route('/news', methods=['GET'])
def get_n_news_article():
    n = request.args.get('max')
    cached_response = cache.get(n)
    
    if cached_response:
        return jsonify(json.loads(cached_response))
    
    params = {
        'category': 'general',
        'max': n,
        'token': API_KEY
    }
    response = requests.get(GNEWS_TOP_HEADLINES_URL, params=params)
    articles = response.json().get('articles', [])
    
    cache.set(n, json.dumps(articles), timeout=3600)  # Cache for 1 hour
    
    return jsonify(articles)

@app.route('/search', methods=['GET'])
def get_news():
    search_keyword = request.args.get('q')
    search_in = request.args.get('in')

    params = {
        'q': search_keyword,
        'in': search_in,
        'token': API_KEY,
    }
    cache_key = search_keyword + search_in
    cached_response = cache.get(cache_key)
    
    if cached_response:
        return jsonify(json.loads(cached_response))
    
    response = requests.get(GNEWS_API_URL, params=params)
    articles = response.json().get('articles', [])
    
    cache.set(cache_key, json.dumps(articles), timeout=3600)  # Cache for 1 hour
    
    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True)
