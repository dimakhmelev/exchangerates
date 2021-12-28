
import pytest
import argparse
from untitled import cur

parser = argparse.ArgumentParser()
parser.add_argument("teststring", type=str, help="this is a string")
args = parser.parse_args()
args = '8530d2f34fc31945387502c95763180e'

def test_on_string():
  assert cur(args)[0] == 'AED'
    
def test_on_list():
  assert cur(args) == ['AED', 'ANG', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BGN',
                       'BHD', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BYN',
                       'BZD', 'CAD', 'CHF', 'CLF', 'CNY', 'CUC', 'DKK', 'EUR',
                       'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GTQ',
                       'HKD', 'HRK', 'ILS', 'IMP', 'JEP', 'JOD', 'KWD', 'KYD',
                       'LTL', 'LVL', 'LYD', 'MOP', 'MYR', 'NOK', 'NZD', 'OMR',
                       'PAB', 'PEN', 'PGK', 'PLN', 'QAR', 'RON', 'SAR', 'SBD',
                       'SGD', 'SHP', 'SVC', 'TMT', 'TND', 'TOP', 'TTD', 'USD',
                       'WST', 'XAG', 'XAU', 'XCD', 'XDR']
