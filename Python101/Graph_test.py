from GraphNode import GraphNode
from Graph import Graph
from unittest.mock import patch
import pytest


########################################################################################################################
# region test PyTest fixtures
@pytest.fixture
def empty_graph():
    """Create an empty graph"""
    return Graph()


@pytest.fixture
def simple_graph():
    """Create a simple linear graph: A -> B -> C"""
    g = Graph(directed=True)
    a = GraphNode('A')
    b = GraphNode('B')
    c = GraphNode('C')
    g.add_edge(a, b)
    g.add_edge(b, c)
    return g, a, b, c


@pytest.fixture
def complex_graph():
    """
    Create a more complex graph:
        A -> B -> D
        |    |
        v    v
        C -> E
    """
    g = Graph(directed=True)
    a = GraphNode('A')
    b = GraphNode('B')
    c = GraphNode('C')
    d = GraphNode('D')
    e = GraphNode('E')
    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(b, d)
    g.add_edge(b, e)
    g.add_edge(c, e)
    return g, a, b, c, d, e


@pytest.fixture
def cyclic_graph():
    """Create a graph with a cycle: A -> B -> C -> A"""
    g = Graph(directed=True)
    a = GraphNode('A')
    b = GraphNode('B')
    c = GraphNode('C')
    g.add_edge(a, b)
    g.add_edge(b, c)
    g.add_edge(c, a)
    return g, a, b, c


@pytest.fixture
def disconnected_graph():
    """Create a disconnected graph: A -> B  C -> D"""
    g = Graph(directed=True)
    a = GraphNode('A')
    b = GraphNode('B')
    c = GraphNode('C')
    d = GraphNode('D')
    g.add_edge(a, b)
    g.add_edge(c, d)
    return g, a, b, c, d
# endregion
########################################################################################################################


########################################################################################################################
# region test Graph.__init__(directed) -> None:
def test_Graph__init__():
    g = Graph()
    assert isinstance(g, Graph)
# endregion
########################################################################################################################


########################################################################################################################
# region test Graph.add_edge(from_node, to_node, weight) -> None:
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
########################################################################################################################


########################################################################################################################
# region test Graph.add_node(node) -> None:
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
########################################################################################################################


########################################################################################################################
# region test Graph.bfs(from_node, to_node) -> bool:
def test_Graph_bfs_same_node(simple_graph):
    """Test BFS when start and end nodes are the same"""
    g, a, b, c = simple_graph
    assert g.bfs(a, a) is True
    assert g.bfs(b, b) is True


def test_Graph_bfs_direct_connection(simple_graph):
    """Test BFS with directly connected nodes"""
    g, a, b, c = simple_graph
    assert g.bfs(a, b) is True
    assert g.bfs(b, c) is True


def test_Graph_bfs_indirect_connection(simple_graph):
    """Test BFS with indirectly connected nodes"""
    g, a, b, c = simple_graph
    assert g.bfs(a, c) is True


def test_Graph_bfs_no_path(simple_graph):
    """Test BFS when no path exists (directed graph)"""
    g, a, b, c = simple_graph
    assert g.bfs(c, a) is False
    assert g.bfs(b, a) is False


def test_Graph_bfs_node_not_in_graph(simple_graph):
    """Test BFS with node not in the graph"""
    g, a, b, c = simple_graph
    external_node = GraphNode('X')
    assert g.bfs(a, external_node) is False
    assert g.bfs(external_node, a) is False


def test_Graph_bfs_complex_path_exists(complex_graph):
    """Test BFS finds path in complex graph"""
    g, a, b, c, d, e = complex_graph
    assert g.bfs(a, d) is True
    assert g.bfs(a, e) is True
    assert g.bfs(b, e) is True
    assert g.bfs(c, e) is True


def test_Graph_bfs_complex_no_path(complex_graph):
    """Test BFS correctly identifies no path in complex graph"""
    g, a, b, c, d, e = complex_graph
    assert g.bfs(d, a) is False
    assert g.bfs(e, a) is False
    assert g.bfs(d, e) is False


def test_Graph_bfs_cyclic_graph(cyclic_graph):
    """Test BFS handles cycles correctly"""
    g, a, b, c = cyclic_graph
    assert g.bfs(a, c) is True
    assert g.bfs(b, a) is True
    assert g.bfs(c, b) is True


def test_Graph_bfs_disconnected_components(disconnected_graph):
    """Test BFS with disconnected graph components"""
    g, a, b, c, d = disconnected_graph
    # Within same component
    assert g.bfs(a, b) is True
    assert g.bfs(c, d) is True

    # Across components
    assert g.bfs(a, c) is False
    assert g.bfs(a, d) is False
    assert g.bfs(b, c) is False


def test_Graph_bfs_undirected_graph():
    """Test BFS with undirected graph"""
    g = Graph(directed=False)
    a = GraphNode('A')
    b = GraphNode('B')
    c = GraphNode('C')

    g.add_edge(a, b)
    g.add_edge(b, c)

    # All nodes should be reachable from any node
    assert g.bfs(a, c) is True
    assert g.bfs(c, a) is True
    assert g.bfs(b, a) is True


def test_Graph_bfs_ingle_node_graph():
    """Test BFS with single node"""
    g = Graph()
    a = GraphNode('A')
    g.add_node(a)

    assert g.bfs(a, a) is True


def test_Graph_bfs_empty_graph(empty_graph):
    """Test BFS with empty graph"""
    a = GraphNode('A')
    b = GraphNode('B')
    assert empty_graph.bfs(a, b) is False


def test_Graph_bfs_search_route_alias(simple_graph):
    """Test that search_route works as alias to bfs"""
    g, a, b, c = simple_graph
    # Assuming search_route = bfs
    assert g.search_route(a, c) == g.bfs(a, c)
    assert g.search_route(c, a) == g.bfs(c, a)
# endregion
########################################################################################################################


########################################################################################################################
# region test Graph.find_node(value) -> Optional[GraphNode]:
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
########################################################################################################################


########################################################################################################################
# region test Graph.has_edge(from_node, to_node) -> bool:
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
########################################################################################################################


########################################################################################################################
# region test Graph.print_matrix() -> None:
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
########################################################################################################################


########################################################################################################################
# region test Graph.remove_edge(from_node, to_node) -> None:
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
########################################################################################################################
