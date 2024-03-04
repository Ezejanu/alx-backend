#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


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
        assert index is None or (isinstance(index, int) and index >= 0),\
            "Index must be None or a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0,\
            "Page size must be an integer greater than 0"

        dataset = self.dataset()
        current_index = index if index is not None else 0

        # Verify that the current index is within a valid range
        assert current_index < len(dataset), "Index is out of range"

        # Calculate the start and end indices for the current page
        start_index = current_index
        end_index = current_index + page_size

        # Verify that the end index is within the dataset range
        if end_index > len(dataset):
            end_index = len(dataset)

        # Return the dictionary with the requested information
        return {
            "index": start_index,
            "next_index": end_index,
            "page_size": page_size,
            "data": dataset[start_index:end_index]
        }
