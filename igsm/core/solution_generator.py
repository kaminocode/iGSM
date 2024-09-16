from typing import Dict, List
import string

class SolutionGenerator:
    def __init__(self, config: Dict):
        self.config = config
        self.mod = config.get('arithmetic_mod', 23)

    def generate(self, dependency_graph: Dict[str, Dict]) -> str:
        solution_steps = []
        computed_params = {}
        var_names = iter(string.ascii_lowercase)

        for param in self._topological_sort(dependency_graph):
            step, result = self._generate_step(param, dependency_graph[param], computed_params, var_names)
            solution_steps.append(step)
            computed_params[param] = result

        return "\n".join(solution_steps)

    def _topological_sort(self, graph: Dict[str, Dict]) -> List[str]:
        visited = set()
        result = []

        def dfs(node):
            if node not in visited:
                visited.add(node)
                for dep in graph[node]['dependencies']:
                    dfs(dep)
                result.append(node)

        for node in graph:
            dfs(node)

        return result

    def _generate_step(self, param: str, info: Dict, computed_params: Dict[str, int], var_names: iter) -> tuple:
        category, item = param.split('.')
        var = next(var_names)
        deps = info['dependencies']
        op, constants = info['operation']

        step = f"Define {item} in each {category} as {var}; "

        if op == 'constant':
            result = constants[0]
            step += f"so {var} = {result}."
        else:
            dep_vars = [computed_params[dep] for dep in deps]
            if op == '+':
                result = sum(dep_vars + constants) % self.mod
                step += f"so {var} = {' + '.join(map(str, dep_vars + constants))} = {result}."
            elif op == '-':
                result = (dep_vars[0] - sum(dep_vars[1:] + constants)) % self.mod
                step += f"so {var} = {dep_vars[0]} - ({' + '.join(map(str, dep_vars[1:] + constants))}) = {result}."
            elif op == '*':
                result = 1
                for val in dep_vars + constants:
                    result = (result * val) % self.mod
                step += f"so {var} = {' * '.join(map(str, dep_vars + constants))} = {result}."

        return step, result