def calculate(expr: str) -> float:
    ops = {'+': 1, '-': 1, '*': 2, '/': 2}

    def apply(op, b, a):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/':
            if b == 0:
                raise ZeroDivisionError("Деление на ноль")
            return a / b

    values = []
    operators = []
    i = 0

    while i < len(expr):
        ch = expr[i]

        if ch.isspace():
            i += 1
            continue

        if ch.isdigit():
            num = 0
            while i < len(expr) and expr[i].isdigit():
                num = num * 10 + int(expr[i])
                i += 1
            values.append(num)
            continue

        if ch == '(':
            operators.append(ch)

        elif ch == ')':
            while operators and operators[-1] != '(':
                values.append(apply(operators.pop(), values.pop(), values.pop()))
            if not operators:
                raise ValueError("Неверные скобки")
            operators.pop()

        elif ch in ops:
            while (operators and operators[-1] in ops and
                   ops[operators[-1]] >= ops[ch]):
                values.append(apply(operators.pop(), values.pop(), values.pop()))
            operators.append(ch)

        elif ch == '=':
            break

        else:
            raise ValueError(f"Недопустимый символ: {ch}")

        i += 1

    while operators:
        if operators[-1] == '(':
            raise ValueError("Неверные скобки")
        values.append(apply(operators.pop(), values.pop(), values.pop()))

    if len(values) != 1:
        raise ValueError("Ошибка выражения")

    return values[0]


if __name__ == "__main__":
    expr = input("Введите выражение: ").strip()
    if not expr.endswith('='):
        print("Ошибка: выражение должно заканчиваться '='")
    else:
        try:
            result = calculate(expr)
            print("Результат:", result)
        except Exception as e:
            print("Ошибка:", e)
