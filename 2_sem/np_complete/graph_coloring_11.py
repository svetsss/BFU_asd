# раскрашивает граф заданным количеством цветов
def color_graph(matrix: list, color_count: int) -> list:
    if any(matrix[i][i] == 1 for i in range(len(matrix))):
        return []

    colors = [0] * len(matrix)

    def can_use_color(vertex: int, color: int) -> bool:
        for neighbor in range(len(matrix)):
            if matrix[vertex][neighbor] == 1 and colors[neighbor] == color:
                return False
        return True

    def paint(vertex: int) -> bool:
        if vertex == len(matrix):
            return True

        for color in range(1, color_count + 1):
            if can_use_color(vertex, color):
                colors[vertex] = color
                if paint(vertex + 1):
                    return True
                colors[vertex] = 0

        return False

    if paint(0):
        return colors
    return []


if __name__ == "__main__":
    matrix = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
    ]
    colors = color_graph(matrix, 3)

    print("Матрица смежности:", matrix)
    print("Раскраска:", colors)
