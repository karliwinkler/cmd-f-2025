from flask import Flask, render_template, request, redirect, url_for, render_template_string
import test
import random

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
    dict = selected_recipes.to_dict(flat=False)
    # return dict
    # for s in selected_recipes:
    # print(selected_recipes.items())
    # return selected_recipes
    return render_template("meal_plan.html", recipes=dict)


if __name__ == "__main__":
    app.run(debug=True)
