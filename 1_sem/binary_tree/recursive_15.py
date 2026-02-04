class Node:
    def __init__(self, key: int):
        self.left = None
        self.right = None
        self.val = key

    def traversePreOrder(self) -> str:
        result = []
        self._preorder(self, result)
        return " ".join(result)

    def traverseInOrder(self) -> str:
        result = []
        self._inorder(self, result)
        return " ".join(result)

    def traversePostOrder(self) -> str:
        result = []
        self._postorder(self, result)
        return " ".join(result)

    def _preorder(self, node, result):
        if node is None:
            return
        result.append(str(node.val))
        self._preorder(node.left, result)
        self._preorder(node.right, result)

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(str(node.val))
        self._inorder(node.right, result)

    def _postorder(self, node, result):
        if node is None:
            return
        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(str(node.val))


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


if __name__ == "__main__":
    tree = create_tree(input("Введите дерево: ").strip())

    if tree is None:
        print("Дерево пустое")
    else:
        print("Прямой обход:", tree.traversePreOrder())
        print("Центральный обход:", tree.traverseInOrder())
        print("Концевой обход:", tree.traversePostOrder())
