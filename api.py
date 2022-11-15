import pytrends.request as request


def trend_request(kw_lists):
    req = request.TrendReq()
    req.build_payload(kw_lists)
    ans = req.interest_over_time().values[:, :-1]
    return ans
