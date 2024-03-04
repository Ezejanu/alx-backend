#!/usr/bin/env python3
"""A simple helper function"""
from typing import Tuple


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
