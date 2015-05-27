import csv, urllib2, os, operator
from pprint import pprint as pp

def read_data(fname):
    my_file = open(fname, "r")
    lines = my_file.read().split("\n\n\n")
    my_file.close()
    formatted = [[l.replace("\n", " ") for l in line.split("\n\n")[1::]] for line in lines]
    form2 = [list(operator.itemgetter(0, 3, -1)(line)) for line in formatted if len(line) > 3]
    with open("neuro_words.csv", "wb") as neuro_words:
        writer = csv.writer(neuro_words)
        header = ['title', 'content', 'pmid']
        writer.writerow(header)
        for row in form2:
            writer.writerow(row)
    return "Write complete"

print read_data("pubmed_result.txt")