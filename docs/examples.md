# igsm Usage Examples

## Basic Usage

### Generating a Dataset

```python
from igsm import igsmDataset

# Create a dataset with default configuration
dataset = igsmDataset()

# Generate 100 problems
problems = dataset.generate(num_problems=100)

# Print each problem and its solution
for problem in problems:
    print("Problem:")
    print(problem.statement)
    print("\nSolution:")
    print(problem.solution)
    print("\n---\n")
```

## Advanced Usage

### Custom Configuration

```python
from igsm import igsmDataset

# Define a custom configuration
custom_config = {
    'structure_layers': 3,
    'min_items_per_layer': 2,
    'max_items_per_layer': 4,
    'max_operations': 20,
    'arithmetic_mod': 10,
    'query_type': 'leaf'
}

# Create a dataset with custom configuration
dataset = igsmDataset(custom_config)

# Generate 50 problems
problems = dataset.generate(num_problems=50)

# Process the generated problems...
```

### Working with Individual Components

```python
from igsm.core import StructureGraph, DependencyGraph, ProblemGenerator, SolutionGenerator
from igsm.config import DEFAULT_CONFIG

# Create individual components
structure_graph = StructureGraph(DEFAULT_CONFIG)
dependency_graph = DependencyGraph(DEFAULT_CONFIG)
problem_generator = ProblemGenerator(DEFAULT_CONFIG)
solution_generator = SolutionGenerator(DEFAULT_CONFIG)

# Generate a structure
structure = structure_graph.generate()

# Generate dependencies based on the structure
dependencies = dependency_graph.generate(structure)

# Generate a problem statement
problem_statement = problem_generator.generate(dependencies)

# Generate a solution
solution = solution_generator.generate(dependencies)

print("Problem:")
print(problem_statement)
print("\nSolution:")
print(solution)
```

## Extending igsm

### Custom StructureGraph

```python
from igsm.core import StructureGraph

class CustomStructureGraph(StructureGraph):
    def generate(self):
        # Custom logic to generate a structure
        structure = super().generate()
        # Add custom modifications to the structure
        return structure

# Use the custom structure graph in your dataset
custom_structure_graph = CustomStructureGraph(config)
# ... use custom_structure_graph in your problem generation pipeline
```

### Custom ProblemGenerator

```python
from igsm.core import ProblemGenerator

class CustomProblemGenerator(ProblemGenerator):
    def generate(self, dependency_graph):
        # Custom logic to generate a problem statement
        statement = super().generate(dependency_graph)
        # Add custom modifications to the problem statement
        return statement

# Use the custom problem generator in your dataset
custom_problem_generator = CustomProblemGenerator(config)
# ... use custom_problem_generator in your problem generation pipeline
```

These examples showcase various ways to use and extend the igsm module. You can customize the configuration, work with individual components, or extend the core classes to suit your specific needs.