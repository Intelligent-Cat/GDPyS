import json
import os

def open_config():
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
        return config
    except:
        print('Config file was not found or was corrupted, generating new...')
        try:
            with open('config.json', 'x') as config_file:
                config_file.write(r'{}')
            with open('config.json', 'r') as config_file:
                config = json.load(config_file)
        except:
            os.remove('config.json')
            with open('config.json', 'x') as config_file:
                config_file.write(r'{}')
            with open('config.json', 'r') as config_file:
                config = json.load(config_file)
        config['bot-prefix'] = '!'
        config['bot-token'] = ''
        with open('config.json', 'w') as config_file:
            json.dump(config, config_file, indent=4)
        return 0