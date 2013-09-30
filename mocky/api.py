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

def recommendations_with_these_fields(rec):
    recpath = "recommendations"
    target = rec["columns"]
    recs = [ f for f in listdir(recpath) if isfile(join(recpath, f)) and f[-4:] == ".rec" ]
    ret = []
    recs = [json.load(open(join(recpath, r))) for r in recs]
    for r in recs:
        for column in r["columns"]:
            if column in target:
                ret.append(r)
    ret = [json.dumps(r) for r in ret]
    return ret

def recommendations_with_these_marks(rec):
    recpath = "recommendations"
    target = get_marks(rec)
    recs = [ f for f in listdir(recpath) if isfile(join(recpath, f)) and f[-4:] == ".rec" ]
    ret = []
    recs = [json.load(open(join(recpath, r))) for r in recs]
    for r in recs:
        for mark in get_marks(r):
            if mark in target:
                ret.append(r)
    ret = [json.dumps(r) for r in ret]
    return ret

def get_marks(rec):
    marks = rec["vega"]["marks"]
    marks = [m["type"] for m in marks]
    return marks
    # TODO: check group marks too
