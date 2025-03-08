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
        ],
        "instructions": [
            "1. Boil a large pot of salted water. Cook the spaghetti noodles according to package instructions.",
            "2. While the pasta is cooking, heat olive oil in a pan over medium heat. Add the garlic and sauté until fragrant.",
            "3. Add the tomato sauce to the pan and bring to a simmer. Season with salt and pepper to taste.",
            "4. Drain the pasta and add it to the sauce. Toss to combine.",
            "5. Serve with fresh basil and grated Parmesan cheese, if desired."
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
        ],
        "instructions": [
            "1. In a large bowl, combine the mixed lettuce, cherry tomatoes, cucumber, and red onion.",
            "2. In a small bowl, whisk together olive oil, balsamic vinegar, salt, and pepper.",
            "3. Pour the dressing over the salad and toss to coat.",
            "4. Top with croutons and feta cheese if desired."
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
        ],
        "instructions": [
            "1. In a large bowl, whisk together flour, sugar, baking powder, baking soda, and salt.",
            "2. In another bowl, whisk together the buttermilk, egg, melted butter, and vanilla extract.",
            "3. Pour the wet ingredients into the dry ingredients and stir until just combined (don't overmix).",
            "4. Heat a griddle or non-stick skillet over medium heat. Lightly grease with butter.",
            "5. Pour 1/4 cup of batter onto the skillet for each pancake. Cook until bubbles form on the surface, then flip and cook until golden brown on the other side.",
            "6. Serve with maple syrup and butter."
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
