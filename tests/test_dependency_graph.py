import pytest
from igsm.core import DependencyGraph, StructureGraph
from igsm.config import DEFAULT_CONFIG

@pytest.fixture
def dependency_graph():
    return DependencyGraph(DEFAULT_CONFIG)

@pytest.fixture
def structure():
    return StructureGraph(DEFAULT_CONFIG).generate()

def test_dependency_graph_generation(dependency_graph, structure):
    dependencies = dependency_graph.generate(structure)
    assert isinstance(dependencies, dict)
    assert len(dependencies) > 0
    for param, info in dependencies.items():
        assert 'dependencies' in info
        assert 'operation' in info

def test_dependency_graph_evaluation(dependency_graph, structure):
    dependencies = dependency_graph.generate(structure)
    values = {param: 1 for param in dependencies.keys()}  # Assign 1 to all parameters
    result = dependency_graph.evaluate(dependencies, values)
    assert isinstance(result, dict)
    assert len(result) == len(dependencies)
    for param, value in result.items():
        assert 0 <= value < DEFAULT_CONFIG['arithmetic_mod']

def test_dependency_graph_max_operations(dependency_graph, structure):
    dependencies = dependency_graph.generate(structure)
    assert len(dependencies) <= DEFAULT_CONFIG['max_operations']