def beeramid(bonus, price):
    
    cans = bonus/price
    level = 1
    
    while level**2 <= cans:
        cans -= level**2
        level += 1
    
    return level - 1
