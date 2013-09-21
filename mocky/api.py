from mocky import app

import copy
import json

def generate_recommendations():
    # TODO: FIXME
    with open("mocky/data/square.vega") as spec:
        #square = json.load(spec)
        square = spec.read()
        print square
        return [copy.deepcopy(square)]*12
