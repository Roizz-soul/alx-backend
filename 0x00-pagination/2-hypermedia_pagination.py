#!/usr/bin/env python3
""" A simple Helper function """
import csv
import math
from typing import Tuple, List, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple of size two """
    return (page_size * (page - 1), page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Gets the page were looking for """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        seth = self.dataset()
        ind = list(index_range(page, page_size))

        return seth[ind[0]: ind[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[
        str, Union[int, List[List], None]
    ]:
        """ Get hyper media """
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        total = math.ceil(len(dataset) / page_size)
        ret_dict = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page + 1 <= total else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total
        }

        return ret_dict
