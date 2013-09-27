from mocky import app

import copy
import json
import random

from os import listdir
from os.path import isfile, join

def recommendations():
    recpath = "recommendations"
    recs = [ f for f in listdir(recpath) if isfile(join(recpath, f)) and f[-4:] == "vega" ]
    recs = [json.dumps(json.load(open(join(recpath, r)))) for r in recs]
    return recs
