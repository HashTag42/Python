'''
Implements a graph node object.
'''
from typing import Generic, List, TypeVar
from enum import Enum, auto
T = TypeVar("T")


class NodeState(Enum):
    UNVISITED = auto()
    VISITED = auto()
    VISITING = auto()


class GraphNode(Generic[T]):
    ################################################################################
    # region CONSTRUCTOR
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.nodes: List[GraphNode] = []
        self.state: NodeState = NodeState.UNVISITED
    # endregion
    ################################################################################

    ################################################################################
    # region PUBLIC INTERFACE
    def add_neighbor(self, node: "GraphNode") -> None:
        if node not in self.nodes:
            self.nodes.append(node)

    def get_neighbors(self) -> List["GraphNode"]:
        return self.nodes

    def is_visited(self) -> bool:
        return self.state == NodeState.VISITED

    def mark_visited(self) -> None:
        self.state = NodeState.VISITED

    def mark_visiting(self) -> None:
        self.state = NodeState.VISITING

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
