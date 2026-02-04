import pytest

from binary_tree.recursive_15 import create_tree as create_tree_15
from binary_tree.non_recursive_16 import create_tree as create_tree_16


@pytest.mark.parametrize(
    "source, preorder, inorder, postorder",
    [
        (
            "8 (3 (1, 6 (4,7)), 10 (, 14(13,)))",
            "8 3 1 6 4 7 10 14 13",
            "1 3 4 6 7 8 10 13 14",
            "1 4 7 6 3 13 14 10 8",
        ),
        (
            "10(,14(13,))",
            "10 14 13",
            "10 13 14",
            "13 14 10",
        ),
        (
            "5",
            "5",
            "5",
            "5",
        ),
        (
            "7(3,)",
            "7 3",
            "3 7",
            "3 7",
        ),
    ],
)
def test_recursive_traverses(source, preorder, inorder, postorder):
    tree = create_tree_15(source)

    assert tree.traversePreOrder() == preorder
    assert tree.traverseInOrder() == inorder
    assert tree.traversePostOrder() == postorder


@pytest.mark.parametrize(
    "source, preorder",
    [
        (
            "8 (3 (1, 6 (4,7)), 10 (, 14(13,)))",
            "8 3 1 6 4 7 10 14 13",
        ),
        (
            "10(,14(13,))",
            "10 14 13",
        ),
        (
            "5",
            "5",
        ),
        (
            "7(3,)",
            "7 3",
        ),
    ],
)
def test_non_recursive_preorder(source, preorder):
    tree = create_tree_16(source)
    assert tree.traversePreOrderNonRecursive() == preorder
