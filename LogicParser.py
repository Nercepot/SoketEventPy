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

def parser_yml_config_promo():
    with open("config.yml", 'r') as file:
        config = yaml.safe_load(file)
        return config.get('promo', [])

def parser_yml_config_twich_price():
    with open("config.yml", 'r') as file:
        config = yaml.safe_load(file)
        return config.get('twich', [])

def parser_yml_config_price():
    with open("config.yml", 'r') as file:
        config = yaml.safe_load(file)
        return config.get('price', [])

def parser_yml_config_price_promo():
    with open("config.yml", 'r') as file:
        config = yaml.safe_load(file)
        return config.get('price_promo', [])

ip = parser_yml_config_ip()
port = parser_yml_config_port()
password = parser_yml_config_password()
promo = parser_yml_config_promo()
twich_price = parser_yml_config_twich_price()
price = parser_yml_config_price()
price_promo = parser_yml_config_price_promo()