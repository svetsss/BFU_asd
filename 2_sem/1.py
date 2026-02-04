import math


# определяет ориентацию трёх точек
def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


# вычисляет квадрат расстояния между точками
def dist2(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2


# проверяет существование трёх неколлинеарных точек
def has_noncollinear(points):
    n = len(points)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if orient(points[i], points[j], points[k]) != 0:
                    return True
    return False


# строит выпуклую оболочку методом Грэхема
def graham_scan(points):
    pts = list(set(points))
    if len(pts) < 3:
        return []
    p0 = min(pts, key=lambda p: (p[1], p[0]))
    pts.sort(key=lambda p: (
        math.atan2(p[1] - p0[1], p[0] - p0[0]),
        dist2(p0, p)
    ))
    hull = []
    for p in pts:
        while len(hull) >= 2 and orient(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    return hull if len(hull) >= 3 else []


def main():
    n = int(input())
    points = [tuple(map(float, input().split())) for _ in range(n)]
    if not has_noncollinear(points):
        print("Выпуклая оболочка не существует")
        return
    hull = graham_scan(points)
    if not hull:
        print("Выпуклая оболочка не существует")
    else:
        print("Выпуклая оболочка существует")
        for x, y in hull:
            print(x, y)


if __name__ == "__main__":
    main()


# Метод Грэхема:
# Выбирается опорная точка P0 с минимальной координатой y
# (при равенстве — с минимальным x).
# Остальные точки сортируются по полярному углу относительно P0.
# Последовательно просматриваются точки в порядке сортировки.
# Если три последние точки образуют правый поворот
# (или коллинеарны), средняя точка удаляется.
# В результате остаются только вершины выпуклой оболочки,
# упорядоченные против часовой стрелки.

