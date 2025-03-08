from flask import Flask, render_template

app = Flask(__name__)

# Dummy data simulating backend data
recipes = [
    {
        "title": "Classic Spaghetti",
        "description": "Delicious spaghetti with tomato sauce, garlic, and basil.", 
        "image": "https://www.onceuponachef.com/images/2019/09/Spaghetti-and-Meatballs-1200x1554.jpg",
        "ingredients": [
            "200g spaghetti noodles",
            "1 cup tomato sauce",
            "2 cloves garlic, minced",
            "1 tbsp olive oil",
            "Fresh basil leaves",
            "Salt and pepper to taste",
            "Parmesan cheese (optional)"
        ]
    },
    {
        "title": "Fresh Garden Salad",
        "description": "A refreshing mix of lettuce, tomatoes, cucumbers, and dressing.", 
        "image": "https://thescranline.com/wp-content/uploads/2023/02/GREEN-SALAD-WEB-01.jpg",
        "ingredients": [
            "2 cups mixed lettuce leaves",
            "1/2 cup cherry tomatoes, halved",
            "1/2 cucumber, sliced",
            "1/4 red onion, thinly sliced",
            "2 tbsp olive oil",
            "1 tbsp balsamic vinegar",
            "Salt and pepper to taste",
            "Croutons (optional)",
            "Feta cheese (optional)"
        ]
    },
    {
        "title": "Fluffy Pancakes", 
        "description": "Soft and fluffy pancakes topped with syrup and butter.", 
        "image": "https://www.allrecipes.com/thmb/FE0PiuuR0Uh06uVh1c2AsKjRGbc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/21014-Good-old-Fashioned-Pancakes-mfs_002-0e249c95678f446291ebc9408ae64c05.jpg",
        "ingredients": [
            "1 cup all-purpose flour",
            "2 tbsp sugar",
            "1 tsp baking powder",
            "1/2 tsp baking soda",
            "1/4 tsp salt",
            "3/4 cup buttermilk",
            "1 egg",
            "2 tbsp melted butter",
            "1/2 tsp vanilla extract",
            "Maple syrup and butter for serving"
        ]
    }
]


@app.route("/")
def home():
    return render_template("recipes.html", recipes=recipes)

@app.route("/recipe/<title>")
def recipe_detail(title):
    recipe = get_recipe(title)
    if not recipe:
        return "Recipe not found", 404
    return render_template("recipe_detail.html", recipe=recipe)

def get_recipe(name):
    for r in recipes:
      if (r["title"] == name):
        return r
    return None

if __name__ == "__main__":
    app.run(debug=True)
