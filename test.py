import requests
import json

def get_recipe():
    # Call API
    api_url = 'https://www.themealdb.com/api/json/v1/1/random.php'
    response = requests.get(api_url)

    #checks for errors 
    if response.status_code == requests.codes.ok:
        meal_data = response.json()
        meal = meal_data["meals"][0]
    else:
        print("Error:", response.status_code, response.text)
        return  # Exit the function if there's an error

    # Accessing ingredients and their measurements
    ingredients = []
    for i in range(1, 21):  # The api has up to 20 ingredients
        ingredient = meal.get(f"strIngredient{i}", None)
        measurement = meal.get(f"strMeasure{i}", None)

        # Check if ingredient is not None and not an empty string
        if ingredient and ingredient.strip(): 
            ingredients.append(f"{ingredient}: {measurement if measurement else 'N/A'}")\
            
    #returns the meal id to be stored to be called again 
    return meal['idMeal']

#prints individual recipes based on recipe ID (currently prints name then Category: Instructions: and Ingredents) 
def get_recipe_ID(recipe_ID):

    #call api with the specific ingredent list 
    api_url = f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={recipe_ID}'
    response = requests.get(api_url)

    if response.status_code == requests.codes.ok:
        meal_data = response.json()

        recipes = []

        for meal in meal_data['meals']:
            recipe = {
                'name': meal['strMeal'],
                'category': meal['strCategory'],
                'image': meal['strMealThumb'],
                'instructions': meal['strInstructions'],
                'ingredients': []
            }

            # Loop through the ingredients (up to 20)
            for i in range(1, 21):
                ingredient = meal.get(f"strIngredient{i}", None)
                measurement = meal.get(f"strMeasure{i}", None)
                
                # Only add valid ingredients (non-empty strings)
                if ingredient and ingredient.strip():
                    ingredient_details = {
                        'ingredient': ingredient,
                        'measurement': measurement if measurement else 'N/A'
                    }
                    recipe['ingredients'].append(ingredient_details)

            # Append the recipe to the recipes list
            recipes.append(recipe)

                    

        return recipes
     
def get_recipes_area(area):
    # call api with the specific area (country)
    api_url = f'https://www.themealdb.com/api/json/v1/1/filter.php?a={area}'
    response = requests.get(api_url)

    if response.status_code == requests.codes.ok:
        meal_data = response.json()

        recipes = []

        # Extract each recipe name and its id
        for meal in meal_data['meals']:
            recipe = {
                'name': meal['strMeal'],
                'id': meal['idMeal'],
                'image': meal['strMealThumb']
            }
            recipes.append(recipe)

        # Return the list of recipes (id and name)
        return recipes

def get_recipes_mains(main):
    # call api with the specific area (country)
    api_url = f'https://www.themealdb.com/api/json/v1/1/filter.php?c={main}'
    response = requests.get(api_url)

    if response.status_code == requests.codes.ok:
        meal_data = response.json()

        recipes = []

        # Extract each recipe name and its id
        for meal in meal_data['meals']:
            recipe = {
                'name': meal['strMeal'],
                'id': meal['idMeal'],
                'image': meal['strMealThumb']
            }
            recipes.append(recipe)

        # Return the list of recipes (id and name)
        return recipes

def get_recipes_ingredient(ingredient):
    # call api with the specific ingredient
    api_url = f'https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}'
    response = requests.get(api_url)

    if response.status_code == requests.codes.ok:
        meal_data = response.json()

        recipes = []

        # Extract each recipe name and its id
        for meal in meal_data['meals']:
            recipe = {
                'name': meal['strMeal'],
                'id': meal['idMeal'],
                'image': meal['strMealThumb']
            }
            recipes.append(recipe)

        # Return the list of recipes (id and name)
        return recipes
