#!/usr/bin/env python3
""" Module for Most recently use MRU cache """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Class for MRU cache """
    def __init__(self):
        """ Initialization function """
        super().__init__()
        self.access = {}
        self.mru = ''

    def put(self, key, item):
        """ Adds to the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) == 4 and self.access != {}:
                self.access[key] += 1
                self.mru = key
                print('Put: {}'.format(self.access))
            if len(self.cache_data) == 4 and self.access == {}:
                for i in self.cache_data.keys():
                    self.access[i] = 0
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print('DISCARD: {}'.format(self.mru))
                del self.cache_data[self.mru]
                if key in self.access.keys():
                    self.access[key] += 1
                    self.mru = key
                else:
                    del self.access[self.mru]
                    self.access[key] = 1
                    self.mru = key
                print('Put: {}'.format(self.access))

    def get(self, key):
        """ Gets from the dictionary """
        if key is None or self.cache_data.get(key) is None:
            return None
        if self.access != {}:
            self.access[key] += 1
            self.mru = key
            print('Get: {}'.format(self.access))
        return self.cache_data.get(key)
