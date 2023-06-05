import json
import os

# Look relative to the location of this module file
DATA_FILEPATH = os.path.join(os.path.dirname(__file__), './data/startlists.json')


def load_race_data() -> dict:
    with open(DATA_FILEPATH, 'r') as jsonfile:
        as_json = json.load(jsonfile)
    return as_json


