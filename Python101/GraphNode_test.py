from GraphNode import GraphNode
import pytest


################################################################################
# region GraphNode.__init__()
def test_GraphNode__init__():
    gn = GraphNode(1)
    assert isinstance(gn, GraphNode)
# endregion
################################################################################


################################################################################
# region GraphNode.add_neighbor()
def test_GraphNode_add_neighbor():
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    gn1.add_neighbor(gn2)
    assert gn1.get_neighbors() == [gn2]


def test_GraphNode_add_neighbor_twice():
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    gn1.add_neighbor(gn2)
    gn1.add_neighbor(gn2)
    assert gn1.get_neighbors() == [gn2]
# endregion
################################################################################


################################################################################
# region GraphNode.get_neighbors()
def test_GraphNode_get_neighbors():
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    gn3 = GraphNode(3)
    gn1.add_neighbor(gn2)
    gn1.add_neighbor(gn3)
    assert gn1.get_neighbors() == [gn2, gn3]
# endregion
################################################################################


################################################################################
# region GraphNode.remove_neighbor()
def test_GraphNode_remove_neighbor():
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    gn1.add_neighbor(gn2)
    gn1.remove_neighbor(gn2)
    assert gn1.get_neighbors() == []


def test_GraphNode_remove_neighbor_twice():
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    gn1.add_neighbor(gn2)
    gn1.remove_neighbor(gn2)
    gn1.remove_neighbor(gn2)
    assert gn1.get_neighbors() == []
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
# region GraphNode.__format__()
@pytest.mark.parametrize("value,expected", [
    ('A', 'A'),
    ('ABC', 'ABC'),
    ('', ''),
    (42, '42'),
    (0, '0'),
    (-5, '-5'),
    (3.14, '3.14'),
    (None, 'None'),
    (True, 'True'),
    (False, 'False'),
])
def test_GraphNode__format__default_format_various_values(value, expected):
    """Test default formatting with various value types"""
    node = GraphNode(value)
    assert f"{node}" == expected


@pytest.mark.parametrize("value,width,expected", [
    ('A', 3, 'A  '),
    ('AB', 5, 'AB   '),
    ('ABC', 3, 'ABC'),
    ('ABCD', 2, 'ABCD'),
    ('', 3, '   '),
    (42, 5, '42   '),
])
def test_GraphNode__format__width_specification(value, width, expected):
    """Test width specification with various values"""
    node = GraphNode(value)
    assert f"{node:{width}}" == expected


@pytest.mark.parametrize("value,format_spec,expected", [
    ('X', '<5', 'X    '),
    ('X', '>5', '    X'),
    ('X', '^5', '  X  '),
    ('AB', '<6', 'AB    '),
    ('AB', '>6', '    AB'),
    ('AB', '^6', '  AB  '),
    (7, '<4', '7   '),
    (7, '>4', '   7'),
    (7, '^4', ' 7  '),
])
def test_GraphNode__format__alignment_variations(value, format_spec, expected):
    """Test different alignment options"""
    node = GraphNode(value)
    assert f"{node:{format_spec}}" == expected


@pytest.mark.parametrize("value,format_spec,expected", [
    ('A', '*>5', '****A'),
    ('A', '0>5', '0000A'),
    ('A', '-^7', '---A---'),
    ('A', '_<5', 'A____'),
    ('B', '=>6', '=====B'),
    ('C', '.^8', '...C....'),
])
def test_fill_characters(value, format_spec, expected):
    """Test various fill characters"""
    node = GraphNode(value)
    assert f"{node:{format_spec}}" == expected


@pytest.mark.parametrize("width", [1, 2, 3, 5, 10, 20])
def test_various_widths(width):
    """Test that width specification works correctly"""
    node = GraphNode('A')
    result = f"{node:{width}}"
    assert len(result) == width
    assert result.startswith('A')
    assert result.count(' ') == width - 1
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
# region GraphNode.__lt__()
def test_GraphNode__lt__True():
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    assert (gn1 < gn2) is True


def test_GraphNode__lt__False():
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    assert (gn2 < gn1) is False
# endregion
################################################################################


################################################################################
# region GraphNode.__repr__()
def test_GraphNode__repr__():
    gn1 = GraphNode(1)
    assert repr(gn1) == "GraphNode(1, nodes=[])"


def test_GraphNode__repr__one_neighbor():
    gn1 = GraphNode(1)
    gn2 = GraphNode(2)
    gn1.add_neighbor(gn2)
    assert repr(gn1) == "GraphNode(1, nodes=[GraphNode(2, nodes=[])])"
# endregion
################################################################################
