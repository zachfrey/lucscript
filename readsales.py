
# Return List of lines in the sales file
#from re import A
import re
import pyparsing


# Read all lines from the sales file
def readsales(fname):
    file = open(fname)
    sales = file.readlines()
    file.close()
    return sales

# Split into individual sales records by comma
def splitsales(line):
    return line.split(",")

# Parse a single sales record into a Dictionary
def parsesale(sale):
    sale_tokens = sale.split()
    # TODO: put into Dictionary
    sale_record = { }
    search_results = re.finditer(r'\<.*?\>', sale)
    sale_record["product"] = next(search_results).group().strip('<>')
    return sale_record