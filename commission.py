

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

    ## Ben's sales: 2028 GBP + 49 USD
    #assert sales["Ben"]["GBP"] == 2028
    #assert sales["Ben"]["USD"] == 49

    for seller in sales:
        print("seller: " + seller)
        totals[seller] = float(0.0)
        
        #print(totals)
        for sale in sales[seller]:
            print(sale)
            print(sales[seller][sale])
            #for currency in sale:
                #print(currency)
                #totals[seller] += seller[currency] * currency_table[currency]
    return totals