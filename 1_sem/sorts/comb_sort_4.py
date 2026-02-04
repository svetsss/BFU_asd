def comb_sort(arr: list):
    gap = len(arr)
    flag = True
    while gap > 1 or flag:
        gap = max(1, int(gap / 1.3)) #кэфф 1.3 сокращения шага
        flag = False
        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                flag = True
    return arr


# numbers = list(map(int, input("Введите числа через пробел: ").split()))
# print("Отсортированная последовательность:", *comb_sort(numbers))
