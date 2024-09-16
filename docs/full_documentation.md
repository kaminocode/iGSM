# igsm (Infinite Grade School Math) Module Documentation

## Overview

The igsm module is designed to generate diverse grade-school math problems and solutions. It provides a flexible framework for creating customizable datasets for training and evaluating machine learning models on mathematical reasoning tasks.

## Module Structure

1. `igsm.core`: Core components for generating math problems
2. `igsm.config`: Configuration management
3. `igsm.utils`: Utility functions
4. `igsm.dataset`: Main dataset generation class

## Installation

You can install igsm using pip:

```bash
pip install igsm
```

## Quick Start

Here's a simple example to get you started:

```python
from igsm import igsmDataset

dataset = igsmDataset()
problems = dataset.generate(num_problems=100)

for problem in problems:
    print(problem.statement)
    print(problem.solution)
    print("---")
```

## Configuration

igsm uses a configuration system to customize the problem generation process. You can provide your own configuration when initializing the `igsmDataset` class:

```python
from igsm import igsmDataset

custom_config = {
    'max_operations': 20,
    'arithmetic_mod': 10,
    'structure_layers': 3
}

dataset = igsmDataset(custom_config)
```

For more details on available configuration options, see the API Reference.

## Extending igsm

igsm is designed to be extensible. You can create custom problem types by extending the core classes:

- Extend `StructureGraph` to create custom problem structures
- Extend `DependencyGraph` to define new types of mathematical relationships
- Extend `ProblemGenerator` to customize how problem statements are generated
- Extend `SolutionGenerator` to customize how solutions are generated

For examples of how to extend igsm, see the Examples documentation.

## Contributing

We welcome contributions to igsm! Please see our Contributing Guidelines for more information on how to get started.

## License

igsm is released under the MIT License. See the LICENSE file for more details.