#!/usr/bin/env python3
"""Basic Cache Module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """Assign the item value to the key in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in the cache linked to the key
        """
        if key is not None:
            return self.cache_data.get(key)
