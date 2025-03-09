from flask import Flask, render_template, request, redirect, url_for, render_template_string
import test
import random
import nutrition
import bmr

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search_page")
def search_page():
    return render_template("searchPage.htm")


@app.route("/recipes_page")
def recipes_page():
    cuisine = request.args["cuisine"]
    category = request.args["category"]
    ingredient = request.args["ingredient"]

    areaRecipes = test.get_recipes_area(cuisine)
    ingredientRecipes = test.get_recipes_ingredient(ingredient)
    mainsRecipes = test.get_recipes_mains(category)

    chosen_recipes = random.sample(areaRecipes, 8) + random.sample(ingredientRecipes, 8) + random.sample(mainsRecipes, 8)


    return render_template("recipes.html", recipes=chosen_recipes)

@app.route("/recipe/<id>")
def recipe_detail(id):
    recipe = test.get_recipe_ID(id)
    if not recipe:
        return "Recipe not found", 404
    return render_template("recipe_detail.html", recipe=recipe[0])

@app.route("/submit_recipes", methods=["POST"])
def submit_recipes():
    selected_recipes = request.form #["selected_recipes"]  # Get selected checkboxes

    if len(selected_recipes) != 12:
        return render_template_string("""
            <script>
                alert("Error: You must select exactly 12 recipes! You've selected {{sel}}.");
                window.history.back();  // Goes back to the previous page
            </script>
        """, sel=len(selected_recipes))

    return meal_plan_page(selected_recipes)

# redirect(url_for('meal_plan_page', recipes=selected_recipes))


@app.route("/submit_options", methods=['POST'])
def submit_options():
    if request.method == 'POST':
        # Get the selected values from the form
        cuisine = request.form["cuisine"]
        ingredient = request.form["ingredient"]
        category = request.form["category"]

        # Redirect to /results with the selections as URL parameters
        return redirect(url_for('recipes_page', cuisine=cuisine, ingredient=ingredient, category=category))

    return  "Error", 400

@app.route("/meal_plan_page")
def meal_plan_page(selected_recipes):
    selected_dict = selected_recipes.to_dict(flat=False)
    converted_list = [{key: value[0]} for key, value in selected_dict.items()]
    days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    names_list = list(selected_dict.values())
    total_protein =[]
    total_calories=[]
    total_carbs=[]

    for i in range(0,12,2):
        total_protein.append(round(float(nutrition.get_total_protein(names_list[i][0])) + float(nutrition.get_total_protein(names_list[i+1][0])), 2))
        total_calories.append(round(float(nutrition.get_total_calories(names_list[i][0])) + float(nutrition.get_total_calories(names_list[i+1][0])), 2))
        total_carbs.append(round(float(nutrition.get_total_carbs(names_list[i][0])) + float(nutrition.get_total_carbs(names_list[i+1][0])), 2))

    return render_template("meal_plan.html", recipes=converted_list, weekdays=days, protein=total_protein, carbs=total_carbs, calories=total_calories)

@app.route("/submit_nutrition", methods=['POST'])
def submit_nutrition():
    if request.method == 'POST':
        # Get the selected values from the form
        
        age = request.form['age']
        weight = request.form['weight']
        height = request.form['height']
        sex = request.form['sex']

        nutrients = bmr.calculate_bmr(weight, height, age, sex)

        calories = nutrients['calories']
        carbs = nutrients['carbs']
        protein = nutrients['protein']

        print(calories)

        return render_template('meal_plan_submitted_form.html', calories=calories, carbs=carbs, protein=protein)

    return  "Error", 400



if __name__ == "__main__":
    app.run(debug=True)