
import redis
import random


with redis.Redis() as redis_server: # как только заканч. команды с табом, поток автоматически закроется
    redis_server.lpush("queue", random.randint(0, 22)) # пушим влево рандомное число в промежутке

          