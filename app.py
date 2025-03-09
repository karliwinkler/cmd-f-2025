from flask import Flask, render_template, request, redirect, url_for
from test import get_recipes_area, get_recipes_ingredient, get_recipes_mains


app = Flask(__name__)


@app.route("submit_options", methods=['GET', 'POST'])
def submit_options():
    if request.method == 'POST':
        # Get the selected values from the form
        cuisine = request.form.get('cuisine')
        ingredient = request.form.get('ingredient')
        category = request.form.get('category')

        print(cuisine)
        print(ingredent)
        print(category)

        # Redirect to /results with the selections as URL parameters
        return redirect(url_for('recipes', cuisine=cuisine, ingredient=ingredient, category=category))

    return render_template("searchPage.htm")

@app.route('/recipes')
def recipes():
    # Get the selections from the URL parameters
    cuisine = request.args.get('cuisine')
    ingredient = request.args.get('ingredient')
    category = request.args.get('category')

    # Get the recipes based on the selections
    areaRecipes = get_recipes_area(cuisine)
    ingredientRecipes = get_recipes_ingredient(ingredient)
    mainsRecipes = get_recipes_mains(category)


    return render_template('recipes.html', areaRecipes=areaRecipes, ingredientRecipes=ingredientRecipes, mainsRecipes=mainsRecipes)


if __name__ == '__main__':
    app.run(debug=True)
