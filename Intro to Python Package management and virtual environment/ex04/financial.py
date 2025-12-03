#!/usr/bin/env python3

import sys
import time
import requests
from bs4 import BeautifulSoup


def get_financial_data(ticker, field):

    ticker = ticker.upper()
    url = f"https://finance.yahoo.com/quote/{ticker}/financials/?p={ticker}"

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 YaBrowser/25.8.0.0 Safari/537.36",
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to load page: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    return extract_data_from_html(soup, field)


def extract_data_from_html(soup, field):

    matches = soup.find_all(string=field)

    if not matches:
        raise Exception("Field not found")

    target_elem = matches[0]
    parent = target_elem.parent

    row_container = parent
    max_depth = 5
    depth = 0
    while row_container and depth < max_depth:
        siblings = row_container.find_all(string=True)

        texts = []
        for s in siblings:
            stripped = s.strip()
            if stripped and stripped != field:
                texts.append(stripped)

        numbers = []
        for t in texts:
            clean = t.replace(',', '').replace('.', '')
            if clean.isdigit():
                numbers.append(t)

        if numbers:
            result = (field,) + tuple(numbers)
            # time.sleep(5)
            return result

        row_container = row_container.parent
        depth += 1

    raise Exception("Field not found or no data available")


def validate_input(ticker, field):

    if not ticker or not isinstance(ticker, str):
        raise ValueError("Ticker must be a non-empty string")
    if not field or not isinstance(field, str):
        raise ValueError("Field must be a non-empty string")


def main():
    if len(sys.argv) != 3:
        raise Exception("Usage: ./financial.py <ticker> <field>")

    ticker = sys.argv[1]
    field = sys.argv[2]

    validate_input(ticker, field)
    result = get_financial_data(ticker, field)
    print(result)


if __name__ == "__main__":
    main()