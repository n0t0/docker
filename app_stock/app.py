import csv 
import json


def read_portfolio(filename, *, errors='warn'):
    """
    Read a CSV file to compute base pay + overtime pay as a total pay
    """

    portfolio = [] 
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        # headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                print('Row:', rowno, 'Bad row:', row)
                print('Row:', rowno, 'Reason:', err)
                continue 
            record = { 
                'name': row[0],
                'date': row[1],
                'shares': row[2],
                'price': row[3],
            }
            portfolio.append(record)    
    return portfolio

portfolio = read_portfolio('ticker_data.csv')
print(portfolio)

# JSON 
data = json.dumps(portfolio)
port = json.loads(data)

total = sum([holding['shares'] * holding['price'] for holding in portfolio])

# Set comprehension returns only unique names 
names = {holding['name'] for holding in portfolio} 

namestr = ','.join(names)
print(namestr)

# import urllib.request 

# u = urllib.request.urlopen('http://finance.yahoo.com/d/quotes.csv?s={}&f=l1'.format(namestr))
# data = u.read()
# print(data)
# pricedata = data.split()

# for name, price in zip(names, pricedata):
#     print (name, '=', price)

# prices = dict(zip(names, pricedata))
# prices = { name: float(price) for name, price in zip(names, pricedata) }

# current_value = 0.0
# for holding in portfolio:
#     current_value += holding['shares'] * prices[holding['name']]

# currenct_value = sum([ holding['shares'] * prices[holding['name'] for holding in portfolio])

# change = current_value - total