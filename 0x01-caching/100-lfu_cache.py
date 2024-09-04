#!/usr/bin/env python3
""" Module for Least frequently used LFU cache """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Class for LFU cache """
    def __init__(self):
        """ Initialization function """
        super().__init__()
        self.accessF = {}
        self.accessR = {}

    def put(self, key, item):
        """ Adds to the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item
            to_pop = ''
            to_pip = ''
            check = 0

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_pop = min(self.accessF, key=self.accessF.get)
                for i in self.accessF.values():
                    if i == to_pop:
                        check += 1
                if check > 1:
                    to_pip = min(self.accessR, key=self.accessR.get)
                    print('DISCARD: {}'.format(to_pip))
                    del self.cache_data[to_pip]
                    del self.access[to_pip]
                else:
                    print('DISCARD: {}'.format(to_pop))
                    del self.cache_data[to_pop]
                    del self.accessF[to_pop]

            if key in self.accessF.keys():
                self.accessF[key] += 1
            else:
                self.accessF[key] = 0

            for i in self.accessR.keys():
                self.accessR[i] -= 1
            self.accessR[key] = 0

    def get(self, key):
        """ Gets from the dictionary """
        if key is None or self.cache_data.get(key) is None:
            return None
        if self.accessF != {}:
            self.accessF[key] += 1
            for i in self.accessR.keys():
                self.accessR[i] -= 1
            self.accessR[key] = 0
        return self.cache_data.get(key)
