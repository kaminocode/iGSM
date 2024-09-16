import yaml
from pkg_resources import resource_stream, resource_listdir

def load_yaml(resource_path):
    with resource_stream('igsm', resource_path) as stream:
        return yaml.safe_load(stream)

def load_categories():
    categorizations = load_yaml('knowledge_base/categorizations.yaml')
    categories = {}

    for categorization in categorizations['categorizations']:
        for category, file_path in zip(categorization['categories'], categorization['file_paths']):
            category_data = load_yaml(f'knowledge_base/{file_path}')[category]
            default_type = category_data['default_type']
            items = []
            for item in category_data['items']:
                if isinstance(item, dict):
                    item['type'] = item.get('type', default_type)
                    items.append(item)
                else:
                    items.append({'name': item, 'type': default_type})
            categories[category] = items

    return categories