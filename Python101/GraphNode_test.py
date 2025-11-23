from GraphNode import GraphNode


################################################################################
# region GraphNode.__init__()
def test_GraphNode__init__():
    gn = GraphNode(1)
    assert isinstance(gn, GraphNode)
# endregion
################################################################################


################################################################################
# region GraphNode.add_node()
def test_GraphNode_add_node():
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    gn1.add_node(gn2)
    assert gn1.get_nodes() == [gn2]


def test_GraphNode_add_node_twice():
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    gn1.add_node(gn2)
    gn1.add_node(gn2)
    assert gn1.get_nodes() == [gn2]
# endregion
################################################################################


################################################################################
# region GraphNode.get_nodes()
def test_GraphNode_get_nodes():
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    gn3 = GraphNode(3)
    gn1.add_node(gn2)
    gn1.add_node(gn3)
    assert gn1.get_nodes() == [gn2, gn3]
# endregion
################################################################################


################################################################################
# region GraphNode.remove_node()
def test_GraphNode_remove_node():
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    gn1.add_node(gn2)
    gn1.remove_node(gn2)
    assert gn1.get_nodes() == []


def test_GraphNode_remove_node_twice():
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    gn1.add_node(gn2)
    gn1.remove_node(gn2)
    gn1.remove_node(gn2)
    assert gn1.get_nodes() == []
# endregion
################################################################################


################################################################################
# region GraphNode.__eq__()
def test_GraphNode__eq__True():
    gnA = GraphNode(1)
    gnB = GraphNode(1)
    assert gnA == gnB


def test_GraphNode__eq__False():
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    assert gn1 != gn2


def test_GraphNode__eq__no_GraphNode():
    gn1 = GraphNode(1)
    assert gn1 != "A"
# endregion
################################################################################


################################################################################
# region GraphNode.__hash__()
def test_GraphNode__hash__():
    gn1 = GraphNode("A")
    assert hash(gn1) == hash("A")
# endregion
################################################################################


################################################################################
# region GraphNode.__repr__()
def test_GraphNode__repr__():
    gn1 = GraphNode(1)
    assert repr(gn1) == "GraphNode(1, nodes=[])"


def test_GraphNode__repr__one_node():
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    gn1.add_node(gn2)
    assert repr(gn1) == "GraphNode(1, nodes=[GraphNode(2, nodes=[])])"
# endregion
################################################################################
