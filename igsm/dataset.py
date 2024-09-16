from typing import List, Dict
from igsm.core.structure_graph import StructureGraph
from igsm.core.dependency_graph import DependencyGraph
from igsm.core.problem_generator import ProblemGenerator
from igsm.core.solution_generator import SolutionGenerator
from igsm.config.default_config import DEFAULT_CONFIG

class Problem:
    def __init__(self, statement: str, solution: str):
        self.statement = statement
        self.solution = solution

class igsmDataset:
    def __init__(self, config: Dict = None):
        self.config = config or DEFAULT_CONFIG
        self.structure_graph = StructureGraph(self.config)
        self.dependency_graph = DependencyGraph(self.config)
        self.problem_generator = ProblemGenerator(self.config)
        self.solution_generator = SolutionGenerator(self.config)

    def generate(self, num_problems: int) -> List[Problem]:
        problems = []
        for _ in range(num_problems):
            structure = self.structure_graph.generate()
            dependency = self.dependency_graph.generate(structure)
            statement = self.problem_generator.generate(dependency)
            solution = self.solution_generator.generate(dependency)
            problems.append(Problem(statement, solution))
        return problems