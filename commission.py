

# Given a list of sales, return a Dict of sales amounts
# indexed by salesperson name

from locale import currency


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

def total_sales(sales, currency_table):
    totals = dict()

    for seller in sales:
        totals[seller] = float(0.0)
        
        for currency in sales[seller]:
            totals[seller] += float(sales[seller][currency]) * float(currency_table[currency])
    
    return totals