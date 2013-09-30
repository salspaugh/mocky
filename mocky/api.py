from mocky import app

import copy
import json
import random

from os import listdir
from os.path import isfile, join

def remove_recommendation(rec):
    f = lookup_file(rec)
    mark_removed(f)

def lookup_file(rec): # This seems jank.
    rec = json.loads(rec)
    return rec["filename"]

def mark_removed(recfilename):
    rec = None
    with open(recfilename) as recfile:
        rec = json.load(recfile)
    rec["display"] = 0
    with open(recfilename, 'w') as recfile:
        json.dump(rec, recfile)

def recommendations():
    recpath = "recommendations"
    recs = [ f for f in listdir(recpath) if isfile(join(recpath, f)) and f[-4:] == ".rec" ]
    recs = [json.load(open(join(recpath, r))) for r in recs]
    recs = filter(lambda x: x.get("display", 0), recs)
    recs = [json.dumps(r) for r in recs]
    return recs
