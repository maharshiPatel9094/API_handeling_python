import requests

def stock_data(symbol):
    # this need to be done in every step
    url = f"https://api.freeapi.app/api/v1/public/stocks/{symbol}"
    response = requests.get(url)
    data = response.json()

    #handeling data  
    if data["success"]:
        stock_data = data["data"]
        return stock_data
    else:
        raise Exception(f"Failed to fetch stock data for symbol {symbol}")

def main():
    try:
        symbol = input("Enter the stock symbol: ")
        stock_info = stock_data(symbol.upper())  # Convert symbol to uppercase
        print("Stock Info:")
        # stck data is in the format of key and value 
        for key, value in stock_info.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()