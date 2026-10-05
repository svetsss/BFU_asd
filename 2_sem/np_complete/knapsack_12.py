# находит максимальную стоимость предметов в рюкзаке
def knapsack_01(weights: list, values: list, capacity: int) -> tuple:
    item_count = len(weights)
    table = [[0] * (capacity + 1) for _ in range(item_count + 1)]

    for item in range(1, item_count + 1):
        for current_capacity in range(capacity + 1):
            if weights[item - 1] <= current_capacity:
                without_item = table[item - 1][current_capacity]
                with_item = (
                    table[item - 1][current_capacity - weights[item - 1]]
                    + values[item - 1]
                )
                table[item][current_capacity] = max(without_item, with_item)
            else:
                table[item][current_capacity] = table[item - 1][current_capacity]

    selected_items = []
    current_capacity = capacity

    for item in range(item_count, 0, -1):
        if table[item][current_capacity] != table[item - 1][current_capacity]:
            selected_items.append(item - 1)
            current_capacity -= weights[item - 1]

    selected_items.reverse()
    return table[item_count][capacity], selected_items


if __name__ == "__main__":
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    max_value, selected_items = knapsack_01(weights, values, capacity)
    print("Максимальная стоимость:", max_value)
    print("Выбранные предметы:", selected_items)
