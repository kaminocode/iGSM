import pytest
from igsm.core import SolutionGenerator, StructureGraph, DependencyGraph
from igsm.config import DEFAULT_CONFIG

@pytest.fixture
def solution_generator():
    return SolutionGenerator(DEFAULT_CONFIG)

@pytest.fixture
def dependency_graph():
    structure = StructureGraph(DEFAULT_CONFIG).generate()
    return DependencyGraph(DEFAULT_CONFIG).generate(structure)

def test_solution_generation(solution_generator, dependency_graph):
    solution = solution_generator.generate(dependency_graph)
    assert isinstance(solution, str)
    assert len(solution) > 0
    assert solution.count(';') == len(dependency_graph) - 1  # Each parameter should have one semicolon except the last

def test_solution_includes_all_parameters(solution_generator, dependency_graph):
    solution = solution_generator.generate(dependency_graph)
    for param in dependency_graph.keys():
        category, item = param.split('.')
        assert item in solution
        assert category in solution

def test_solution_has_correct_format(solution_generator, dependency_graph):
    solution = solution_generator.generate(dependency_graph)
    lines = solution.split('\n')
    for line in lines:
        assert line.startswith("Define ")
        assert " as " in line
        assert line.endswith(".")