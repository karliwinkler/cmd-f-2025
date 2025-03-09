import requests
import json

def get_total_protein(query):

    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    response = requests.get(api_url + query, headers={'X-Api-Key': 'aWLd0q1XGNvX8Iy3J2kA8A==Yxg2vfvuiOhuTIBI'})
    if response.status_code == requests.codes.ok:
        nutrition_data = response.json()

        total_protein = 0
        
        for item in nutrition_data["items"]:
            total_protein += item['protein_g']
        
        return total_protein

    else:
        print("Error:", response.status_code, response.text)


def get_total_calories(query):

    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    response = requests.get(api_url + query, headers={'X-Api-Key': 'aWLd0q1XGNvX8Iy3J2kA8A==Yxg2vfvuiOhuTIBI'})
    if response.status_code == requests.codes.ok:
        nutrition_data = response.json()

        total_calories = 0
        
        for item in nutrition_data["items"]:
            total_calories += item['calories']
        
        return total_calories

    else:
        print("Error:", response.status_code, response.text)


def get_total_carbs(query):

    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    response = requests.get(api_url + query, headers={'X-Api-Key': 'aWLd0q1XGNvX8Iy3J2kA8A==Yxg2vfvuiOhuTIBI'})
    if response.status_code == requests.codes.ok:
        nutrition_data = response.json()

        total_carbs = 0
        
        for item in nutrition_data["items"]:
            total_carbs += item['carbohydrates_total_g']
        
        return total_carbs

    else:
        print("Error:", response.status_code, response.text)

