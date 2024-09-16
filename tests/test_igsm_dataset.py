import pytest
from igsm import igsmDataset

@pytest.fixture
def dataset():
    return igsmDataset()

def test_dataset_generation(dataset):
    num_problems = 10
    problems = dataset.generate(num_problems)
    assert len(problems) == num_problems
    for problem in problems:
        assert hasattr(problem, 'statement')
        assert hasattr(problem, 'solution')
        assert isinstance(problem.statement, str)
        assert isinstance(problem.solution, str)

def test_dataset_with_custom_config():
    custom_config = {
        'max_operations': 10,
        'arithmetic_mod': 10,
        'structure_layers': 3
    }
    dataset = igsmDataset(custom_config)
    problems = dataset.generate(5)
    assert len(problems) == 5
    # You might want to add more specific checks here to ensure the custom config is being used

def test_dataset_generates_unique_problems(dataset):
    num_problems = 20
    problems = dataset.generate(num_problems)
    statements = [problem.statement for problem in problems]
    assert len(set(statements)) == num_problems  # All problems should be unique