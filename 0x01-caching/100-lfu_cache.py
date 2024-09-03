#!/usr/bin/env python3
""" Module for Least frequently used LFU cache """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Class for LFU cache """
    def __init__(self):
        """ Initialization function """
        super().__init__()
        self.access = {}

    def put(self, key, item):
        """ Adds to the dictionary """
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                if self.access != {}:
                    self.access[key] += 1
                    print('Put: {}'.format(self.access))

            self.cache_data[key] = item
            to_pop = ''
            if len(self.cache_data) == 4:
                for i in self.cache_data.keys():
                    self.access[i] = 0
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_pop = min(self.access, key=self.access.get)
                print('DISCARD: {}'.format(to_pop))
                del self.cache_data[to_pop]
                if key in self.access.keys():
                    self.access[key] += 1
                else:
                    del self.access[to_pop]
                    self.access[key] = 1
                print('Put: {}'.format(self.access))

    def get(self, key):
        """ Gets from the dictionary """
        if key is None or self.cache_data.get(key) is None:
            return None
        if self.access != {}:
            self.access[key] += 1
            print('Get: {}'.format(self.access))
        return self.cache_data.get(key)
