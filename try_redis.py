import redis

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

redis_client.set('foo', 'bar')

result = redis_client.get('foo')
print(result)