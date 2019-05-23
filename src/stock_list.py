import requests
import json
from model import Stock,DBSession
import GLOBAL

def get_all_stock_list():
    stock_list = []

    for param in GLOBAL.params:
        marked = param["marked"]
        type = param["type"]

        list = get_stock_list(marked, type)
        print("marked:{0},type:{1},count:{2}".format(marked, type, len(list)))
        stock_list.extend(list)

    return stock_list


def get_stock_list(marked, type):
    count = get_stock_count(marked, type)
    url = GLOBAL.stock_list_url.format(count, marked, type)

    response = requests.get(url, headers=GLOBAL.headers)
    data = json.loads(response.content)
    return data["data"]["list"]

def get_stock_count(marked, type):
    url = GLOBAL.stock_list_url.format(0, marked, type)
    response = requests.get(url, headers=GLOBAL.headers)
    data = json.loads(response.content)
    count = data["data"]["count"]
    return count

def save_stock_list(stock_list):
    session = DBSession()

    for stock in stock_list:
        symbol = stock["symbol"]
        name = stock["name"]
        stock_model = Stock(symbol,name)
        session.add(stock_model)

    session.commit()
    session.close()

    return True

if __name__ == "__main__":
    stock_list = get_all_stock_list()
    save_stock_list(stock_list)