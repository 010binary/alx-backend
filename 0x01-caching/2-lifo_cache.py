#!/usr/bin/env python3
""" LIFOCache module
"""


from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - caching system inherit from BaseCaching
      - uses LIFO algorithm for cache replacement
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    discarded_key = self.order.pop()
                    del self.cache_data[discarded_key]
                    print(f"DISCARD: {discarded_key}")
                else:
                    self.order.remove(key)
            
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
