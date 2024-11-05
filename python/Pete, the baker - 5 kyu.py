def cakes(recipe, available):
    
    max_cakes = float('inf')
    
    for ingredient, amount_needed in recipe.items():
        
        amount_available = available.get(ingredient, 0)
        possible_cakes = amount_available // amount_needed
        max_cakes = min(max_cakes, possible_cakes)

    return max_cakes
