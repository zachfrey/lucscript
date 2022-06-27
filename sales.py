#!/usr/bin/python3

import sys
import os

from readsales import *
from commission import *

if __name__ == "__main__":
    print(f"Argument count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"argument {i:>6}: {arg}")
    if len(sys.argv) < 3:
        print(f"usage: {sys.argv[0]} salesdata.csv currency.csv")
        sys.exit(os.EX_USAGE)
    sales = read_sales(sys.argv[1])
    #print(sales)

    sales_list = parse_sales_list(sales)

    # TODO: read currency conversion
    currency_table_keys = ["USD", "GBP"]
    currency_table_values = [1.0, 1.22]
    test_currency_table = dict(zip(currency_table_keys, currency_table_values))

    commissions = calculate_commissions(sales_list, test_currency_table, bonus_rates)

    print(commissions)
