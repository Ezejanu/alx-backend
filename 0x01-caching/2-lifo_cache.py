#!/usr/bin/python3
"""LIFO Cache module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching and is
    a caching system using LIFO algorithm
    """

    def __init__(self):
        """Initialise the LIFOCache instance"""
        super().__init__()

    def put(self, key, item):
        """
        Assign the item value to the key in the cache using LIFO algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If the cache is full, remove the last item (LIFO)
                last_key = list(self.cache_data.keys())[-1]
                print("DISCARD:", last_key)
                del self.cache_data[last_key]

            # Add the new item to the cache
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in the cache linked to the key"""
        if key is not None:
            return self.cache_data.get(key)
