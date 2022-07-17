#!/usr/bin/python3 -B

import sys
import os

from readsales import *
from commission import *

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"usage: {sys.argv[0]} salesdata.csv currency.csv output.csv")
        sys.exit(os.EX_USAGE)
    sales_file = read_sales(sys.argv[1])

    sales_list = []
    for line in sales_file:
        sales_list += parse_sales_list(line)

    # Read currency conversion rates (to $USD)
    currencies = read_currency_conversion(sys.argv[2])

    # Do the math to compute everyone's commissions
    commissions = calculate_commissions2(sales_list, currencies, bonus_rates)

    # Write out the results

    # Seller,Product,Price,Currency,Customer,Bonus,Splits,Conversion,Commission
    fields = ['Seller', 'Product', 'Price', 'Currency',
              'Customer', 'Bonus', 'Splits', 'Conversion', 'Commission']
    filename = sys.argv[3]

    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(commissions)

    # Print summary for crosscheck
    total_sales = dict()
    for sale in commissions:
        if sale["Seller"] not in total_sales:
            total_sales[sale["Seller"]] = sale["Commission"]
        else:
            total_sales[sale["Seller"]] += sale["Commission"]
    for seller in total_sales:
        print(f"{seller}\t${round(total_sales[seller],2)}")
