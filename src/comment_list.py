import requests
import json
import http.cookiejar as cookilib
from model import Stock,Comment,DBSession
import GLOBAL

sess = requests.session()
sess.cookies = cookilib.LWPCookieJar("xqcomment.txt")

def get_stock_list_from_db():
    session = DBSession()
    stock_list = session.query(Stock).all()
    session.close()
    return stock_list

def get_and_save_comment_list(stock_list):
    for stock in stock_list:
        symbol = stock.symbol

        list = get_comment_list(symbol)
        save_comment_list(symbol,list)

def get_comment_list(symbol):
    count = get_comment_count(symbol)
    url = GLOBAL.comment_list_url.format(count,symbol)
    response = sess.get(url, headers=GLOBAL.headers)

    data = json.loads(response.content)
    return data["list"]

def get_comment_count(symbol):
    url = GLOBAL.comment_list_url.format(1, symbol)
    response = sess.get(url, headers=GLOBAL.headers)
    data = json.loads(response.content)
    count = data["count"]
    return count

def save_comment_list(symbol,comment_list):
    session = DBSession()

    for comment in comment_list:
        id = comment["id"]
        title = comment["title"]
        text = comment["text"]
        description = comment["description"]
        comment_model = Comment(id,symbol,title,text,description)
        session.add(comment_model)

    session.commit()
    session.close()

    return True

if __name__ == "__main__":
    sess.get("https://xueqiu.com/hq",headers=GLOBAL.headers)
    sess.cookies.save()

    stock_list = get_stock_list_from_db()
    get_and_save_comment_list(stock_list)
    # sess.get('https://xueqiu.com/statuses/search.json?count=1&comment=0&symbol=00001&sort=time',headers=GLOBAL.headers)
    # list = get_comment_list("00001")
    # save_comment_list("00001", list)