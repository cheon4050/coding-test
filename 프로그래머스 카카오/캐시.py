from collections import deque


def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    for city in cities:
        city = city.upper()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.appendleft(city)
        else:
            answer += 5
            cache.appendleft(city)
            if len(cache) > cacheSize:
                cache.pop()
    return answer
