'''
Implements a graph node object.
'''
from typing import Generic, List, TypeVar
T = TypeVar("T")


class GraphNode(Generic[T]):
    ################################################################################
    # region CONSTRUCTOR
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.nodes: List[GraphNode] = []
    # endregion
    ################################################################################

    ################################################################################
    # region PUBLIC INTERFACE
    def add_neighbor(self, node: "GraphNode") -> None:
        if node not in self.nodes:
            self.nodes.append(node)

    def get_neighbors(self):
        return self.nodes

    def remove_neighbor(self, node: "GraphNode") -> None:
        if node in self.nodes:
            self.nodes.remove(node)
    # endregion
    ################################################################################

    ################################################################################
    # region DUNDER METHODS
    def __eq__(self, other: object) -> bool:
        return isinstance(other, GraphNode) and self.value == other.value

    def __format__(self, format_spec) -> str:
        return format(str(self.value), format_spec)

    def __hash__(self) -> int:
        return hash(self.value)

    def __lt__(self, other: object) -> bool:
        return isinstance(other, GraphNode) and self.value < other.value

    def __repr__(self) -> str:
        return f"GraphNode({self.value}, nodes={self.get_neighbors()})"
    # endregion
    ################################################################################
