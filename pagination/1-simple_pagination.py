#!/usr/bin/env python3
""" simple pagination """
import csv
from typing import List
import math
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ program """
    tupla: Tuple[int, int] = (page * page_size - page_size, page * page_size)
    return tupla


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get page  """
        assert type(page) == int
        assert type(page_size) == int
        assert page >= 1
        assert page_size >= 1
        pagination = index_range(page, page_size)
        self.dataset()
        return self.__dataset[pagination[0]:pagination[1]]
