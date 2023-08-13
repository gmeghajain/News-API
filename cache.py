import redis

class RedisCache:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
    
    def get(self, key):
        cached_data = self.redis_client.get(key)
        if cached_data:
            return cached_data.decode('utf-8')
        return None
    
    def set(self, key, value, timeout):
        self.redis_client.setex(key, timeout, value)
