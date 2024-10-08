# igsm Dataset Generator

igsm (Infinite Grade School Math) is a Python package for generating diverse grade-school math problems and solutions. This tool allows researchers and educators to create customizable datasets for training and evaluating machine learning models on mathematical reasoning tasks.

## Features

- Generate structure graphs representing hierarchical relationships between entities
- Create dependency graphs to model mathematical relationships between parameters
- Produce problem statements and step-by-step solutions
- Customizable difficulty levels and problem types
- Extensible knowledge base for different categories and entities

## Installation

```bash
git clone https://github.com/kaminocode/iGSM.git
pip install -e .
```

## Quick Start

```python
from igsm.dataset import igsmDataset

# Generate a dataset with default settings
dataset = igsmDataset()
problems = dataset.generate(num_problems=100)

for problem in problems:
    print(problem.statement)
    print(problem.solution)
    print("---")
```

## Contributing

We welcome contributions! Please see our [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.