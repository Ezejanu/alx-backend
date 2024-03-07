#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve information about the paginated dataset
        based on a specific index in a hypermedia-friendly format.
        """

        dataset = self.indexed_dataset()

        index = 0 if index is None else index
        assert 0 <= index < len(dataset), "Index is out of range"

        while index < len(dataset) and dataset[index] is None:
            index += 1

        end_index = index + page_size
        end_index = min(end_index, len(dataset))
        next_index = end_index

        # Return the dictionary with the requested information
        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": [dataset[i] for i in range(index, end_index)
                     if dataset[i] is not None]
        }
