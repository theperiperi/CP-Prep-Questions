from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)
        recipe_ingredients = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        
        memo = {}
        result = []

        def can_prepare(recipe):
            if recipe in memo:
                return memo[recipe]

            if recipe in available:
                memo[recipe] = True
                return True

            if recipe not in recipe_ingredients:
                memo[recipe] = False
                return False

            memo[recipe] = False  # Mark as visiting to detect cycles

            for ingredient in recipe_ingredients[recipe]:
                if not can_prepare(ingredient):
                    return False

            memo[recipe] = True
            result.append(recipe)
            return True

        for recipe in recipes:
            can_prepare(recipe)

        return [r for r in recipes if memo.get(r, False)]
