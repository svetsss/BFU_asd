from functools import lru_cache


NO_PATH = float("inf")


# находит кратчайший маршрут с возвращением в начальный город
def traveling_salesman(matrix: list, start: int = 0) -> tuple:
    city_count = len(matrix)
    all_cities = (1 << city_count) - 1

    @lru_cache(None)
    def search(city: int, visited: int) -> tuple:
        if visited == all_cities:
            if city != start and matrix[city][start] == 0:
                return NO_PATH, []
            return matrix[city][start], [start]

        min_distance = NO_PATH
        best_route = []

        for next_city in range(city_count):
            if visited & (1 << next_city):
                continue
            if matrix[city][next_city] == 0:
                continue

            distance, route = search(next_city, visited | (1 << next_city))
            distance += matrix[city][next_city]

            if distance < min_distance:
                min_distance = distance
                best_route = [next_city] + route

        return min_distance, best_route

    distance, route = search(start, 1 << start)
    if distance == NO_PATH:
        return NO_PATH, []
    return distance, [start] + route


if __name__ == "__main__":
    matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]

    distance, route = traveling_salesman(matrix)
    print("Кратчайшее расстояние:", distance)
    print("Маршрут:", route)


# Алгоритм Хелда — Карпа: search получает текущий город и маску посещённых.
# Например, 0001 означает, что посещён город 0, а 1111 — все четыре города.
# Рекурсией перебираем города, в которые есть путь, и считаем расстояние.
# Если новое расстояние меньше, сохраняем его и соответствующий маршрут.
