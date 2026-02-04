class Node:
    def __init__(self, key: int):
        self.left = None
        self.right = None
        self.val = key


def create_tree(string: str):
    return create_subtree(string, 0, len(string))


def find_right_subtree(string: str, start: int, end: int) -> int:
    level = 0
    while start < end:
        if string[start] == '(':
            level += 1
        elif string[start] == ')':
            level -= 1
        elif string[start] == ',' and level == 1:
            return start + 1
        start += 1
    return -1


def create_subtree(string: str, start: int, end: int):
    while start < end and (string[start].isspace() or string[start] == '('):
        start += 1

    if start >= end or string[start] in ',)':
        return None

    number = ''
    while start < end and string[start].isdigit():
        number += string[start]
        start += 1

    if number == '':
        raise Exception("Неверная скобочная запись")

    node = Node(int(number))

    while start < end and string[start].isspace():
        start += 1

    if start >= end or string[start] != '(':
        return node

    right_start = find_right_subtree(string, start, end)
    if right_start == -1:
        raise Exception("Неверная скобочная запись")

    node.left = create_subtree(string, start + 1, right_start - 1)
    node.right = create_subtree(string, right_start, end - 1)
    return node


class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.val:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            elif value > current.val:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right
            else:
                raise Exception("Такое значение уже есть в дереве")

    def search(self, value: int):
        parent = None
        current = self.root

        while current:
            if value == current.val:
                return parent, current
            parent = current
            current = current.left if value < current.val else current.right

        return None, None

    def _min_node(self, node: Node) -> Node:
        current = node
        while current.left:
            current = current.left
        return current

    def _remove(self, node, value: int):
        if node is None:
            return None

        if value < node.val:
            node.left = self._remove(node.left, value)
            return node
        if value > node.val:
            node.right = self._remove(node.right, value)
            return node

        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        successor = self._min_node(node.right)
        node.val = successor.val
        node.right = self._remove(node.right, successor.val)
        return node

    def remove(self, value: int) -> None:
        self.root = self._remove(self.root, value)

    def to_brackets(self) -> str:
        def build(node):
            if node is None:
                return ""
            left = build(node.left)
            right = build(node.right)
            if node.left or node.right:
                return f"{node.val}({left},{right})"
            return str(node.val)

        return build(self.root)

    def traverse_preorder_non_recursive(self) -> str:
        if self.root is None:
            return ""
        stack = [self.root]
        result = []
        while stack:
            current = stack.pop()
            result.append(str(current.val))
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return " ".join(result)


def menu():
    print("Меню:")
    print("1) Добавить вершину")
    print("2) Найти вершину")
    print("3) Удалить вершину")
    print("4) Показать обход (прямой нерекурсивный)")
    print("0) Выход")


if __name__ == "__main__":
    text = input("Введите дерево (линейно-скобочная запись): ").strip()
    bst = BST(create_tree(text))

    while True:
        menu()
        command = input("Введите команду: ").strip()

        if command == "1":
            value = int(input("Введите значение для добавления: "))
            try:
                bst.insert(value)
                print("Значение добавлено")
            except Exception as e:
                print("Ошибка:", e)

        elif command == "2":
            value = int(input("Введите значение для поиска: "))
            parent, current = bst.search(value)
            if current is None:
                print("Значение не найдено")
            else:
                if parent is None:
                    print(f"Найдено: {current.val}. Это корень, родителя нет")
                else:
                    print(f"Найдено: {current.val}. Родитель: {parent.val}")

        elif command == "3":
            value = int(input("Введите значение для удаления: "))
            parent, current = bst.search(value)
            if current is None:
                print("Значение не найдено")
            else:
                bst.remove(value)
                print("Значение удалено")

        elif command == "4":
            result = bst.traverse_preorder_non_recursive()
            print("Обход:", result if result else "(пусто)")

        elif command == "0":
            break

    print("Дерево перед завершением программы:")
    print(bst.to_brackets())

# 8(3(1,6(4,7)),10(,14(13,)))
