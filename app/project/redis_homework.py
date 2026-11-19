from redis_utils.redis_client import redis_client

redis_client.set("favorite_car", "toyota supra")
redis_client.set("favorite_pet", "cat", ex=7200)

redis_client.delete("shopping_list")
redis_client.rpush("shopping_list", "bread", "eggs", "apples")
redis_client.expire("shopping_list", 604800)

redis_client.delete("cake_ingredients")
redis_client.hset("cake_ingredients", mapping={"flour": 250, "milk": 500})
redis_client.hincrby("cake_ingredients", "sugar", 300)
redis_client.hset("cake_ingredients", "sugar", 500)

print("favorite_car:", redis_client.get("favorite_car"))
print("favorite_pet:", redis_client.get("favorite_pet"), "TTL:", redis_client.ttl("favorite_pet"))
print("shopping_list:", redis_client.lrange("shopping_list", 0, -1), "TTL:", redis_client.ttl("shopping_list"))
print("cake_ingredients:", redis_client.hgetall("cake_ingredients"))