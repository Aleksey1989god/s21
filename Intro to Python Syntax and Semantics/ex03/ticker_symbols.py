import sys

def main():
    if len(sys.argv) != 2:
        return
    
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX', 
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    
    ticker = sys.argv[1].upper()
    
    company_name = None
    for company, company_ticker in COMPANIES.items():
        if company_ticker == ticker:
            company_name = company
    
    
    if ticker in STOCKS:  
        stock_price = STOCKS[ticker]
        company_name = None
        for company, company_ticker in COMPANIES.items():
            if company_ticker == ticker:
                company_name = company

        print(f"{company_name} {stock_price}")
    else:
        print("Unknown company")

if __name__ == "__main__":
    main()