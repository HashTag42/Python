'''
Implements a graph object.
'''
from GraphNode import GraphNode, NodeState
from Queue import Queue
from typing import Generic, List, Optional, TypeVar
T = TypeVar("T")


class Graph(Generic[T]):
    ################################################################################
    # region CONSTRUCTOR
    def __init__(self, directed: bool = False) -> None:
        """Initializes a graph object"""
        self.nodes: List[GraphNode] = []
        self.directed = directed
        self.matrix = {}
    # endregion
    ################################################################################

    ################################################################################
    # region PUBLIC INTERFACE
    def add_edge(self, from_node: GraphNode, to_node: GraphNode, weight: int = 1) -> None:
        """Add an edge between two nodes"""
        self.add_node(from_node)
        self.add_node(to_node)
        from_node.add_neighbor(to_node)
        self.matrix[from_node][to_node] = weight
        if not self.directed:
            to_node.add_neighbor(from_node)

    def add_node(self, node: GraphNode) -> None:
        """Add a new node to the graph"""
        if node not in self.nodes:
            self.nodes.append(node)
            self.matrix[node] = {}

    def bfs(self, from_node: GraphNode, to_node: GraphNode) -> bool:
        """
        Perform breadth-first search from start_node to to_node.
        Returns True if a path exists, False otherwise.
        """
        if from_node not in self.nodes or to_node not in self.nodes:
            return False
        if from_node == to_node:
            return True
        for node in self.nodes:
            node.mark_unvisited()
        queue = Queue()
        from_node.mark_visiting
        queue.enqueue(from_node)
        while not queue.is_empty():
            current: GraphNode = queue.dequeue()
            for neighbor in current.get_neighbors():
                if neighbor.state == NodeState.UNVISITED:
                    if neighbor == to_node:
                        return True
                    neighbor.mark_visiting
                    queue.enqueue(neighbor)
            current.mark_visited()
        return False

    def find_node(self, value: T) -> Optional[GraphNode]:
        """Find a node by its value"""
        for node in self.nodes:
            if node.value == value:
                return node
        return None

    def get_weight(self, from_node: GraphNode, to_node: GraphNode) -> int:
        """Get edge weight, return 0 if no edge"""
        if self.has_edge(from_node, to_node):
            return self.matrix[from_node][to_node]
        return 0

    def has_edge(self, from_node: GraphNode, to_node: GraphNode) -> bool:
        """Check if an edge exists"""
        return from_node in self.matrix and to_node in self.matrix[from_node]

    def print_matrix(self) -> None:
        """Return a str representation of the adjacency matrix"""
        result = ""
        nodes = sorted(self.nodes)
        result += "    " + " ".join(f"{n.value:3}" for n in nodes) + "\n"
        for from_node in nodes:
            row = [self.get_weight(from_node, to_node) for to_node in nodes]
            result += f"{from_node:3}: {row}\n"
        print(result)

    def remove_edge(self, from_node: GraphNode, to_node: GraphNode) -> None:
        """Remove an edge between two nodes"""
        from_node.remove_neighbor(to_node)
        if (from_node in self.matrix
                and to_node in self.matrix[from_node]):
            del self.matrix[from_node][to_node]
        if (not self.directed
                and to_node in self.matrix
                and from_node in self.matrix[to_node]):
            to_node.remove_neighbor(from_node)

    # Alias for bfs
    search_route = bfs
    # endregion
    ################################################################################

    ################################################################################
    # region DUNDER METHODS
    def __repr__(self) -> str:
        """Return a developer-friendly representation of the graph"""
        return f"Graph(nodes={len(self.nodes)}, directed={self.directed})"
    # endregion
    ################################################################################
