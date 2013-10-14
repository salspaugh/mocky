
import json
import sys

def mark_not_removed(recfilename):
    print recfilename
    rec = None
    with open(recfilename) as recfile:
        rec = json.load(recfile)
    rec["display"] = 1
    with open(recfilename, 'w') as recfile:
        json.dump(rec, recfile, indent=4, separators=(',', ': '))

for f in sys.argv[1:]:
    mark_not_removed(f)
