from GraphNode import GraphNode
from Graph import Graph
from unittest.mock import patch


################################################################################
# region Graph.__init__()
def test_Graph__init__():
    g = Graph()
    assert isinstance(g, Graph)
# endregion
################################################################################


################################################################################
# region Graph.add_edge()
def test_Graph_add_edge_directed_True():
    g = Graph(directed=True)
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    g.add_node(gn1)
    g.add_node(gn2)
    g.add_edge(gn1, gn2)


def test_Graph_add_edge_directed_False():
    g = Graph(directed=False)
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    g.add_node(gn1)
    g.add_node(gn2)
    g.add_edge(gn1, gn2)
# endregion
################################################################################


################################################################################
# region Graph.add_node()
def test_Graph_add_node():
    g = Graph()
    gn1 = GraphNode(1)
    g.add_node(gn1)
    assert repr(g) == "Graph(nodes=1, directed=False)"


def test_Graph_add_node_twice():
    g = Graph()
    gn1 = GraphNode(1)
    g.add_node(gn1)
    g.add_node(gn1)
    assert repr(g) == "Graph(nodes=1, directed=False)"


def test_Graph_add_node_two_nodes():
    g = Graph(True)
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    g.add_node(gn1)
    g.add_node(gn2)
    assert repr(g) == "Graph(nodes=2, directed=True)"
# endregion
################################################################################


################################################################################
# region Graph.find_node()
def test_Graph_find_node_one_node_Success():
    g = Graph()
    gn1 = GraphNode(1)
    g.add_node(gn1)
    assert g.find_node(1) == gn1


def test_Graph_find_node_multiple_nodes_Success():
    g = Graph()
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    gn3 = GraphNode(3)
    g.add_node(gn1)
    g.add_node(gn2)
    g.add_node(gn3)
    assert g.find_node(2) == gn2


def test_Graph_find_node_None():
    g = Graph()
    assert g.find_node(1) is None
# endregion
################################################################################


################################################################################
# region Graph.has_edge()
def test_Graph_has_edge_True():
    g = Graph()
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    g.add_node(gn1)
    g.add_node(gn2)
    g.add_edge(gn1, gn2)
    assert g.has_edge(gn1, gn2) is True


def test_Graph_has_edge_False():
    g = Graph()
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    g.add_node(gn1)
    g.add_node(gn2)
    g.add_edge(gn2, gn1)
    assert g.has_edge(gn1, gn2) is False
# endregion
################################################################################


################################################################################
# region Graph.print_matrix()
def test_Graph_print_matrix():
    g = Graph()
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    g.add_edge(gn1, gn2)
    expected = "      1   2\n1  : [0, 1]\n2  : [0, 0]\n"
    with patch('builtins.print') as mock_print:
        g.print_matrix()
        mock_print.assert_any_call(expected)
# endregion
################################################################################


# ################################################################################
# region Graph.remove_edge()
def test_Graph_remove_edge_True():
    g = Graph(directed=True)
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    g.add_node(gn1)
    g.add_node(gn2)
    g.add_edge(gn1, gn2)
    g.remove_edge(gn1, gn2)


def test_Graph_remove_edge_False():
    g = Graph(directed=False)
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    g.add_node(gn1)
    g.add_node(gn2)
    g.add_edge(gn1, gn2)
    g.remove_edge(gn1, gn2)


def test_Graph_remove_edge_non_existing_edge():
    g = Graph(directed=False)
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    g.add_node(gn1)
    g.add_node(gn2)
    # Attempt to remove a non-existing edge
    g.remove_edge(gn1, gn2)


def test_Graph_remove_edge_bidirectional():
    g = Graph(directed=False)
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    g.add_edge(gn1, gn2)
    g.add_edge(gn2, gn1)
    g.remove_edge(gn1, gn2)
# endregion
################################################################################
