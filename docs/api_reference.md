# igsm API Reference

## igsm.dataset

### igsmDataset

The main class for generating igsm datasets.

#### `__init__(self, config: Dict = None)`

Initialize the igsmDataset with an optional configuration dictionary.

Parameters:
- `config` (Dict, optional): A dictionary of configuration options. If not provided, default configuration will be used.

#### `generate(self, num_problems: int) -> List[Problem]`

Generate a specified number of problems.

Parameters:
- `num_problems` (int): The number of problems to generate.

Returns:
- List[Problem]: A list of generated Problem objects.

## igsm.core

### StructureGraph

#### `__init__(self, config: Dict)`

Initialize the StructureGraph with a configuration dictionary.

Parameters:
- `config` (Dict): A dictionary of configuration options.

#### `generate() -> Dict`

Generate a structure graph.

Returns:
- Dict: A dictionary representing the generated structure graph.

#### `get_item_by_type(category: str, item_type: str) -> Dict`

Get a random item of a specific type from a category.

Parameters:
- `category` (str): The category to select from.
- `item_type` (str): The type of item to select.

Returns:
- Dict: A dictionary representing the selected item.

### DependencyGraph

#### `__init__(self, config: Dict)`

Initialize the DependencyGraph with a configuration dictionary.

Parameters:
- `config` (Dict): A dictionary of configuration options.

#### `generate(structure: Dict) -> Dict[str, Dict]`

Generate a dependency graph based on the given structure.

Parameters:
- `structure` (Dict): A dictionary representing the problem structure.

Returns:
- Dict[str, Dict]: A dictionary representing the generated dependency graph.

### ProblemGenerator

#### `__init__(self, config: Dict)`

Initialize the ProblemGenerator with a configuration dictionary.

Parameters:
- `config` (Dict): A dictionary of configuration options.

#### `generate(dependency_graph: Dict[str, Dict]) -> str`

Generate a problem statement based on the given dependency graph.

Parameters:
- `dependency_graph` (Dict[str, Dict]): A dictionary representing the dependency graph.

Returns:
- str: The generated problem statement.

### SolutionGenerator

#### `__init__(self, config: Dict)`

Initialize the SolutionGenerator with a configuration dictionary.

Parameters:
- `config` (Dict): A dictionary of configuration options.

#### `generate(dependency_graph: Dict[str, Dict]) -> str`

Generate a step-by-step solution based on the given dependency graph.

Parameters:
- `dependency_graph` (Dict[str, Dict]): A dictionary representing the dependency graph.

Returns:
- str: The generated step-by-step solution.

## igsm.config

### DEFAULT_CONFIG

A dictionary containing the default configuration for the igsm module.

### validate_config(config: Dict) -> Dict

Validate the given configuration and return a validated configuration dictionary.

Parameters:
- `config` (Dict): A dictionary of configuration options to validate.

Returns:
- Dict: A validated configuration dictionary.

## igsm.utils

### load_yaml(file_path: str) -> Dict

Load a YAML file and return its contents as a dictionary.

Parameters:
- `file_path` (str): The path to the YAML file.

Returns:
- Dict: The contents of the YAML file as a dictionary.

### load_categories(base_path: str) -> Dict[str, List[Dict]]

Load category data from YAML files in the given base path.

Parameters:
- `base_path` (str): The base path where the category YAML files are located.

Returns:
- Dict[str, List[Dict]]: A dictionary of categories, where each category is a list of items.