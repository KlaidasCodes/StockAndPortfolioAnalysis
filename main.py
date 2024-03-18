from ratios import *
import requests
import datetime as dt

date_now = str(dt.datetime.now()).split(" ")[0]

API_KEY_POLYGON = "Xa2zsRes3tyPLE0KPdFbV9y3lH20c8m4"
API_KEY_FINNHUB = "cnp3hmhr01qgia587ek0cnp3hmhr01qgia587ekg"
# stock_ticker = input("What stock would you like to analyze?\n")
stock_ticker = "JNJ"

token_header_polygon = {
    "Authorization": f"Bearer {API_KEY_POLYGON}"
}
token_header_finnhub = {
    "X-Finnhub-Token": API_KEY_FINNHUB
}
#
response_polygon = requests.get(url=f"https://api.polygon.io/v2/aggs/ticker/{stock_ticker}/range/1/day/2024-03-12/{date_now}",
                        headers=token_header_polygon)

polygon_data_json = response_polygon.json()
closing_price = polygon_data_json["results"][0]["c"]
print(f"Closing price of {stock_ticker}: {closing_price}")

response_finnhub = requests.get(url=f"https://finnhub.io/api/v1/stock/metric?symbol={stock_ticker}&metric=all",
                                headers=token_header_finnhub).json()
# print(response_finnhub.text)

try:
    book_value_per_share = response_finnhub["metric"]["bookValuePerShareQuarterly"]
    print(f"book_price: {book_value_per_share}")
except KeyError:
    pass

try:
    beta = response_finnhub["metric"]["beta"]
    print(f"beta: {beta}")
except KeyError:
    pass
try:
    current_ratio = response_finnhub["metric"]["currentRatioQuarterly"]
    print(f"current ratio: {current_ratio}")
except KeyError:
    pass
try:
    earnings_per_share = response_finnhub["metric"]["epsTTM"]
    print(f"earnings_per_share: {earnings_per_share}")
except KeyError:
    pass
try:
    pe_ratio = calc_price_to_earnings_ratio(earnings_per_share, closing_price)
    print(f"pe ratio: {pe_ratio}")
except KeyError:
    pass
try:
    quick_ratio = response_finnhub["metric"]["quickRatioQuarterly"]
    print(f"quick ratio: {quick_ratio}")
except KeyError:
    pass
try:
    debt_to_equity_ratio = response_finnhub["metric"]["longTermDebt/equityQuarterly"]
    print(f"debt to equity ratio: {debt_to_equity_ratio}")
except KeyError:
    pass
try:
    price_to_book_ratio = calc_price_to_book_ratio(closing_price, book_value_per_share)
    print(f"price to book ratio: {price_to_book_ratio}")
except KeyError:
    pass
try:
    capital_expenditure_CAGR_5y = response_finnhub["metric"]["capexCagr5Y"]
    print(f"Capex CAGR 5y: {capital_expenditure_CAGR_5y}")
except KeyError:
    pass
try:
    ebitd_per_share_ttm = response_finnhub["metric"]["ebitdPerShareTTM"]
    print(f"ebitd per share ttm: {ebitd_per_share_ttm}")
except KeyError:
    pass
try:
    ebitda_cagr_5y = response_finnhub["metric"]["ebitdaCagr5Y"]
    print(f"ebitda cagr 5y: {ebitda_cagr_5y}")
except KeyError:
    pass
try:
    dividend_growth_rate_5y = response_finnhub["metric"]["dividendGrowthRate5Y"]
    print(f"dividend growth rate 5y: {dividend_growth_rate_5y}")
except KeyError:
    pass
try:
    dividend_per_share = response_finnhub["metric"]["dividendPerShareTTM"]
    print(f"dividends per share: {dividend_per_share}")
except KeyError:
    pass
try:
    earnings_per_share_growth_5y = response_finnhub["metric"]["epsGrowth5Y"]
    print(f"earnings per share growth 5y: {earnings_per_share_growth_5y}")
except KeyError:
    pass
try:
    free_operating_cash_flow_cagr_5y = response_finnhub["metric"]["focfCagr5Y"]
    print(f"free operating cash flow cagr 5y: {free_operating_cash_flow_cagr_5y}")
except KeyError:
    pass
try:
    price_to_free_cash_flow_per_share_ratio = response_finnhub["metric"]["pfcfShareTTM"]
    print(f"price to free cash flow per share ratio: {price_to_free_cash_flow_per_share_ratio}")
except KeyError:
    pass
# still need to get market cap, net income, revenue, stuff like that from financial statements
# in the interface allow for the comparison of different companies. Let's say, up to 5 side by side
# also implement a portfolio backtesting feature. So basically the "user" could investigate the financial data about
# a company, then construct a portfolio and backtest it all in one place.





