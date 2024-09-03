#!/usr/bin/env python3
""" Module for FIFO cache """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Class for FIFO cache """
    def __init__(self):
        """ Initialization function """
        super().__init__()

    def put(self, key, item):
        """ Adds to the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print('DISCARD: {}'.format(
                            list(self.cache_data.keys())[0]
                            ))
                del self.cache_data[list(self.cache_data.keys())[0]]

    def get(self, key):
        """ Gets from the dictionary """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
