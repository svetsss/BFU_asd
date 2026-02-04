# берет опору делит на лево и право и рекурсивно сортирует, лучше пивот рандом
# от лог до н квадрат

def quick_sort(arr: list):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)


# numbers = list(map(int, input("Введите числа через пробел: ").split()))
# print("Отсортированная последовательность:", *quick_sort(numbers))
