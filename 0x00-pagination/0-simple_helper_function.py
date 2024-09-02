#!/usr/bin/env python3
""" A simple Helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple of size two """
    return (page_size * (page - 1), page * page_size)
