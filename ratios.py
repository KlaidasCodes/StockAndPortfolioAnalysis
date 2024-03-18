import numpy as np


def calc_earnings_per_share(net_income, number_of_outstanding_shares):
    earnings_per_share = net_income / number_of_outstanding_shares
    return earnings_per_share


def calc_price_to_earnings_ratio(earnings_per_share, current_stock_price):
    price_to_earnings_ratio = current_stock_price / earnings_per_share
    return price_to_earnings_ratio


def calc_return_on_equity(net_income, shareholders_equity):
    return_on_equity = net_income / shareholders_equity
    return return_on_equity


# def calc_debt_to_equity_ratio(total_debt, shareholders_equity):
#     debt_to_equity_ratio = total_debt / shareholders_equity
#     return debt_to_equity_ratio


# def calc_current_ratio(current_assets, current_liabilities):
#     current_ratio = current_assets / current_liabilities
#     return current_ratio


# def calc_quick_ratio(current_assets, inventory, current_liabilities):
#     quick_ratio = (current_assets - inventory) / current_liabilities
#     return quick_ratio


def calc_dividend_yield(annual_dividends_per_share, current_stock_price):
    dividend_yield = annual_dividends_per_share / current_stock_price
    return dividend_yield


# def calc_book_value_per_share(shareholders_equity, preferred_equity, number_of_outstanding_shares):
#     book_value_per_share = (shareholders_equity - preferred_equity) / number_of_outstanding_shares
#     return book_value_per_share


def calc_price_to_book_ratio(current_stock_price, book_value_per_share):
    price_to_book_ratio = current_stock_price / book_value_per_share
    return price_to_book_ratio


def calc_free_cash_flow(operating_cashflow, capital_expenditures):
    free_cash_flow = operating_cashflow - capital_expenditures
    return free_cash_flow


# def calc_beta(stock_returns=list, market_returns=list):
#     stock_returns_array = np.array(stock_returns)
#     market_returns_array = np.array(market_returns)
#     covariance = np.cov(stock_returns_array, market_returns_array)[0, 1]
#     variance = np.var(market_returns)
#     beta = covariance / variance
#     return beta


def calc_dividend_payout_ratio(dividends_paid, net_income):
    dividend_payout_ratio = dividends_paid / net_income
    return dividend_payout_ratio





