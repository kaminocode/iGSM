import random
from typing import Dict, List
from igsm.utils.yaml_loader import load_categories

class StructureGraph:
    def __init__(self, config: Dict):
        self.config = config
        self.categories = self._load_categories()

    def _load_categories(self) -> Dict[str, List[Dict]]:
        return load_categories() 

    def generate(self) -> Dict:
        layers = self.config.get("structure_layers", 4)
        min_items = self.config.get("min_items_per_layer", 1)
        max_items = self.config.get("max_items_per_layer", 3)
        
        structure = {}
        category_names = list(self.categories.keys())
        
        for i in range(min(layers, len(category_names))):
            category = category_names[i]
            num_items = random.randint(min_items, min(max_items, len(self.categories[category])))
            items = random.sample(self.categories[category], num_items)
            structure[category] = items
            
        return structure

    def get_item_by_type(self, category: str, item_type: str) -> Dict:
        matching_items = [item for item in self.categories[category] if item['type'] == item_type]
        return random.choice(matching_items) if matching_items else None

    def get_random_item(self, category: str) -> Dict:
        return random.choice(self.categories[category])

    def get_all_items(self, category: str) -> List[Dict]:
        return self.categories[category]

    def get_item_types(self, category: str) -> List[str]:
        return list(set(item['type'] for item in self.categories[category]))