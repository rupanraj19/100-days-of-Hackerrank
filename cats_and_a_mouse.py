def catAndMouse(x, y, z):
    catA = abs(x-z)
    catB = abs(y-z)
    
    if catA == catB:
        return "Mouse C"
    elif catA < catB:
        return "Cat A"
    else:
        return "Cat B"
    
print(catAndMouse(1, 2, 3))