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
    
    company_name = sys.argv[1].capitalize()
    
    if company_name in COMPANIES:
        ticker = COMPANIES[company_name]
        stock_price = STOCKS[ticker]
        print(stock_price)
    else:
        print("Unknown company")

if __name__ == "__main__":
    main()