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
    
    args = sys.argv[1]
    expressions = args.split(',')
    results = []
    for expr in expressions:
        expr_clean = expr.strip()
        if not expr_clean:
            return
        expr_upper = expr_clean.upper()
        expr_title = expr_clean.title()
        if expr_title in COMPANIES:
            ticker = COMPANIES[expr_title]
            price = STOCKS[ticker]
            results.append(f"{expr_title} stock price is {price}")
        elif expr_upper in STOCKS:
            company_name = None
            for name, ticker in COMPANIES.items():
                if ticker == expr_upper:
                    company_name = name
                    break
            if company_name:
                results.append(f"{expr_upper} is a ticker symbol for {company_name}")
        
        else:
            results.append(f"{expr_clean} is an unknown company or an unknown ticker symbol")

    for result in results:
        print(result)

if __name__ == "__main__":
    main()