import requests

def random_user_api(number):
    if not 1 <= number <= 10:
        raise ValueError("Number must be between 1 and 10")

    # URL of the API with the provided number
    url = f"https://api.freeapi.app/api/v1/public/randomusers?page=1&limit={number}"
    response = requests.get(url)
    print("Response content:", response.content)  # Print the response content
    # convert data to JSON
    data = response.json()

    if data.get("success", False):
        user_data = data.get("data", {})
        user_inner_data = user_data.get("data", {})
        return user_inner_data
    else:
        raise Exception("Unable to fetch the data")

def main():
    try:
        number = int(input("Enter the number of users you want (1-10): "))
        user_inner_data = random_user_api(number)
        print(f"Random User Details: {user_inner_data}")
    except ValueError as ve:
        print(str(ve))
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
