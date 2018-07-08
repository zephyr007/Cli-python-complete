import requests
from terminaltables import DoubleTable
from termcolor import colored
table_data = [
    [colored('Crypto','green'),colored('Symbol','red'), colored('Price :USD','blue'), colored('Circulating Supply', 'yellow'), colored('Total Supply','green'),colored('Market Cap','red'), colored('Percent change hourly','blue'), colored('Percent Change Daily','yellow'), colored('Percent Change week','green')]
]
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

url = 'https://api.coinmarketcap.com/v2/ticker/?limit=10'
res = requests.get(url)
data = res.json()
table = DoubleTable(table_data)
data1 = data['data']
for d in data1:
    rank = data1[d]['rank']
    name = data1[d]['name']
    symbol = data1[d]['symbol']
    price = data1[d]['quotes']['USD']['price']
    circulating_supply = data1[d]['circulating_supply']
    total_supply = data1[d]['total_supply']
    market_cap = data1[d]['quotes']['USD']['market_cap']
    pc1 = str(data1[d]['quotes']['USD']['percent_change_1h']) + '%'
    pc24 = str(data1[d]['quotes']['USD']['percent_change_24h']) + '%'
    pc7d = str(data1[d]['quotes']['USD']['percent_change_7d']) + '%'

    dataStream = [colored(name,'green'),colored(symbol,'red'),colored('$'+ str(price),'blue'),colored(circulating_supply,'yellow'),colored(total_supply,'green'),colored('$'+str(market_cap),'red'),colored(pc1,'blue'),colored(pc24,'yellow'),colored(pc7d,'green')]


    table_data.append(dataStream)
def do_crypto():
    print("\t\t Crypto-currencies")
    print(table.table)
    print()


#k = colored('hello', 'red') + colored('world', 'green')
#print(k)






