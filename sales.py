#!/usr/bin/python3

import sys
import os

from readsales import *
from commission import *

import sales_testdata

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"usage: {sys.argv[0]} salesdata.csv currency.csv")
        sys.exit(os.EX_USAGE)
    sales_file = read_sales(sys.argv[1])

    sales_list = parse_sales_list(sales_file[0])

    # TODO: read currency conversion

    commissions = calculate_commissions(sales_list, sales_testdata.test_currency_table, bonus_rates)

    print(commissions)
