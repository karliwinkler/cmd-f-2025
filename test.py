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
def print_recipe(recipe_ID):

    #call api with the specific ingredent list 
    api_url = f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={recipe_ID}'
    response = requests.get(api_url)

    if response.status_code == requests.codes.ok:
        meal_data = response.json()
    else:
        print("Error:", response.status_code, response.text)

    # Print the recipe details
    if "meals" in meal_data and len(meal_data["meals"]) > 0:
        meal = meal_data["meals"][0]
        print(f"{meal['strMeal']}")
        print(f"Category: {meal['strCategory']}")
        print(f"Instructions: {meal['strInstructions']}")
        
        # Print ingredients
        print("Ingredients:")
        for i in range(1, 21):  # Maximum of 20 ingredients
            ingredient = meal.get(f"strIngredient{i}", None)
            measurement = meal.get(f"strMeasure{i}", None)
            
            if ingredient and ingredient.strip():  # Check for valid ingredient
                print(f"{measurement if measurement else 'N/A'} {ingredient}")
     
def get_recipes_area(area):
    # call api with the specific area (country)
    api_url = f'https://www.themealdb.com/api/json/v1/1/filter.php?a={area}'
    response = requests.get(api_url)

    if response.status_code == requests.codes.ok:
        meal_data = response.json()
        print(response.json())
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return 


def get_cList():
    #call api for list of places if we need it to populate drop down lists??

    api_url = 'https://www.themealdb.com/api/json/v1/1/list.php?a=list'
    response = requests.get(api_url)

    if response.status_code == requests.codes.ok:
        meal_data = response.json()
    else:
        print("Error:", response.status_code, response.text)

    # Print each ingredient
    if "meals" in meal_data:
        for place in meal_data["meals"]:
            print(place["strArea"])
 
def create_card():
    ID=get_recipe()
    print_recipe(ID)
    T_F = str(input("Do you want this recipe, y/n? "))
    
area = "Canadian"
get_recipes_area(area)



