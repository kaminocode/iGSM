import pytest
from igsm.core import ProblemGenerator, StructureGraph, DependencyGraph
from igsm.config import DEFAULT_CONFIG

@pytest.fixture
def problem_generator():
    return ProblemGenerator(DEFAULT_CONFIG)

@pytest.fixture
def dependency_graph():
    structure = StructureGraph(DEFAULT_CONFIG).generate()
    return DependencyGraph(DEFAULT_CONFIG).generate(structure)

def test_problem_generation(problem_generator, dependency_graph):
    problem = problem_generator.generate(dependency_graph)
    assert isinstance(problem, str)
    assert len(problem) > 0
    assert "How many" in problem  # Assuming the question always starts with "How many"

def test_problem_includes_all_parameters(problem_generator, dependency_graph):
    problem = problem_generator.generate(dependency_graph)
    for param in dependency_graph.keys():
        category, item = param.split('.')
        assert item in problem
        assert category in problem