#Cryptocurrency simulator
#created by emry Mcgill
#you can purchase or sell Cryptocurrencies in a virtual enviroment
#uses the coinmarketcap API to get information

import requests
import ast

def user_in():
  return input('\nEnter a command(remember to use the quit command to save your data):\n')

def getName(user_input):
  url = 'https://api.coinmarketcap.com/v1/ticker/'+user_input+'/'
  data = requests.get(url)
  data = data.json()
  name = (data[0].get('name'))
  return name

def getPrice(user_input):
  url = 'https://api.coinmarketcap.com/v1/ticker/'+user_input+'/'
  data = requests.get(url)
  data = data.json()
  price = float(data[0].get('price_usd'))
  price = price*1.31
  return price

def listofcurrency():
  print('\nHere are some examples of crytocurrencies you can buy\nbitcoin\nethereum\nripple\nlitecoin\ntether\nlibra\nmonero\neos')

def buy(balence, portfolio):
  valid = False
  while valid!=True:
    valid=True
    try:
      cur = input('Enter the name of the currency you wish to purchase: ')
      getPrice(cur)
    except:
      print('enter a valid currency')
      valid=False

  price = getPrice(cur)
  name = getName(cur)
  totalprice = balence+1

  while (totalprice>balence):
    valid = False
    while valid!=True:
      valid = True
      try:
        amount = int(input(('How many ' + name + ' do you want to buy: ')))
      except:
        print('enter an integer')
        valid = False


    totalprice = amount*price
    if totalprice>balence:
      print('You cannot afford ' + str(amount) + ' ' + name)
  print('Order details:\nNumber of ' + name + ' : ' + str(amount) + '\nTotal price: $' + str(round(totalprice,2)))
  

  confirm = input('Please confirm your order yes (y) no (n): ')
  if confirm == 'y' or confirm == 'yes' or confirm == 'Y':
    balence-=totalprice
    try:
      portfolio['{0}'.format(name.lower())] += amount
    except:
      portfolio['{0}'.format(name.lower())] = amount
    print('Balence: $' + str(round(balence,2)))
  elif confirm == 'n' or confirm == 'no' or confirm == 'N':
    print('Order canceled')
  else:
    print('order was canceled')
  main(balence, portfolio)

def getPortfolio(balence, portfolio):
  vals = [i for i in portfolio.values()]
  labels = [i for i in portfolio.keys()]

  print('\nYour portfolio:\n\nCAD $' + str(round(balence,2)))
  totalvalue = balence
  for i in range (len(vals)):
    print (labels[i], vals[i])
    value = getPrice(labels[i])*vals[i]
    totalvalue += value
    print ('Value: $' + str(round(value,2)))
  print('Total value of portfolio: $' + str(round(totalvalue,2)))
  main(balence, portfolio)
   
def sell(balence, portfolio):
  valid = False
  while valid!=True:
    valid=True
    try:
      cur = input('Enter the name of the currency you wish to sell: ')
      getPrice(cur)
    except:
      print('enter a valid currency')
      valid=False
  
  price = getPrice(cur)
  name = getName(cur)
  amount = portfolio['{0}'.format(name.lower())]+1
  while amount>portfolio['{0}'.format(name.lower())]:
    try:
      amount = int(input(('How many ' + name + ' do you want to sell: ')))
    except:
      print('enter an integer')

  totalprice = amount*price
  print('Order details:\nNumber of ' + name + ' : ' + str(amount) + '\nTotal price: $' + str(round(totalprice,2)))

  confirm = input('Please confirm your order yes (y) no (n): ')
  if confirm == 'y' or confirm == 'yes' or confirm == 'Y':
    balence+=totalprice
    portfolio['{0}'.format(name.lower())] -= amount
    print('Balence: $' + str(round(balence,2)))
  elif confirm == 'n' or confirm == 'no' or confirm == 'N':
    print('Order canceled')
  else:
    print('order was canceled')
  main(balence, portfolio)

def reset():
  writefile=open('data','w').close()
  writefile=open('data','w')
  writefile.write('100000\n{}')
  writefile.close()

def main(balence, portfolio):
  inp = user_in()
  if (inp == 'buy'):
    buy(balence, portfolio)
  if (inp == 'portfolio'):
    getPortfolio(balence, portfolio)
  if (inp == 'get_price'):
    print('$' + str(round(getPrice(input('Enter the currency to check the price: ')),2)))
  if (inp == 'quit'):
    writefile=open("data",'w')
    writefile.write(str(balence)+'\n'+str(portfolio))
    writefile.close()
    quit('Goodbye')
  if (inp == 'sell'):
    sell(balence, portfolio)
  if (inp == 'list'):
    listofcurrency()
  if (inp == 'reset'):
    reset()
  else:
    main(balence, portfolio)


writefile=open("data",'r')
lines = writefile.readlines()
balence = float(lines[0])
portfolio = lines[1]
portfolio = ast.literal_eval(portfolio)
writefile.close()
print(balence, portfolio)

print('Welcome to the Cryptocurrency simulator\nYou get a starting cash balence of $100,000. You can use the following commands\n\nbuy\nsell\nportfolio\nget_price\nlist\nreset\nquit\n')

main(balence, portfolio)


