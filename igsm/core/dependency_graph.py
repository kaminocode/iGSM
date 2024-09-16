import random
from typing import Dict, List, Tuple

class DependencyGraph:
    def __init__(self, config: Dict):
        self.config = config
        self.mod = config.get('arithmetic_mod', 23)

    def generate(self, structure: Dict) -> Dict[str, Dict]:
        dependency_graph = {}
        parameters = self._flatten_structure(structure)
        operation_count = 0
        max_operations = self.config.get('max_operations', 15)

        while parameters and operation_count < max_operations:
            param = random.choice(parameters)
            dependencies = self._generate_dependencies(parameters, param)
            operation = self._generate_operation(dependencies)
            dependency_graph[param] = {
                'dependencies': dependencies,
                'operation': operation
            }
            parameters.remove(param)
            operation_count += 1

        return dependency_graph

    def _flatten_structure(self, structure: Dict) -> List[str]:
        return [f"{category}.{item['name']}" for category, items in structure.items() for item in items]

    def _generate_dependencies(self, parameters: List[str], current_param: str) -> List[str]:
        num_dependencies = random.randint(0, min(3, len(parameters) - 1))
        return random.sample([p for p in parameters if p != current_param], num_dependencies)

    def _generate_operation(self, dependencies: List[str]) -> Tuple[str, List[int]]:
        operations = ['+', '-', '*']
        if not dependencies:
            return ('constant', [random.randint(1, self.mod - 1)])
        elif len(dependencies) == 1:
            return (random.choice(operations), [random.randint(1, self.mod - 1)])
        else:
            return (random.choice(operations), [])

    def evaluate(self, dependency_graph: Dict[str, Dict], values: Dict[str, int]) -> Dict[str, int]:
        result = values.copy()
        for param, info in dependency_graph.items():
            if param not in result:
                deps = info['dependencies']
                op, constants = info['operation']
                if op == 'constant':
                    result[param] = constants[0]
                elif op == '+':
                    result[param] = sum([result[d] for d in deps] + constants) % self.mod
                elif op == '-':
                    result[param] = (result[deps[0]] - sum([result[d] for d in deps[1:]] + constants)) % self.mod
                elif op == '*':
                    product = 1
                    for d in deps:
                        product = (product * result[d]) % self.mod
                    for c in constants:
                        product = (product * c) % self.mod
                    result[param] = product
        return result