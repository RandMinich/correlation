import numpy
import pandas as pd
import pytrends.request as request
import yfinance


def closing_price(ticker):
    Asset = pd.DataFrame(yfinance.download(ticker, period='max')['Adj Close'])
    return numpy.array(Asset)[:, 0]


def trend_request(kw_lists):
    req = request.TrendReq()
    req.build_payload(kw_lists)
    ans = req.interest_over_time().values[:, :-1]
    return ans[:, 0]
