# сортировка по десяткам O(d*n) d-число разрядов

def radix_sort(arr: list):
    if not arr:
        return arr

    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10

    return arr


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        index = num // exp % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = arr[i] // exp % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output

# numbers = list(map(int, input("Введите числа через пробел: ").split()))
# print("Отсортированная последовательность:", *radix_sort(numbers))
