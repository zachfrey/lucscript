
# Return List of lines in the sales file

import re


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
    sale_record["product"]  = next(search_results).group().strip('<>')
    sale_record["price"]    = int(next(search_results).group().strip('<>'))
    sale_record["currency"] = next(search_results).group().strip('<>')
    sale_record["email"]    = next(search_results).group().strip('<>')
    sale_record["bonus"]    = next(search_results).group().strip('<>')
    sale_record["seller"]   = []
    for item in search_results:
        sale_record["seller"].append(item.group().strip('<>'))
    
    return sale_record