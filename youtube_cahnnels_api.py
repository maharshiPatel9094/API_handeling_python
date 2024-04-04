import requests

# def for getting userdata
def youtube_channel_api():
    url = "https://api.freeapi.app/api/v1/public/youtube/channel"
    response = requests.get(url)
    data = response.json()

    if data.get("success", False):
        user_data = data.get("data", {})
        user_info = user_data.get("info", {})
        user_kind = user_info.get("kind", {})
        user_id = user_info.get("id", {})
        return user_kind, user_id

    else:
        raise Exception("unable to fetch data")


def main():
    try:  
        user_kind, user_id = youtube_channel_api()
        print(f"Youtube Info: {user_kind} \n user Id: {user_id}")
    except Exception as e:
        print(str(e))



if __name__ == "__main__":
    main()    