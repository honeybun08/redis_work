import redis

with redis.Redis() as redis_client:
    value = redis_client.brpop("queue")

print(int(value[1])) # перевели байты в нормальное число и выводим только число без названия queue