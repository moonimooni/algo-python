# https://leetcode.com/problems/lru-cache/

from typing import Deque, Dict
from collections import deque

# ing
class LRUCache:
    __capacity: int
    __lru_keys: Deque
    __cache: Dict

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__lru_keys = deque([])
        self.__cache = dict()

    def get(self, key: int) -> int:
        if key not in self.__cache:
            return -1

        self.__lru_keys.remove(key)
        self.__lru_keys.append(key)
        return self.__cache[key]

    def put(self, key: int, value: int) -> None:
        if len(self.__cache) == self.__capacity:
            deleted_data = self.__lru_keys.popleft()
            del self.__cache[deleted_data]

        self.__cache.update({key: value})
        self.__lru_keys.append(key)
        return


obj = LRUCache(2)
print(obj.put(1, 1))
print(obj.put(2, 2))
print(obj.get(1))
print(obj.put(3, 3))
print(obj.get(2))
print(obj.put(4, 4))
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
