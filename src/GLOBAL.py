stock_list_url = 'https://xueqiu.com/service/v5/stock/screener/quote/list?size={0}&order=desc&orderby=code&order_by=symbol&market={1}&type={2}'
comment_list_url = "https://xueqiu.com/statuses/search.json?count={0}&comment=0&symbol={1}&sort=time"

params = [{"marked": "CN", "type": "sh_sz"}, {"marked": "US", "type": "us"}, {"marked": "HK", "type": "hk"}]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Content-Type": "application/json; charset=utf-8",
    "Referer": "https://xueqiu.com/hq",
    "Host": "xueqiu.com"
}