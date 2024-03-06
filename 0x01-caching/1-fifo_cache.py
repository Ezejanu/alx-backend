#!/usr/bin/python3
"""FIFO Cache module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching and is
    a caching system using FIFO algorithm
    """

    def __init__(self):
        """Initialise the FIFOCache instance"""
        super().__init__()

    def put(self, key, item):
        """
        Assign the item value to the key in the cache using FIFO algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If the cache is full, remove the first item (FIFO)
                first_key = next(iter(self.cache_data))
                print("DISCARD:", first_key)
                del self.cache_data[first_key]

            # Add the new item to the cache
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in the cache linked to the key"""
        if key is not None:
            return self.cache_data.get(key)
