#!/usr/bin/env python3
""" Module for LIFO cache """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Class for LIFO cache """
    def __init__(self):
        """ Initialization function """
        super().__init__()
        self.last = ''

    def put(self, key, item):
        """ Adds to the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print('DISCARD: {}'.format(self.last))
                del self.cache_data[self.last]
            self.last = key

    def get(self, key):
        """ Gets from the dictionary """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
