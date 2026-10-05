# находит минимальное количество бросков для двух яиц
def minimum_worst_case_throws(floors: int = 100) -> int:
    throws = 0
    checked_floors = 0

    while checked_floors < floors:
        throws += 1
        checked_floors += throws

    return throws


# возвращает этажи, с которых бросают первое яйцо
def first_egg_floors(floors: int = 100) -> list:
    step = minimum_worst_case_throws(floors)
    current_floor = 0
    result = []

    while current_floor < floors:
        current_floor = min(floors, current_floor + step)
        result.append(current_floor)
        step -= 1

    return result


# имитирует поиск критического этажа
def find_critical_floor(critical_floor: int, floors: int = 100) -> tuple:
    checked = []
    last_safe_floor = 0

    for current_floor in first_egg_floors(floors):
        checked.append(current_floor)

        if current_floor >= critical_floor:
            for floor in range(last_safe_floor + 1, current_floor):
                checked.append(floor)
                if floor == critical_floor:
                    return floor, len(checked), checked

            return current_floor, len(checked), checked

        last_safe_floor = current_floor

    return 0, len(checked), checked


if __name__ == "__main__":
    critical_floor = 73
    floor, throws, checked = find_critical_floor(critical_floor)

    print("Критический этаж:", floor)
    print("Количество бросков:", throws)
    print("Проверенные этажи:", checked)
