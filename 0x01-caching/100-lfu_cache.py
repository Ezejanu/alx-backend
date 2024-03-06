#!/usr/bin/python3
"""LFUCache module"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching and
    is a caching system using LFU algorithm
    """

    def __init__(self):
        """Initialise the LFUCache instance"""
        super().__init__()
        # Dictionary to keep track of the frequency of each key
        self.frequency = {}
        # Dictionary to keep track of the access time of each key
        self.access_time = {}
        # Counter for tracking access time
        self.time_counter = 0

    def put(self, key, item):
        """Assign the item value to the key in the cache using LFU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the frequency if key already exists
                self.frequency[key] += 1
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If the cache is full, find the least frequency used item
                lfu_keys = [k for k, v in self.frequency.items()
                            if v == min(self.frequency.values())]

                if len(lfu_keys) > 1:
                    # If there are multiple LFU items, use LRU to break the tie
                    lfu_keys.sort(key=lambda k: self.access_time[k])

                # Delete the LFU or LRU item
                lfu_key = lfu_keys[0]
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                del self.access_time[lfu_key]
                print("DISCARD:", lfu_key)

            # Add the new item to the cache and initialise the frequency
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.access_time[key] = self.time_counter
            self.time_counter += 1

    def get(self, key):
        """Return the value in the cache linked to the key"""
        if key is not None and key in self.cache_data:
            # Update the frequency and access time when accessing an item
            self.frequency[key] += 1
            self.access_time[key] = self.time_counter
            self.time_counter += 1
            return self.cache_data[key]
        return None
