# Module: main.py
# Author: Adam Walls
# Description: 

### local defines and imports
import csv
import sys, os
dir_path = (os.getcwd() + os.path.sep + ".." + os.path.sep + "include")
sys.path.append(dir_path)
from dTree import dTree as dt

#
def parseCsv(csvFile):
    err = 0
    csvArr = list()
    try:
        f = open(csvFile)
        reader = csv.reader(f)
        for row in reader:
            csvArr.append(row)
        return err, csvArr
    except:
        err = 1
        return err, csvArr

# 
def runId3(csvArr, numClasses, maxDepth):
    err = 0
    try:
        d = dt(csvArr, numClasses, maxDepth)
        examples = d.getExamples()
        targetAttrs = d.getTargetAttrs()
        d.runId3(examples, targetAttrs)
        return err, None
    except:
        err = 1
        return err, None

# main entry point to code
def main():
    if len(sys.argv) != 4:
        print("Error: Need a file argument and number of classifications argument.")
        sys.exit(1)
    else:
        print("Processing csv file contents...")

    # Parse file
    err, csvArr = parseCsv(sys.argv[1])
    if err:
        print("Error: File parse error.")
        sys.exit(2)
    else:
        print("Creating decision tree...")

    # runID3 algorithm to determine decision tree
    err, d = runId3(csvArr, sys.argv[2], sys.argv[3])
    if err:
        print("Error: Exception running algorithm.")
        sys.exit(2)

if __name__ == "__main__":
    main()