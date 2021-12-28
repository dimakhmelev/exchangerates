
import argparse
from scrapy import Selector
import requests

parser = argparse.ArgumentParser()
parser.add_argument("teststring", type=str, help="this is a string")
args = parser.parse_args()

def cur(args):
    api_key = "http://api.exchangeratesapi.io/v1/latest?access_key=8530d2f34fc31945387502c95763180e"

    html = requests.get(api_key).content
    sel = Selector(text=html)
    true = 1
    Dict = eval(sel.xpath('//text()').extract_first())
    lis = []
    for currency, value in Dict['rates'].items():
        # Add each name to the names by rank dictionary using rank as the key
        if value < 10:
            lis.append(currency)
    return lis
