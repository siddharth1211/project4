import redis
import random

with redis.Redis() as redis_client:
    print('random value', redis_client.rpop("queue"))