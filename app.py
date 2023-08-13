from flask import Flask, request, jsonify
import requests
from cache import RedisCache

app = Flask(__name__)
cache = RedisCache()

GNEWS_API_URL = "https://gnews.io/api/v4/search"
# https://gnews.io/api/v4/{endpoint}?apikey=API_KEY "https://gnews.io/api/v4/search"

@app.route('/news', methods=['GET'])
def get_news():
    keywords = request.args.get('keywords')
    # cached_response = cache.get(keywords)
    
    # if cached_response:
    #     return jsonify(cached_response)
    
    params = {
        'q': keywords,
        'token': 'ca34c717caaa6e1c1401ef9582dbaced',  # Replace with your GNews API key
    }
    
    response = requests.get(GNEWS_API_URL, params=params)
    articles = response.json().get('articles', [])
    
    # cache.set(keywords, articles, timeout=3600)  # Cache for 1 hour
    
    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True)
