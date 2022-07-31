import yaml
from munch import Munch

def read_yaml(path: str) -> Munch:
    with open(path) as f:
        return Munch.fromDict(yaml.load(f, yaml.SafeLoader))