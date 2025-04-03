import string

def je_palindrom(slovo):
    slovo_naopak = slovo[::-1]
    if slovo.lower() == slovo_naopak.lower():
        return True
    else:
        return False
    
print(je_palindrom("oko"))  # True
print(je_palindrom("Python"))  # False
print(je_palindrom("Rotor"))  # True
