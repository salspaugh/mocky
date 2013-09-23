from mocky import app

import copy
import json
import random

def generate_recommendations():
    squares = []
    with open("mocky/data/square.vega") as spec:
        square = json.load(spec)
        for i in range(12):
            s = copy.deepcopy(square)
            s["marks"][0]["properties"]["update"]["fill"]["value"] = random_color()
            s = json.dumps(s)
            squares.append(s)
    return squares

def random_color():
    R = str(hex(random.randint(0, 255))) 
    G = str(hex(random.randint(0, 255)))
    B = str(hex(random.randint(0, 255)))
    color = "".join(['#', R[2:], G[2:], B[2:]])
    return color

