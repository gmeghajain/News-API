# News-API

This is a simple API that interacts with the GNews API to fetch news articles based on keywords. It includes caching using Redis to improve performance.

## Setup

1. Clone this repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Replace `'YOUR_GNEWS_API_KEY'` in `app.py` with your actual GNews API key.
4. Install Redis server (Visit the Redis official website (https://redis.io/download) and download the latest stable release of Redis)
5. Open a terminal and run cmd 'redis-server'

## Running the Application

Run the Flask app by executing the following command in your terminal:

```bash
python app.py
