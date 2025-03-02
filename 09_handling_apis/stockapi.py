import requests
import sys
sys.stdout.reconfigure(encoding="utf-8")

url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
response = requests.get(url)
data = response.json()

def fetch_stock():
        if data["success"] and 'data' in data:
                stock_data = data["data"]
                sname = stock_data['Name']
                mark_cap = stock_data["MarketCap"]
                curr_price = stock_data["CurrentPrice"]

                return sname, mark_cap, curr_price
        else:
                raise Exception("Failed to fetch stock data")
        
def main():
        try:
                sname, mark_cap, curr_price = fetch_stock()
                print(f"Name: {sname}, Marketcap: {mark_cap}, CurrentPrice: {curr_price}")
        except Exception as e:
                print(str(e))

if __name__ == "__main__":
        main()
    