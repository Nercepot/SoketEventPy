import yaml

def parser_yml_config_ip():
    with open("config.yml", 'r') as file:
        config = yaml.safe_load(file)
        return config.get('ip', [])

def parser_yml_config_port():
    with open("config.yml", 'r') as file:
        config = yaml.safe_load(file)
        return config.get('port', [])

def parser_yml_config_password():
    with open("config.yml", 'r') as file:
        config = yaml.safe_load(file)
        return config.get('password', [])

ip = parser_yml_config_ip()
port = parser_yml_config_port()
password = parser_yml_config_password()


