#!/usr/bin/env python3
""" Module for basic cache """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Class for basic cache """
    def put(self, key, item):
        """ Adds to the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Gets from the dictionary """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
