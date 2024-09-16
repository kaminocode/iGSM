import random
from typing import Dict, List

class ProblemGenerator:
    def __init__(self, config: Dict):
        self.config = config

    def generate(self, dependency_graph: Dict[str, Dict]) -> str:
        statements = []
        for param, info in dependency_graph.items():
            statement = self._generate_statement(param, info)
            statements.append(statement)
        
        random.shuffle(statements)
        problem = " ".join(statements)
        
        query_param = random.choice(list(dependency_graph.keys()))
        query = f"How many {query_param.split('.')[-1]} does {query_param.split('.')[0]} have?"
        
        return f"{problem} {query}"

    def _generate_statement(self, param: str, info: Dict) -> str:
        category, item = param.split('.')
        deps = info['dependencies']
        op, constants = info['operation']
        
        if op == 'constant':
            return f"The number of {item} in each {category} is {constants[0]}."
        
        if len(deps) == 1:
            dep_category, dep_item = deps[0].split('.')
            if op == '+':
                return f"The number of {item} in each {category} is {constants[0]} more than the number of {dep_item} in each {dep_category}."
            elif op == '-':
                return f"The number of {item} in each {category} is {constants[0]} less than the number of {dep_item} in each {dep_category}."
            elif op == '*':
                return f"The number of {item} in each {category} is {constants[0]} times the number of {dep_item} in each {dep_category}."
        
        dep_items = [f"{d.split('.')[-1]} in each {d.split('.')[0]}" for d in deps]
        if op == '+':
            return f"The number of {item} in each {category} is the sum of the number of {', '.join(dep_items[:-1])} and {dep_items[-1]}."
        elif op == '-':
            return f"The number of {item} in each {category} is the difference between the number of {dep_items[0]} and the sum of {', '.join(dep_items[1:])}."
        elif op == '*':
            return f"The number of {item} in each {category} is the product of the number of {' and '.join(dep_items)}."

        return ""  # Default case, should not happen