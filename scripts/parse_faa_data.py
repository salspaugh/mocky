
import csv

def print_column_names(csvfile):
    with open(csvfile) as csvdata:
        reader = csv.reader(csvdata)
        for row in reader:
            for column_name in row:
                print column_name
            return

def transpose_some_rows(csvfile):
    columns = []
    first = True
    count = 0
    with open(csvfile) as csvdata:
        reader = csv.reader(csvdata)
        for row in reader:
            if first:
                for item in row:
                    columns.append([item])
                first = False
                continue
            i = 0
            for item in row:
                columns[i].append(item)
                i += 1
            count += 1
            if count > 2:
                break
    for row in columns:
        print row

def add_id(csvfile):
    count = 0
    with open(csvfile) as csvdata:
        reader = csv.reader(csvdata)
        for row in reader:
            row.insert(0, count)
            print ",".join([str(r) for r in row])
            count += 1

#transpose_some_rows("mocky/data/faa/ontime_performance_2013_1_noheader.csv")
#transpose_some_rows("mocky/data/faa/tmp")
transpose_some_rows("foo")

def loaddb(csvfile):
    with open(csvfile) as csvdata:
        reader = csv.reader(csvdata)
        first = True
        for row in reader:
            if first:
                first = False
                continue
