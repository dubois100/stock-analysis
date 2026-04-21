# stock-analysis
Built a stock risk analysis project using Python for data analysis and Power BI for visualization of volatility, beta, and correlation.
#  Stock Risk Analysis Dashboard

##  Overview

This project analyzes the risk profile of selected stocks using key financial metrics such as **volatility**, **beta**, and **correlation**.
Data processing was performed using Python, and the dashboard was built in Power BI for visualization.

---

##  Tools & Technologies

* Python (pandas, numpy, yfinance)
* Power BI
* Excel

---

##  Key Insights

* **INFY.NS** shows the highest volatility (~0.24), indicating higher price fluctuations
* **ITC.NS** has the lowest volatility (~0.20), making it relatively stable
* **RELIANCE.NS** (≈1.12) and **HDFCBANK.NS** (≈1.05) have higher market sensitivity (beta > 1)
* Correlations between stocks are positive, with the highest between HDFC Bank and Reliance (~0.36)
* Moderate correlations suggest **limited diversification benefits**

---

##  Dashboard Preview

<img width="1285" height="720" alt="stockdashboard" src="https://github.com/user-attachments/assets/f22ba182-534c-43cf-ba8f-0e7b582d5c77" />


---

## Project Structure

```
stock-risk-analysis/
├── dashboard/
│   └── dashboard_preview.png
├── data/
│   ├── volatility.xlsx
│   ├── beta.xlsx
│   └── correlation_matrix.xlsx
├── src/
│   └── stock.py
└── README.md
```

---

## How to Use

1. Download the repository
2. Open the Power BI file (.pbix) *(to be added)*
3. Explore the dashboard and insights

---

## Notes

* This project focuses on basic risk metrics and exploratory analysis
* Future improvements may include portfolio optimization and Value at Risk (VaR)

---

##  Author
dubois100

