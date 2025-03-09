from flask import Flask, render_template

app = Flask(__name__)

# Dummy data simulating backend data
recipes = [
    {
        "title": "Classic Spaghetti",
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
    },
    {
        "title": "Chicken Caesar Salad",
        "image": "https://s23209.pcdn.co/wp-content/uploads/2023/01/220905_DD_Chx-Caesar-Salad_051-500x500.jpg",
        "ingredients": [
            "2 cups romaine lettuce, chopped",
            "1 chicken breast, grilled and sliced",
            "1/2 cup croutons",
            "1/4 cup Caesar dressing",
            "Parmesan cheese, shredded"
        ],
        "instructions": [
            "1. Toss the lettuce and croutons in a large bowl.",
            "2. Add the grilled chicken slices on top.",
            "3. Drizzle Caesar dressing over the salad and toss to coat.",
            "4. Top with Parmesan cheese and serve."
        ]
    },
    {
        "title": "Vegetable Stir-Fry",
        "image": "https://kristineskitchenblog.com/wp-content/uploads/2024/01/vegetable-stir-fry-22-3.jpg",
        "ingredients": [
            "1 tbsp olive oil",
            "1 onion, sliced",
            "1 bell pepper, sliced",
            "1 zucchini, sliced",
            "1 cup broccoli florets",
            "2 tbsp soy sauce",
            "1 tsp sesame oil"
        ],
        "instructions": [
            "1. Heat olive oil in a pan over medium heat.",
            "2. Add the onion, bell pepper, zucchini, and broccoli. Stir-fry for 5-7 minutes.",
            "3. Add soy sauce and sesame oil and stir to combine.",
            "4. Serve hot."
        ]
    },
    {
        "title": "Beef Tacos",
        "image": "https://thegirlonbloor.com/wp-content/uploads/2022/10/Crockpot-beef-tacos-8.jpg",
        "ingredients": [
            "1 lb ground beef",
            "1 packet taco seasoning",
            "8 taco shells",
            "Lettuce, shredded",
            "Tomato, diced",
            "Cheese, shredded"
        ],
        "instructions": [
            "1. Cook the ground beef in a pan over medium heat until browned.",
            "2. Add the taco seasoning and water as directed on the packet.",
            "3. Fill taco shells with beef mixture and top with lettuce, tomato, and cheese."
        ]
    },
    {
        "title": "Eggplant Parmesan",
        "image": "https://www.honeywhatscooking.com/wp-content/uploads/2020/11/Baked-Eggplant-Parmesan30.jpg",
        "ingredients": [
            "2 eggplants, sliced",
            "1 cup breadcrumbs",
            "1 cup marinara sauce",
            "1/2 cup mozzarella cheese",
            "1/4 cup Parmesan cheese"
        ],
        "instructions": [
            "1. Preheat oven to 375°F (190°C).",
            "2. Dip eggplant slices in breadcrumbs and bake on a sheet for 20 minutes.",
            "3. Layer eggplant slices with marinara sauce and cheese. Bake for an additional 10 minutes."
        ]
    },
    {
        "title": "Grilled Cheese Sandwich",
        "image": "https://www.jocooks.com/wp-content/uploads/2024/01/grilled-cheese-1-9-500x500.jpg",
        "ingredients": [
            "2 slices bread",
            "2 slices cheddar cheese",
            "Butter"
        ],
        "instructions": [
            "1. Butter one side of each slice of bread.",
            "2. Place cheese between the slices of bread, butter side out.",
            "3. Grill on medium heat until golden brown on both sides."
        ]
    },
    {
        "title": "Chocolate Chip Cookies",
        "image": "https://cdn.loveandlemons.com/wp-content/uploads/2024/08/chocolate-chip-cookie-recipe.jpg",
        "ingredients": [
            "1 cup butter",
            "1 cup sugar",
            "2 cups flour",
            "1 tsp vanilla extract",
            "1 cup chocolate chips",
            "1 egg"
        ],
        "instructions": [
            "1. Preheat oven to 350°F (175°C).",
            "2. Mix butter, sugar, flour, vanilla, and egg.",
            "3. Stir in chocolate chips.",
            "4. Drop spoonfuls of dough onto a baking sheet.",
            "5. Bake for 10 minutes."
        ]
    },
    {
        "title": "Chicken Alfredo",
        "image": "https://gimmedelicious.com/wp-content/uploads/2024/10/Skinny-Chicken-Broccoli-Alfredo-1.jpg",
        "ingredients": [
            "1 lb fettuccine pasta",
            "1 lb chicken breast, cooked and sliced",
            "1 cup heavy cream",
            "1/2 cup Parmesan cheese",
            "2 cloves garlic, minced"
        ],
        "instructions": [
            "1. Cook pasta according to package instructions.",
            "2. In a separate pan, sauté garlic in butter.",
            "3. Add heavy cream and bring to a simmer.",
            "4. Stir in Parmesan and chicken.",
            "5. Toss with cooked pasta."
        ]
    },
    {
        "title": "Fruit Smoothie",
        "image": "https://www.dinneratthezoo.com/wp-content/uploads/2018/05/frozen-fruit-smoothie-3.jpg",
        "ingredients": [
            "1 banana",
            "1/2 cup strawberries",
            "1/2 cup yogurt",
            "1 cup milk"
        ],
        "instructions": [
            "1. Blend all ingredients until smooth.",
            "2. Serve immediately."
        ]
    },
    {
        "title": "Lemon Chicken",
        "image": "https://cdn.apartmenttherapy.info/image/upload/f_jpg,q_auto:eco,c_fill,g_auto,w_1500,ar_1:1/at%2Farchive%2F6c6cebd013fd68fe8699157859b61918353479d4",
        "ingredients": [
            "4 chicken breasts",
            "1 lemon, sliced",
            "2 tbsp olive oil",
            "1 tbsp honey",
            "1 tsp thyme"
        ],
        "instructions": [
            "1. Preheat oven to 375°F (190°C).",
            "2. Drizzle chicken with olive oil and honey.",
            "3. Top with lemon slices and thyme.",
            "4. Bake for 25-30 minutes."
        ]
    },
    {
        "title": "Pork Stir-Fry",
        "image": "https://www.allrecipes.com/thmb/teG7lERARphCsU61rV3sbhPqiFM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/AR-241091-pork-stir-fry-DDMFS-beauty-4x3-eff9d98327ff43a8a90ab4968843f89c.jpg",
        "ingredients": [
            "1 lb pork tenderloin, sliced",
            "1 bell pepper, sliced",
            "1 onion, sliced",
            "2 tbsp soy sauce",
            "1 tbsp ginger, minced"
        ],
        "instructions": [
            "1. Stir-fry pork slices in a pan until browned.",
            "2. Add vegetables and stir-fry for an additional 5 minutes.",
            "3. Add soy sauce and ginger, and stir to combine."
        ]
    },
    {
        "title": "Tomato Soup",
        "image": "https://dishingouthealth.com/wp-content/uploads/2023/01/TomatoRoastedRedPepperSoup_Square.jpg",
        "ingredients": [
            "4 cups tomato juice",
            "1/2 cup cream",
            "1 onion, chopped",
            "2 cloves garlic, minced",
            "Salt and pepper to taste"
        ],
        "instructions": [
            "1. Sauté onion and garlic in a pot until fragrant.",
            "2. Add tomato juice and bring to a boil.",
            "3. Reduce heat and stir in cream.",
            "4. Simmer for 10 minutes and season with salt and pepper."
        ]
    },
    {
        "title": "Spicy Chili",
        "image": "https://www.halfbakedharvest.com/wp-content/uploads/2023/12/Crockpot-Spicy-Queso-Beef-Chili-1-scaled.jpg",
        "ingredients": [
            "1 lb ground beef",
            "1 can kidney beans",
            "1 can diced tomatoes",
            "2 tbsp chili powder",
            "1 tsp cumin",
            "1 jalapeño, chopped"
        ],
        "instructions": [
            "1. Brown ground beef in a pot.",
            "2. Add beans, tomatoes, chili powder, cumin, and jalapeño.",
            "3. Simmer for 30 minutes and serve."
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
