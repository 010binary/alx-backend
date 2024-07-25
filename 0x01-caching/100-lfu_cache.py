#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - caching system inherit from BaseCaching
      - uses LFU algorithm for cache replacement
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.lru = defaultdict(OrderedDict)
        self.min_frequency = 0

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self._update(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    self._evict()
                self.frequency[key] = 1
                self.lru[1][key] = None
                self.min_frequency = 1
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self._update(key)
            return self.cache_data[key]
        return None

    def _update(self, key):
        """ Update frequency and LRU for a key
        """
        freq = self.frequency[key]
        self.frequency[key] += 1
        del self.lru[freq][key]
        if not self.lru[freq] and freq == self.min_frequency:
            self.min_frequency += 1
        self.lru[freq + 1][key] = None

    def _evict(self):
        """ Evict the least frequently used item
        """
        lfu_key, _ = self.lru[self.min_frequency].popitem(last=False)
        del self.cache_data[lfu_key]
        del self.frequency[lfu_key]
        print(f"DISCARD: {lfu_key}")

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))
