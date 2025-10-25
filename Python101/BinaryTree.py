from typing import List


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the tree (BST style)."""
        if not self.root:
            self.root = BinaryTreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left:
                self._insert_recursive(node.left, value)
            else:
                node.left = BinaryTreeNode(value)
        else:
            if node.right:
                self._insert_recursive(node.right, value)
            else:
                node.right = BinaryTreeNode(value)

    def search(self, value):
        """Search for a value in the tree."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        """Return list of values in inorder (left-root-right)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def height(self, root) -> int:
        """Returns the height of the binary tree."""
        h = 0
        if root is None:
            h = 0
        else:
            l_height = self.height(root.left)
            r_height = self.height(root.right)
            h += 1 + max(l_height, r_height)
        return h

    def levels(self, root) -> List[List[int]]:
        """Returns a list of nodes grouped by levels starting from the top"""
        levels = []
        if not root:
            return levels

        def helper(node: BinaryTreeNode, level: int) -> None:
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.value)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels
