import requests

# Replace with your Spoonacular API key
api_key = "YOUR.API.KEY"

# Define the Spoonacular API endpoint for complex search
search_endpoint = "API.ENDPOINT.URL"

# Ingredients you want to search for
ingredients = ["beef", "butter", "salt", "pepper", "onions"]

# Prepare the API request for complex search
search_params = {
    "includeIngredients": ",".join(ingredients),
    "apiKey": api_key,
    "number": 10,  # You can adjust the number of results you want to retrieve
}

# Send the API request for complex search
search_response = requests.get(search_endpoint, params=search_params)

# Check if the search request was successful
if search_response.status_code == 200:
    search_data = search_response.json()

    # Extract and print recipes
    for recipe in search_data["results"]:
        title = recipe.get("title", "No Title Available")

        # Retrieve more detailed information for each recipe by its ID
        recipe_id = recipe["id"]
        recipe_endpoint = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
        recipe_params = {"apiKey": api_key}

        # Send the API request for recipe information
        recipe_response = requests.get(recipe_endpoint, params=recipe_params)

        # Check if the request for recipe information was successful
        if recipe_response.status_code == 200:
            recipe_data = recipe_response.json()
            source_url = recipe_data.get("sourceUrl", "No Source URL Available")
            print(f"Recipe: {title}")
            print(f"URL: {source_url}")
            print()
        else:
            print(f"Error fetching recipe information: {recipe_response.status_code}")
else:
    print(f"Error: {search_response.status_code} - {search_response.text}")
