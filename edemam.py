import requests

def search_recipes(ingredient):
    base_url = "https://api.edamam.com/search"
    app_id = "b6d12021"  # Replace with your Edamam App ID
    app_key = "542b9e7cb7215cf3ac84b705d721b9de"  # Replace with your Edamam App Key

    # Define the parameters for the API request
    params = {
        "q": ingredient,
        "app_id": app_id,
        "app_key": app_key,
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # Parse and extract relevant information from the response
        data = response.json()
        recipes = data.get("hits", [])
        return recipes
    else:
        return None

ingredient = "chicken"
recipes = search_recipes(ingredient)

print(recipes)
