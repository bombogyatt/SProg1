import random

def prehazej(slovo):
    
    prehazene_slovo = ""

    for i in range(len(slovo)):
        random = random.randint(0, len(slovo))
        prehazene_slovo += slovo[random.randint(0, len(slovo))]
        
    return prehazene_slovo

print(prehazej("ahoj"))