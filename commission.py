
# Sales type determines commission rate:
#
# N  = No bonus = 5%
# SG = Self generated = 10%
# E  = Eli = 7%

bonus_keys = ["N", "SG", "E"]
bonus_values = [0.05, 0.10, 0.07]
bonus_rates = dict(zip(bonus_keys, bonus_values))

# Given a list of sales, return a Dict of sales amounts
# indexed by salesperson name


# Version 2 - calculate running commission total with bonus type
#             & currency conversion
# Returns - Dictionary indexed by name with commission total

def add_sales2(sales, currencies, sales_types):
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
