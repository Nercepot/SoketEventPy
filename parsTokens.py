import yaml

def load_tokens_from_yaml(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
        return config.get('tokens', [])
    
