
# Return List of lines in the sales file
from re import A


# Read all lines from the sales file
def readsales(fname):
    file = open(fname)
    sales = file.readlines()
    file.close()
    return sales


def splitsales(line):
    return line.split(",")