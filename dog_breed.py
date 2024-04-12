import requests


def dog_breeds():
    # api url
    url = "https://api.freeapi.app/api/v1/public/dogs/124"
    # get the data
    response = requests.get(url)
    # convert data into json 
    data = response.json()
    


# checking if our data got success method 
    if data.get("success"):
        user_data = data.get("data", {})
        dog_id = user_data.get("id", {})
        dog_name = user_data.get("name", {})
        dog_usage = user_data.get("bred_for", {})
        dog_life = user_data.get("life_span", {})
        dog_skills = user_data.get("temperament", {})
        return  dog_name, dog_usage, dog_life, dog_skills

    else:
        raise Exception("Unable to Fetch Data")


def main(): 
    try:
        dog_name, dog_usage, dog_life, dog_skills = dog_breeds()
        print(f"Name of Dog Breed: {dog_name} \nDog Used For: {dog_usage} \nLife span: {dog_life} \nTemperment: {dog_skills}")
    except Exception as e:
        print(str(e))    


if __name__ == "__main__":
    main()