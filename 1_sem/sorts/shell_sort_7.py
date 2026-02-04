# улучшенная сортировка вставками только гэп сначала большой и стремится к очень маленькому O(n logn)

def shell_sort(arr: list):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


# numbers = list(map(int, input("Введите числа через пробел: ").split()))
# print("Отсортированная последовательность:", *shell_sort(numbers))