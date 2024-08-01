#!/usr/bin/env python3
"""Task 10 Module"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Augment the following code with the correct duck-typed annotations"""

    if lst:
        return lst[0]
    else:
        return None
