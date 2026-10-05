# раскладывает предметы по минимальному количеству ящиков
def bin_packing(items: list, capacity: int) -> list:
    items = sorted(items, reverse=True)
    best_bins = [[item] for item in items]
    bins = []

    def search(item_number: int) -> None:
        nonlocal best_bins

        if item_number == len(items):
            if len(bins) < len(best_bins):
                best_bins = [current_bin.copy() for current_bin in bins]
            return

        if len(bins) >= len(best_bins):
            return

        item = items[item_number]

        for current_bin in bins:
            if sum(current_bin) + item <= capacity:
                current_bin.append(item)
                search(item_number + 1)
                current_bin.pop()

        bins.append([item])
        search(item_number + 1)
        bins.pop()

    search(0)
    return best_bins


if __name__ == "__main__":
    items = [6, 5, 3, 2, 2, 2]
    capacity = 10
    bins = bin_packing(items, capacity)

    print("Количество ящиков:", len(bins))
    print("Раскладка:", bins)
