import json
from .models import NAMES
def read_config(path):
    config=json.loads(open(path).read())
    if config['model'] not in NAMES: raise ValueError('Unknown model')
    if not isinstance(config['seed'],int): raise ValueError('Seed must be integer')
    return config
