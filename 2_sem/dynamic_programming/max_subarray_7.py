# возвращает максимальную сумму и найденный подмассив
def max_subarray(numbers: list) -> tuple:
    if not numbers:
        return 0, []

    current_sum = best_sum = numbers[0]
    current_start = best_start = best_end = 0

    for i in range(1, len(numbers)):
        if current_sum < 0:
            current_sum = numbers[i]
            current_start = i
        else:
            current_sum += numbers[i]

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = i

    return best_sum, numbers[best_start:best_end + 1]


if __name__ == "__main__":
    numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, subarray = max_subarray(numbers)
    print("Массив:", numbers)
    print("Наибольшая сумма:", max_sum)
    print("Подмассив:", subarray)


# Алгоритм Кадана: если сумма отрицательная, переходим
# на элемент правее и берём его за начало нового подмассива.
