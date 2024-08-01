#!/usr/bin/env python3
"""Task 9 Module"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate the below function parameters and return
    values with the appropriate types
    """
    
    return [(i, len(i)) for i in lst]