import yfinance as yf
stocks = ["RELIANCE.NS","HDFCBANK.NS","INFY.NS","ITC.NS"]
market = "^NSEI"

data = yf.download(stocks, start= "2021-01-01", end= "2026-01-01")
nifty= yf.download(market, start= "2021-01-01", end= "2026-01-01")
print(data.head())
print(nifty.head())

close_prices= data['Close']

returns = close_prices.pct_change()

corr_matrix = returns.corr()
print(corr_matrix)
print(returns.head())
volatility= returns.std()
print(volatility)

annual_volatility= returns.std() * (252**0.5)
print(annual_volatility)
market_close= nifty['Close']
market_returns = market_close.pct_change().dropna()

betas = {}
for stock in returns.columns:
    combined= returns[stock].dropna().to_frame().join(market_returns, how= 'inner')
    combined.columns= ['stock','market']
    cov= combined['stock'].cov(combined['market'])
    var= combined['market'].var()
    beta= cov/var
    betas[stock]= beta
print(betas)

corr_matrix.to_excel("correlation_matrix.xlsx")
annual_volatility.to_excel("annual_volatility.xlsx")

import pandas as pd
betas_df = pd.Series(betas, name= "Beta")
betas_df.to_excel("betas.xlsx")

