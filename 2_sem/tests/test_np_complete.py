import pytest

from np_complete.bin_packing_13 import bin_packing
from np_complete.graph_coloring_11 import color_graph
from np_complete.knapsack_12 import knapsack_01


def _is_valid_coloring(matrix: list, colors: list) -> bool:
    for vertex in range(len(matrix)):
        for other in range(len(matrix)):
            if matrix[vertex][other] and colors[vertex] == colors[other]:
                return False
    return True


def test_triangle_requires_three_colors() -> None:
    matrix = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
    ]

    assert color_graph(matrix, 2) == []
    coloring = color_graph(matrix, 3)
    assert coloring
    assert _is_valid_coloring(matrix, coloring)


def test_graph_with_loop_cannot_be_colored() -> None:
    assert color_graph([[1]], 1) == []


@pytest.mark.parametrize(
    "weights, values, capacity, expected_value, expected_items",
    [
        ([10, 20, 30], [60, 100, 120], 50, 220, [1, 2]),
        ([1, 2, 3], [6, 10, 12], 5, 22, [1, 2]),
        ([5], [10], 4, 0, []),
        ([], [], 10, 0, []),
    ],
)
def test_knapsack(
    weights: list,
    values: list,
    capacity: int,
    expected_value: int,
    expected_items: list,
) -> None:
    assert knapsack_01(weights, values, capacity) == (expected_value, expected_items)


def test_bin_packing_finds_optimum_better_than_greedy_solution() -> None:
    items = [6, 5, 3, 2, 2, 2]
    bins = bin_packing(items, 10)

    assert len(bins) == 2
    assert sorted(item for current_bin in bins for item in current_bin) == sorted(items)
    assert all(sum(current_bin) <= 10 for current_bin in bins)


def test_bin_packing_empty_input() -> None:
    assert bin_packing([], 10) == []
