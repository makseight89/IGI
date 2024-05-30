import requests


def get_random_joke() -> str:
    data = requests.get("https://api.chucknorris.io/jokes/random")
    random_joke = data.json()["value"]
    return random_joke


def get_random_cat_fact() -> str:
    data = requests.get("https://catfact.ninja/fact")
    cat_fact = data.json()["fact"]
    return cat_fact
