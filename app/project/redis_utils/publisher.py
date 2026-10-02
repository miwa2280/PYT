import time
from redis_utils.redis_client import redis_client



for pub in range(0, 100):
    time.sleep(0.5)
    redis_client.publish('our_channel', f'message #{pub}')