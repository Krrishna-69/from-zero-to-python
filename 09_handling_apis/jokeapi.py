import requests

def fetch_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response = requests.get(url)
    data = response.json()

    if data["success"] and 'data' in data:
        joke_data = data['data']['data']
        cont = joke_data.get("joke_data")
        print("** Random jokes **")
        print(cont)
    else:
        print("failed to fetch jokes: ", data.get("message", "unknown error"))


fetch_jokes()
 
