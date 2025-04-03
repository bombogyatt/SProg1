def prevod_na_minuty(hodiny, minuty):
    if  not  hodiny < 0 and not minuty < 0:
        return hodiny * 60 + minuty
    else:
        return None
    
print(prevod_na_minuty(2, 45))  
print(prevod_na_minuty(-1, 30))
