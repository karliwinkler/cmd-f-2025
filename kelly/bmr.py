def calculate_bmr(weight, height, age, sex):
    
    nutriance = {}
    
    #calculates caloric needs based on sex 
    if sex == "m":
        calories = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        calories = (10 * weight) + (6.25 * height) - (5 * age) - 161
    
    # calculates macronutrients
    carbs = round(0.5 * calories / 4, 1)
    protein = round(0.2 * calories / 4, 1)
    fat = round(0.25 * calories / 9, 1)
    
    # store results 
    nutriance = {
        'calories': round(calories, 1), 
        'carbs': carbs,
        'protein': protein,
        'fat': fat
    }

    return nutriance

print(calculate_bmr(100, 120, 20, "m"))
