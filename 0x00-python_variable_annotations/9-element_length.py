#!/usr/bin/env python3
""" Annotates """

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Duck typing """
    return [(i, len(i)) for i in lst]
