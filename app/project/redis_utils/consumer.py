from redis_utils.redis_client import redis_client

subscriber = redis_client.pubsub()
subscriber.subscribe('our_channel', "weather_odesa")
subscriber.subscribe('news')

for message in subscriber.listen():
    print(message)