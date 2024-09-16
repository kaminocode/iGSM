import pytest
from igsm.core import StructureGraph
from igsm.config import DEFAULT_CONFIG

@pytest.fixture
def structure_graph():
    return StructureGraph(DEFAULT_CONFIG)

def test_structure_graph_generation(structure_graph):
    structure = structure_graph.generate()
    assert isinstance(structure, dict)
    assert len(structure) <= DEFAULT_CONFIG['structure_layers']
    for category, items in structure.items():
        assert DEFAULT_CONFIG['min_items_per_layer'] <= len(items) <= DEFAULT_CONFIG['max_items_per_layer']

def test_get_item_by_type(structure_graph):
    # Assuming 'School' category exists and has items of type 'High School'
    item = structure_graph.get_item_by_type('School', 'High School')
    assert item is not None
    assert item['type'] == 'High School'

def test_get_random_item(structure_graph):
    # Assuming 'School' category exists
    item = structure_graph.get_random_item('School')
    assert item is not None
    assert 'name' in item
    assert 'type' in item

def test_get_all_items(structure_graph):
    # Assuming 'School' category exists
    items = structure_graph.get_all_items('School')
    assert isinstance(items, list)
    assert len(items) > 0
    assert all('name' in item and 'type' in item for item in items)

def test_get_item_types(structure_graph):
    # Assuming 'School' category exists
    types = structure_graph.get_item_types('School')
    assert isinstance(types, list)
    assert len(types) > 0
    assert 'High School' in types  # Assuming 'High School' is a valid type