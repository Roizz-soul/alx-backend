#!/usr/bin/env python3
""" Module for Least recently use LRU cache """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Class for LRU cache """
    def __init__(self):
        """ Initialization function """
        super().__init__()
        self.access = {}

    def put(self, key, item):
        """ Adds to the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item
            to_pop = ''

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_pop = min(self.access, key=self.access.get)
                print('DISCARD: {}'.format(to_pop))
                del self.cache_data[to_pop]
                del self.access[to_pop]

            for i in self.access.keys():
                self.access[i] -= 1
            self.access[key] = 0

    def get(self, key):
        """ Gets from the dictionary """
        if key is None or self.cache_data.get(key) is None:
            return None
        if self.access != {}:
            for i in self.access.keys():
                self.access[i] -= 1
            self.access[key] = 0
        return self.cache_data.get(key)
