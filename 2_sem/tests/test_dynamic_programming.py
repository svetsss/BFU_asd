import math

import pytest

from dynamic_programming.coin_change_8 import count_change_ways
from dynamic_programming.egg_dropping_10 import (
    find_critical_floor,
    first_egg_floors,
    minimum_worst_case_throws,
)
from dynamic_programming.max_subarray_7 import max_subarray
from dynamic_programming.traveling_salesman_9 import traveling_salesman


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], (6, [4, -1, 2, 1])),
        ([-8, -3, -6, -5], (-3, [-3])),
        ([5], (5, [5])),
        ([0, 0, -1], (0, [0])),
    ],
)
def test_max_subarray(numbers: list, expected: tuple) -> None:
    assert max_subarray(numbers) == expected


def test_max_subarray_with_empty_array() -> None:
    assert max_subarray([]) == (0, [])


@pytest.mark.parametrize(
    "amount, coins, expected",
    [
        (5, [1, 2, 5], 4),
        (10, [2, 5, 3, 6], 5),
        (3, [2], 0),
        (0, [1, 2], 1),
        (5, [1, 2, 2, 5], 4),
    ],
)
def test_count_change_ways(amount: int, coins: list, expected: int) -> None:
    assert count_change_ways(amount, coins) == expected


def test_traveling_salesman_finds_shortest_cycle() -> None:
    matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]

    cost, route = traveling_salesman(matrix)

    assert cost == 80
    assert route[0] == route[-1] == 0
    assert set(route[:-1]) == {0, 1, 2, 3}
    assert len(route) == 5


def test_traveling_salesman_reports_missing_cycle() -> None:
    matrix = [
        [0, 2, 0],
        [2, 0, 3],
        [0, 3, 0],
    ]

    cost, route = traveling_salesman(matrix)

    assert math.isinf(cost)
    assert route == []


def test_traveling_salesman_with_one_city() -> None:
    assert traveling_salesman([[0]]) == (0, [0, 0])


def test_egg_dropping_strategy_for_100_floors() -> None:
    assert minimum_worst_case_throws(100) == 14
    assert first_egg_floors(100) == [14, 27, 39, 50, 60, 69, 77, 84, 90, 95, 99, 100]


@pytest.mark.parametrize("critical_floor", range(1, 101))
def test_egg_dropping_finds_every_critical_floor(critical_floor: int) -> None:
    found_floor, throws, checked_floors = find_critical_floor(critical_floor)

    assert found_floor == critical_floor
    assert throws == len(checked_floors)
    assert throws <= 14
