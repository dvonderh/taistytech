import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def search_recipes(ingredients):
    base_url = "https://api.edamam.com/search"
    app_id = "b6d12021"  # Replace with your Edamam App ID
    app_key = "542b9e7cb7215cf3ac84b705d721b9de"  # Replace with your Edamam App Key

    # Define the parameters for the API request
    params = {
        "q": ",".join(ingredients),
        "app_id": app_id,
        "app_key": app_key,
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # Parse and extract relevant information from the response
        data = response.json()
        hits = data.get("hits", [])

        # Extract recipe labels and ingredients
        recipe_labels = [hit['recipe']['label'] for hit in hits]
        recipe_ingredients = [" ".join(hit['recipe']['ingredientLines']) for hit in hits]

        # Use TF-IDF vectorizer to convert text data into vectors
        vectorizer = TfidfVectorizer(stop_words='english')
        vectors = vectorizer.fit_transform(recipe_ingredients)

        # Calculate cosine similarity between ingredient vectors
        cosine_similarities = linear_kernel(vectors, vectors)

        # Get indices of recipes similar to the user's ingredients
        similar_indices = cosine_similarities[-1].argsort()[:-6:-1]

        # Get recommended recipes
        recommended_recipes = [{'label': recipe_labels[idx], 'url': hits[idx]['recipe']['url']} for idx in similar_indices if idx != len(hits) - 1]
            
        return recommended_recipes

    else:
        return None

ingredient = ["chicken", "salt", "butter"]
recipes = search_recipes(ingredient)
for i in recipes:
    print(i)

