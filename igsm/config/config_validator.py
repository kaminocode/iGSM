import os
from typing import Dict

def validate_config(config: Dict) -> Dict:
    validated_config = {}
    
    # Validate knowledge_base_path
    kb_path = config.get('knowledge_base_path', 'igsm/knowledge_base')
    if not os.path.exists(kb_path):
        raise ValueError(f"Knowledge base path does not exist: {kb_path}")
    validated_config['knowledge_base_path'] = kb_path
    
    # Validate structure_layers
    structure_layers = config.get('structure_layers', 4)
    if not isinstance(structure_layers, int) or structure_layers < 1:
        raise ValueError("structure_layers must be a positive integer")
    validated_config['structure_layers'] = structure_layers
    
    # Validate min_items_per_layer and max_items_per_layer
    min_items = config.get('min_items_per_layer', 1)
    max_items = config.get('max_items_per_layer', 3)
    if not isinstance(min_items, int) or min_items < 1:
        raise ValueError("min_items_per_layer must be a positive integer")
    if not isinstance(max_items, int) or max_items < min_items:
        raise ValueError("max_items_per_layer must be an integer greater than or equal to min_items_per_layer")
    validated_config['min_items_per_layer'] = min_items
    validated_config['max_items_per_layer'] = max_items
    
    # Validate max_operations
    max_operations = config.get('max_operations', 15)
    if not isinstance(max_operations, int) or max_operations < 1:
        raise ValueError("max_operations must be a positive integer")
    validated_config['max_operations'] = max_operations
    
    # Validate arithmetic_mod
    arithmetic_mod = config.get('arithmetic_mod', 23)
    if not isinstance(arithmetic_mod, int) or arithmetic_mod < 2:
        raise ValueError("arithmetic_mod must be an integer greater than 1")
    validated_config['arithmetic_mod'] = arithmetic_mod
    
    # Validate min_dependencies and max_dependencies
    min_deps = config.get('min_dependencies', 0)
    max_deps = config.get('max_dependencies', 3)
    if not isinstance(min_deps, int) or min_deps < 0:
        raise ValueError("min_dependencies must be a non-negative integer")
    if not isinstance(max_deps, int) or max_deps < min_deps:
        raise ValueError("max_dependencies must be an integer greater than or equal to min_dependencies")
    validated_config['min_dependencies'] = min_deps
    validated_config['max_dependencies'] = max_deps
    
    # Validate operations
    operations = config.get('operations', ['+', '-', '*'])
    if not isinstance(operations, list) or not all(op in ['+', '-', '*'] for op in operations):
        raise ValueError("operations must be a list containing '+', '-', and/or '*'")
    validated_config['operations'] = operations
    
    # Validate constant_probability
    constant_prob = config.get('constant_probability', 0.2)
    if not isinstance(constant_prob, (int, float)) or not 0 <= constant_prob <= 1:
        raise ValueError("constant_probability must be a float between 0 and 1")
    validated_config['constant_probability'] = constant_prob
    
    # Validate query_type
    query_type = config.get('query_type', 'random')
    if query_type not in ['random', 'leaf', 'root']:
        raise ValueError("query_type must be 'random', 'leaf', or 'root'")
    validated_config['query_type'] = query_type
    
    return validated_config

# Usage example:
# from igsm.config import DEFAULT_CONFIG, validate_config
# user_config = {...}  # User-provided configuration
# merged_config = {**DEFAULT_CONFIG, **user_config}  # Merge with defaults
# validated_config = validate_config(merged_config)