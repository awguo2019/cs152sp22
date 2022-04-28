import glob
import csv

# for our purposes, 0 refers to a human creator and 1 refers to an AI creator
header = ['creator', 'poem']

with open("input/train.csv", 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    # for human generated poems
    for filename in glob.glob('../free-verse/*.txt'):
        if filename == "all_poems.txt":
            # don't want to copy this file into csv.
            continue
        with open(filename, 'r') as readfile:
            textdata = readfile.read()
            row = ['0', textdata]
            writer.writerow(row)

    # for ai-generated poems
    for filename in glob.glob('../ai-poems/*.txt'):
        with open(filename, 'r') as readfile:
            textdata = readfile.read()
            row = ['0', textdata]
            writer.writerow(row)

with open("input/test.csv", 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    # for human generated poems
    for filename in glob.glob('../free-verse-testing-human/*.txt'):
        with open(filename, 'r') as readfile:
            textdata = readfile.read()
            row = ['0', textdata]
            writer.writerow(row)

    # for ai-generated poems
    for filename in glob.glob('../free-verse-testing-ai/*.txt'):
        with open(filename, 'r') as readfile:
            textdata = readfile.read()
            row = ['0', textdata]
            writer.writerow(row)
