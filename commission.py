


bonus_keys = ["N", "SG", "E"]
bonus_values = [0.05, 0.10, 0.07]
bonus_rates = dict(zip(bonus_keys, bonus_values))

# Given a list of sales, return a Dict of sales amounts
# indexed by salesperson name

def add_sales(sales):
    sales_by_person = dict()
    for sale in sales:
        sellers = sale["seller"]
        num_sellers = len(sellers)
        currency = sale["currency"]
        price = sale["price"] / num_sellers
        for seller in sellers:
            if seller not in sales_by_person:
                sales_by_person[seller] = dict()
                sales_by_person[seller][currency] = 0
            if currency not in sales_by_person[seller]:
                sales_by_person[seller][currency] = 0
            sales_by_person[seller][currency] += price
    return sales_by_person

# Version 2 - calculate running commission total with bonus type & currency conversion
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

# Total sales with conversion to base currency (USD)

def total_sales(sales, currency_table):
    totals = dict()

    for seller in sales:
        totals[seller] = float(0.0)
        
        for currency in sales[seller]:
            totals[seller] += float(sales[seller][currency]) * float(currency_table[currency])
    
    return totals

def calculate_commissions(sales, commission_rates):
    commissions = dict()
    for seller in sales:
        commissions[seller] = float(sales[seller]) * float(commission_rates[seller])
    return commissions