from mocky import app

import copy
import json
import random

NUM_RECOMMENDATIONS = 12

def recommendations(color=(0, 255, 0, 255, 0, 255)):
    squares = []
    with open("mocky/data/bar.vega") as spec:
        square = json.load(spec)
        for i in range(NUM_RECOMMENDATIONS):
            s = copy.deepcopy(square)
            s["marks"][0]["properties"]["update"]["fill"]["value"] = random_color(*color)
            s = json.dumps(s)
            squares.append(s)
    return squares

def random_color(ra, rb, ga, gb, ba, bb):
    R = str(hex(random.randint(ra, rb))) 
    G = str(hex(random.randint(ga, gb)))
    B = str(hex(random.randint(ba, bb)))
    color = "".join(['#', R[2:], G[2:], B[2:]])
    return color

def get_nearby_range(hex_color):
    R = int(hex_color[1:3], 16)
    G = int(hex_color[3:5], 16)
    B = int(hex_color[5:], 16)
    ra = max(0, R-25)
    rb = min(255, R+25)
    ga = max(0, G-25)
    gb = min(255, G+25)
    ba = max(0, B-25)
    bb = min(255, B+25)
    return (ra, rb, ga, gb, ba, bb)

def recommendations_like_this(vega_spec):
    s = json.loads(vega_spec)
    print type(s)
    print s
    color = s["marks"][0]["properties"]["update"]["fill"]["value"]
    return recommendations(get_nearby_range(color))
