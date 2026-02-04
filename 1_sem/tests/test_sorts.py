import pytest


from sorts.shell_sort_7 import shell_sort
from sorts.radix_sort_8 import radix_sort
from sorts.heap_sort_9 import heap_sort
from sorts.merge_sort_10 import merge_sort
from sorts.quick_sort_11 import quick_sort


@pytest.mark.parametrize("sort_func", [shell_sort, radix_sort, heap_sort, 
                                       merge_sort, quick_sort])
@pytest.mark.parametrize("input_data, expected", [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([5, 3, 8, 1, 2], [1, 2, 3, 5, 8]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([3, 3, 2, 1, 2], [1, 2, 2, 3, 3]),
])
def test_sort_functions(sort_func, input_data, expected):
    assert sort_func(input_data.copy()) == expected