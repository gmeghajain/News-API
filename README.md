# News-API

This is a simple API that interacts with the GNews API to fetch news articles like, fetching N news articles, finding a news article with a specific title or author, and searching by keywords. It includes caching using Redis to improve performance.

## Setup

### Requirements
1. Python version 3.11 or above
2. Redis Cache 

### Steps to setup
1. Clone this repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Replace `'API_KEY'` in `app.py` with your actual GNews API key.
4. Install Redis server (Visit the Redis official website (https://redis.io/download) and download the latest stable release of Redis)

## Running the Application

Run the Flask app by executing the following command in your terminal:

TERMINAL 1
```bash
redis-server
```
TERMINAL 2
```bash
python app.py
```

## APIs

### 1. Fetch N news article
#### HTTP Request

```GET http://127.0.0.1:5000/news?max={N}```

#### Query Parameters

max : This parameter allows you to specify the number of news articles returned by the API. The minimum value of this parameter is 1 and the maximum value is 10.

### 2. Search Article
#### HTTP Request

```GET http://127.0.0.1:5000/search?q={keyword}&in={title,description,content}```

#### Query Parameters

q : This parameter is mandatory.
This parameter allows you to specify your search keywords to find the news articles you are looking for. The keywords will be used to return the most relevant articles. It is possible to use logical operators with keywords.

in : This parameter allows you to choose in which attributes the keywords are searched. The attributes that can be set are title, description and content. It is possible to combine several attributes by separating them with a comma.
e.g. title,description
