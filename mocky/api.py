from mocky import app

import copy
import json
import random

from os import listdir
from os.path import isfile, join

def recommendations():
    recpath = "recommendations"
    recs = [ f for f in listdir(recpath) if isfile(join(recpath, f)) and f[-4:] == ".rec" ]
    recs = [json.load(open(join(recpath, r))) for r in recs]
    recs = filter(lambda x: x.get("display", 0), recs)
    recs = [json.dumps(r) for r in recs]
    return recs
