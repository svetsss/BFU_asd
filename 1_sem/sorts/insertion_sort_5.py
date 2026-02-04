def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        insertion = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > insertion:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = insertion
    return arr


# numbers = list(map(int, input("Введите числа через пробел: ").split()))
# print("Отсортированная последовательность:", *insertion_sort(numbers))
