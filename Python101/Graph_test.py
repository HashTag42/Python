from GraphNode import GraphNode
from Graph import Graph


################################################################################
# region Graph.__init__()
def test_Graph__init__():
    g = Graph()
    assert isinstance(g, Graph)
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
# region Graph.remove_edge()
def test_Graph_remove_edge_directed_True():
    g = Graph(directed=True)
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    g.add_node(gn1)
    g.add_node(gn2)
    g.add_edge(gn1, gn2)
    g.remove_edge(gn1, gn2)


def test_Graph_remove_edge_directed_False():
    g = Graph(directed=False)
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    g.add_node(gn1)
    g.add_node(gn2)
    g.add_edge(gn1, gn2)
    g.remove_edge(gn1, gn2)
# endregion
################################################################################
