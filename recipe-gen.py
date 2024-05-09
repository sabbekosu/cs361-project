def main():
    # Recipes database: Each recipe is associated with a set of ingredients
    recipes = {
        'Tomato Soup': {'tomato', 'onion', 'garlic', 'basil', 'salt', 'pepper'},
        'Apple Pie': {'apple', 'sugar', 'flour', 'butter', 'cinnamon'},
        'Vegetable Stir Fry': {'broccoli', 'carrot', 'bell pepper', 'soy sauce', 'garlic', 'onion'},
        'Mango Salad': {'mango', 'lime', 'chili', 'salt', 'pepper'},
        'Spaghetti Carbonara': {'spaghetti', 'egg', 'bacon', 'parmesan', 'pepper'}
    }

    # Ingredients set for easy access and checking
    all_ingredients = set(ingredient for ingredients in recipes.values() for ingredient in ingredients)

    while True:
        print("\nMain Menu:")
        print("1. View Ingredients")
        print("2. View Recipes")
        print("3. Find Recipe with My Ingredients")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            print("\nAvailable Ingredients:")
            for ingredient in sorted(all_ingredients):
                print(ingredient)

        elif choice == '2':
            print("\nAvailable Recipes:")
            for recipe, ingredients in recipes.items():
                print(f"{recipe}: Ingredients - {', '.join(ingredients)}")

        elif choice == '3':
            user_ingredients = input("Enter your favorite ingredients (comma separated): ").split(',')
            user_ingredients = set(ingredient.strip().lower() for ingredient in user_ingredients)

            # Find the best matching recipe
            best_recipe = None
            max_match_count = 0

            for recipe, ingredients in recipes.items():
                match_count = len(user_ingredients.intersection(ingredients))
                if match_count > max_match_count:
                    max_match_count = match_count
                    best_recipe = recipe

            if best_recipe:
                print(f"\nBest matching recipe: {best_recipe}")
            else:
                print("\nNo matching recipes found.")

        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == '__main__':
    main()
