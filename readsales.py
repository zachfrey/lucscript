
# Return List of lines in the sales file

import re


# Read all lines from the sales file
def read_sales(fname):
    file = open(fname)
    sales = file.readlines()
    file.close()
    return sales


# Split into individual sales records by comma
# NOTE: using split() means we cannot have data files containing ','
#       or input will break. If this is not an acceptible limitation,
#       this function will have to take <> delimiters into account.
def split_sales(line):
    return line.split(",")


# Parse a single sales record into a Dictionary
def parse_sale(sale):
    sale_tokens = sale.split()
    # TODO: nicer error handling
    sale_record = {}
    search_results = re.finditer(r'\<.*?\>', sale)
    sale_record["product"] = next(search_results).group().strip('<>')
    sale_record["price"] = float(next(search_results).group().strip('<>'))
    sale_record["currency"] = next(search_results).group().strip('<>')
    sale_record["email"] = next(search_results).group().strip('<>')
    sale_record["bonus"] = next(search_results).group().strip('<>')
    sale_record["seller"] = []
    for item in search_results:
        sale_record["seller"].append(item.group().strip('<>'))

    return sale_record


def parse_sales_list(sales):
    sales_list = []
    sale_records = split_sales(sales)
    for sale in sale_records:
        sales_list.append(parse_sale(sale))
    return sales_list
