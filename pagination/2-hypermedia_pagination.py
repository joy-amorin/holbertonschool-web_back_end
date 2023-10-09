#!/usr/bin/env python3
""" TASK 3 """
import csv
from typing import List, Dict
import math
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ pagination program """
    tupla: Tuple[int, int] = (page * page_size - page_size, page * page_size)
    return tupla


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
        """ returns the items from the asked pages """
        assert type(page) == int
        assert type(page_size) == int
        assert page >= 1
        assert page_size >= 1
        pagination = index_range(page, page_size)
        self.dataset()
        return self.__dataset[pagination[0]:pagination[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ returns a dict with information """
        self.dataset()
        total_pages: int = math.ceil(len(self.__dataset) / page_size)

        if page + 1 > total_pages:
            next_page = None
        else:
            next_page = page + 1

        if page - 1 < 1:
            prev_page = None
        else:
            prev_page = page - 1

        dict_data: Dict = {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return dict_data
