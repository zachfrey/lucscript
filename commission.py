from calendar import c
import csv

# Sales type determines commission rate:
#
# N  = No bonus = 5%
# SG = Self generated = 10%
# E  = Eli = 7%

bonus_keys = ["N", "SG", "E"]
bonus_values = [0.05, 0.10, 0.07]
bonus_rates = dict(zip(bonus_keys, bonus_values))


# Read all lines from the sales file
def read_currency_conversion(fname):
    currency_table = dict()
    with open(fname) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            currency_table[row[0]] = row[1]
    return currency_table


# Calculate running commission total with bonus type
#     & currency conversion
# Returns - Dictionary indexed by name with commission total

def calculate_commissions(sales, currencies, sales_types):
    commissions = dict()
    for sale in sales:
        sellers = sale["seller"]
        num_sellers = len(sellers)
        currency = sale["currency"]
        price = sale["price"] / num_sellers
        price2 = price * float(currencies[currency])
        commission = price2 * sales_types[sale["bonus"]]
        for seller in sellers:
            if seller not in commissions:
                commissions[seller] = commission
            else:
                commissions[seller] += commission
    return commissions
