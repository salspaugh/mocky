
import csv
import json
import sys

def csv_to_dicts(csvfile):
    data = []
    with open(csvfile) as csvdata:
        reader = csv.reader(csvdata)
        header = True
        for row in reader:
            if header:
                attributes = [r.replace("(", "").replace(")", "") for r in row]
                header = False
                continue
            item = {}
            for i in range(len(row)):
                item[attributes[i]] = row[i]
            data.append(item)
    print json.dumps(data)

if __name__ == "__main__":
    csv_to_dicts(sys.argv[1])
