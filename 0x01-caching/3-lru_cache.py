#!/usr/bin/python3
"""LRUCache module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache inherits from BaseCaching and
    is a caching system using LRU algorithm
    """

    def __init__(self):
        """Initialise the LRUCache instance"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assign the item value to the key in the cache using LRU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the usage order if the key already exists
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If the cache is full, remove the least recently used item
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)

            # Add the new item to the cache and update the order
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Return the value in the cache linked to the key"""
        if key is not None and key in self.cache_data:
            # Update the usage order when accessing an item
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
