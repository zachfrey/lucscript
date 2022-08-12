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
def parse_sale(sale, line_num):

    # TODO: nicer error handling
    sale_record = {}
    search_results = re.finditer(r'\<.*?\>', sale)
    sale_record["line_number"] = line_num
    sale_record["product"] = next(search_results).group().strip('<>')
    sale_record["price"] = float(next(search_results).group().strip('<>'))
    sale_record["currency"] = next(search_results).group().strip('<>')
    sale_record["email"] = next(search_results).group().strip('<>')
    sale_record["seller"] = []
    while True:
        try:
            seller = {}
            seller["bonus"] = next(search_results).group().strip('<>')
            seller["name"] = next(search_results).group().strip('<>').strip()
            sale_record["seller"].append(seller)
        except StopIteration:
            break

    return sale_record


def parse_sales_list(sales, line_num):
    sales_list = []
    sale_records = split_sales(sales)

    for sale in sale_records:
        sale_tokens = sale.strip().split()
        if len(sale_tokens) == 0:
            # blank line, skip
            continue
        sales_list.append(parse_sale(sale, line_num))
    return sales_list
