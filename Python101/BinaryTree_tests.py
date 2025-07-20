import unittest
from BinaryTree import Node, BinaryTree


class Node_tests(unittest.TestCase):
    def test_Node_object_creation(self):
        n = Node(0)
        self.assertEqual(isinstance(n, Node), True)

    def test_Node_value(self):
        n = Node(0)
        self.assertEqual(n.value, 0)

    def test_Node_update_value(self):
        n = Node(0)
        n.value = 1
        self.assertEqual(n.value, 1)

    def test_Node_left(self):
        n = Node(0)
        n.left = Node(1)
        self.assertEqual(n.left.value, 1)

    def test_Node_right(self):
        n = Node(0)
        n.right = Node(2)
        self.assertEqual(n.right.value, 2)


class BinaryTree_tests(unittest.TestCase):
    def test_BinaryTree_object_creation(self):
        """Verify a BinaryTree object can be instantiated"""
        bt = BinaryTree()
        self.assertEqual(isinstance(bt, BinaryTree), True)


class BinaryTree_insert_tests(unittest.TestCase):
    def test_BinaryTree_insert_one_node(self):
        bt = BinaryTree()
        bt.insert(10)
        self.assertEqual(bt.search(10), True)

    def test_BinaryTree_insert_two_nodes(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(5)
        self.assertEqual(bt.search(5), True)

    def test_BinaryTree_insert_three_nodes(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(5)
        bt.insert(15)
        self.assertEqual(bt.search(15), True)

    def test_BinaryTree_insert_two_levels(self):
        bt = BinaryTree()
        bt.insert(6)
        bt.insert(4)
        bt.insert(5)
        bt.insert(12)
        bt.insert(15)
        bt.insert(18)
        bt.insert(10)
        self.assertEqual(bt.inorder_traversal(), [4, 5, 6, 10, 12, 15, 18])


class BinaryTree_search_tests(unittest.TestCase):
    def test_BinaryTree_search_no_nodes(self):
        bt = BinaryTree()
        self.assertEqual(bt.search(10), False)

    def test_BinaryTree_search_one_node(self):
        bt = BinaryTree()
        bt.insert(10)
        self.assertEqual(bt.search(10), True)

    def test_BinaryTree_search_non_existing_node(self):
        bt = BinaryTree()
        bt.insert(10)
        self.assertEqual(bt.search(5), False)


class BinaryTree_inorder_traversal_tests(unittest.TestCase):
    def test_BinaryTree_inorder_traversal_no_nodes(self):
        bt = BinaryTree()
        self.assertEqual(bt.inorder_traversal(), [])

    def test_BinaryTree_inorder_traversal_one_node(self):
        bt = BinaryTree()
        bt.insert(10)
        self.assertEqual(bt.inorder_traversal(), [10])

    def test_BinaryTree_inorder_traversal_two_nodes(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(20)
        self.assertEqual(bt.inorder_traversal(), [10, 20])

    def test_BinaryTree_inorder_traversal_three_nodes(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(20)
        bt.insert(5)
        self.assertEqual(bt.inorder_traversal(), [5, 10, 20])


class BinaryTree_height_tests(unittest.TestCase):
    def test_BinaryTree_height_empty_tree_is_zero_levels(self):
        bt = BinaryTree()
        self.assertEqual(bt.height(bt.root), 0)

    def test_BinaryTree_height_one_node_is_one_level(self):
        bt = BinaryTree()
        bt.insert(10)
        self.assertEqual(bt.height(bt.root), 1)

    def test_BinaryTree_height_two_nodes_is_two_levels(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(20)
        self.assertEqual(bt.height(bt.root), 2)

    def test_BinaryTree_height_three_levels(self):
        bt = BinaryTree()
        bt.insert(10)
        bt.insert(5)
        bt.insert(2)
        bt.insert(8)
        bt.insert(15)
        bt.insert(12)
        bt.insert(18)
        self.assertEqual(bt.height(bt.root), 3)
