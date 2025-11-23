'''
Implements a graph object.
'''
from GraphNode import GraphNode
from typing import Generic, List, Optional, TypeVar
T = TypeVar("T")


class Graph(Generic[T]):
    ################################################################################
    # region CONSTRUCTOR
    def __init__(self, directed=False) -> None:
        """Initializes a graph object"""
        self.nodes: List[GraphNode] = []
        self.directed = directed
    # endregion
    ################################################################################

    ################################################################################
    # region PUBLIC INTERFACE
    def add_node(self, node: GraphNode) -> None:
        """Add a new node to the graph"""
        if node not in self.nodes:
            self.nodes.append(node)

    def add_edge(self, node1: GraphNode, node2: GraphNode) -> None:
        """Add an edge between two nodes"""
        node1.add_node(node2)
        if not self.directed:
            node2.add_node(node1)

    def find_node(self, value: T) -> Optional[GraphNode]:
        """Find a node by its value"""
        for node in self.nodes:
            if node.value == value:
                return node
        return None

    def remove_edge(self, node1: GraphNode, node2: GraphNode) -> None:
        """Remove an edge between two nodes"""
        node1.remove_node(node2)
        if not self.directed:
            node2.remove_node(node1)
    # endregion
    ################################################################################

    ################################################################################
    # region DUNDER METHODS
    def __repr__(self) -> str:
        """Return a developer-friendly representation of the graph"""
        return f"Graph(nodes={len(self.nodes)}, directed={self.directed})"
    # endregion
    ################################################################################
