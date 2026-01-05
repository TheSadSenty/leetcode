from collections import OrderedDict


class LRUCache(object):
    def __init__(self, capacity):
        self._cache: OrderedDict[int, int] = OrderedDict()
        self._cap = capacity

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1

        val = self._cache.pop(key)

        self._cache[key] = val

        return self._cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._cache.pop(key)

        self._cache[key] = value

        if len(self._cache) > self._cap:
            self._cache.popitem(last=False)
