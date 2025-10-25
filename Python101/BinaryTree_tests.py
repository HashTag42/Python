import unittest
from BinaryTree import BinaryTreeNode, BinaryTree


class Node_tests(unittest.TestCase):
    def test_Node_object_creation(self):
        n = BinaryTreeNode(0)
        self.assertTrue(isinstance(n, BinaryTreeNode))

    def test_Node_value(self):
        n = BinaryTreeNode(0)
        self.assertEqual(n.value, 0)

    def test_Node_update_value(self):
        n = BinaryTreeNode(0)
        n.value = 1
        self.assertEqual(n.value, 1)

    def test_Node_left(self):
        n = BinaryTreeNode(0)
        n.left = BinaryTreeNode(1)
        self.assertEqual(n.left.value, 1)

    def test_Node_right(self):
        n = BinaryTreeNode(0)
        n.right = BinaryTreeNode(2)
        self.assertEqual(n.right.value, 2)


class BinaryTree__init__tests(unittest.TestCase):
    def test_BinaryTree_object_creation(self):
        """Verify a BinaryTree object can be instantiated"""
        bt = BinaryTree()
        self.assertTrue(isinstance(bt, BinaryTree))


class BinaryTree__insert__tests(unittest.TestCase):
    def test_BinaryTree__insert__one_node(self):
        bt = BinaryTree()
        bt.insert(10)
        self.assertTrue(bt.search(10))

    def test_BinaryTree__insert__two_nodes(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(5)
        self.assertTrue(bt.search(5))

    def test_BinaryTree__insert__three_nodes(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(5)
        bt.insert(15)
        self.assertTrue(bt.search(15))

    def test_BinaryTree__insert__two_levels(self):
        bt = BinaryTree()
        bt.insert(6)
        bt.insert(4)
        bt.insert(5)
        bt.insert(12)
        bt.insert(15)
        bt.insert(18)
        bt.insert(10)
        self.assertEqual(bt.inorder_traversal(), [4, 5, 6, 10, 12, 15, 18])


class BinaryTree__search__tests(unittest.TestCase):
    def test_BinaryTree__search__no_nodes(self):
        bt = BinaryTree()
        self.assertFalse(bt.search(10))

    def test_BinaryTree__search__one_node(self):
        bt = BinaryTree()
        bt.insert(10)
        self.assertTrue(bt.search(10))

    def test_BinaryTree__search__non_existing_node(self):
        bt = BinaryTree()
        bt.insert(10)
        self.assertFalse(bt.search(5))


class BinaryTree__inorder_traversal__tests(unittest.TestCase):
    def test_BinaryTree__inorder_traversal__no_nodes(self):
        bt = BinaryTree()
        self.assertEqual(bt.inorder_traversal(), [])

    def test_BinaryTree__inorder_traversal__one_node(self):
        bt = BinaryTree()
        bt.insert(10)
        self.assertEqual(bt.inorder_traversal(), [10])

    def test_BinaryTree__inorder_traversal__two_nodes(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(20)
        self.assertEqual(bt.inorder_traversal(), [10, 20])

    def test_BinaryTree__inorder_traversal__three_nodes(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(20)
        bt.insert(5)
        self.assertEqual(bt.inorder_traversal(), [5, 10, 20])


class BinaryTree__height__tests(unittest.TestCase):
    def test_BinaryTree__height__empty_tree_is_zero_levels(self):
        bt = BinaryTree()
        self.assertEqual(bt.height(bt.root), 0)

    def test_BinaryTree__height__one_node_is_one_level(self):
        bt = BinaryTree()
        bt.insert(10)
        self.assertEqual(bt.height(bt.root), 1)

    def test_BinaryTree__height__two_nodes_is_two_levels(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(20)
        self.assertEqual(bt.height(bt.root), 2)

    def test_BinaryTree__height__three_levels(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(5)
        bt.insert(2)
        bt.insert(8)
        bt.insert(15)
        bt.insert(12)
        bt.insert(18)
        self.assertEqual(bt.height(bt.root), 3)


class BinaryTree__levels__tests(unittest.TestCase):
    def test_BinaryTree__levels__no_nodes(self):
        bt = BinaryTree()
        self.assertEqual(bt.levels(bt.root), [])

    def test_BinaryTree__levels__one_node(self):
        bt = BinaryTree()
        bt.insert(1)
        self.assertEqual(bt.levels(bt.root), [[1]])

    def test_BinaryTree__levels__three_levels(self):
        bt = BinaryTree()
        bt.insert(3)
        bt.insert(9)
        bt.insert(20)
        bt.insert(15)
        bt.insert(7)
        self.assertEqual(bt.levels(bt.root), [[3], [9], [7, 20], [15]])
