#!/usr/bin/env python3
""" Module for Most recently use MRU cache """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Class for MRU cache """
    def __init__(self):
        """ Initialization function """
        super().__init__()
        self.mru = ''

    def put(self, key, item):
        """ Adds to the dictionary """
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.mru = key

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print('DISCARD: {}'.format(self.mru))
                del self.cache_data[self.mru]
                self.mru = key

    def get(self, key):
        """ Gets from the dictionary """
        if key is None or self.cache_data.get(key) is None:
            return None
        self.mru = key
        return self.cache_data.get(key)
