#!/usr/bin/env python3
"""A simple helper function"""

import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> tuple():
    """
    Calculate the start and end indices for a given page
    and page size in a paginated system.

    Parameters:
    - page (int): The page number (1-indexed) for which to calculate indices.
    - page_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing the start index (inclusive)
    and end index (exclusive) for the specified page.
    """

    # type: (int, int) -> Tuple[int, int]

    # Calculate the start index for the given page
    start_index = (page - 1) * page_size

    # Calculate the end index by adding the page size to the start index
    end_index = start_index + page_size

    return (start_index, end_index)


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
        """
        Retrieve a paginated portion of the dataset based on the specified
        page and page size.

        Parameters:
        - page (int): The page number (1-indexed). Default is 1.
        - page_size (int): The number of items per page. Default is 10.

        Returns:
        List[List]: A list containing rows of the dataset corresponding
        to the specified page.
        Returns an empty list if the input arguments are out of range.
        """

        assert isinstance(page, int) and page > 0,\
            "Page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0,\
            "Page size must be an integer greater than 0"

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        # Check if the calculated indexes are within the dataset range
        if start_index >= len(dataset) or end_index > len(dataset):
            return []

        # Return the paginated portion of the dataset
        return dataset[start_index:end_index]
