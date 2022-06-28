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

    sales_list = []
    for line in sales_file:
        sales_list += parse_sales_list(line)

    # Read currency conversion rates (to $USD)
    currencies = read_currency_conversion(sys.argv[2])

    # Do the math to compute everyone's commissions
    commissions = calculate_commissions(sales_list, currencies, bonus_rates)

    # Print out the results
    for seller in commissions:
        print(f"{seller}\t${round(commissions[seller],2)}")
