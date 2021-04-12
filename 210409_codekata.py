def get_max_area(height):
    lp, rp = 0, len(height)-1
    biggest, challenger = 0, 0

    while lp < rp:
        
        if height[lp] <= height[rp]:
            challenger = height[lp] * (rp - lp)
            
            if height[lp] < height[lp+1] or height[lp+1] > height[rp-1]:
                    lp += 1
            else:
                rp -= 1

        
        elif height[lp] > height[rp]:
            challenger = height[rp] * (rp - lp)

            if height[rp] < height[rp-1] or height[rp-1] > height[lp+1]: 
                    rp -= 1
            else:
                lp += 1
    
        if biggest < challenger:
            biggest = challenger

    return biggest

print(get_max_area([35, 46, 43, 59, 59]))