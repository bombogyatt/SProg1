import math

# promenne
nejdelsiStrana = 0
stredniStrana = 0
nejkratsiStrana = 0
pythagorovaVeta = 0


# vstupy
a = float(input("Zadej délku první strany: "))
b = float(input("Zadej délku druhé strany: "))
c = float(input("Zadej délku třetí strany: "))

# trojuhelnikova nerovnost a typy trojuhelniku
if (a + b) > c and (a + c) > b and (c + b) > a:
    if a == b and a == c:
        print(f"Strany {a, b, c} tvoří rovnostranný trojúhelník")
        print("Trojúhelník je ostroúhlý")                           # ostrouhly

    elif a != b and c != b:
        print(f"Strany {a, b, c} tvoří obecný  trojúhelník")
        
        # urceni nejvetsi strany
        nejdelsiStrana = max(a, b, c)

        # urceni ostatnich stran
        if nejdelsiStrana == a:
            stredniStrana = max(b, c)
            if stredniStrana == b:
                nejkratsiStrana = c
            else:
                nejkratsiStrana = b     
        if nejdelsiStrana == b:
            stredniStrana = max(a, c)
            if stredniStrana == a:
                nejkratsiStrana = c
            else:
                nejkratsiStrana = a
        if nejdelsiStrana == c:
            stredniStrana = max(a, b)
            if stredniStrana == a:
                nejkratsiStrana = b
            else:
                nejkratsiStrana = a

        # pythagorova veta
        pythagorovaVeta = nejkratsiStrana**2 + stredniStrana**2
        if pythagorovaVeta == nejdelsiStrana**2:
            print("Trojuhelnik je pravouhly")
        elif pythagorovaVeta > nejdelsiStrana**2:
            print("Trojuhelnik je ostrouhly")
        else:
            print("Trojuhelnik je tupouhly")
        

    else:
        print(f"Strany {a, b, c} tvoří rovnoramenný trojúhelník")
        print("Trojúhelník je ostroúhlý")                           # ostrouhly
else:
    print(f"Strany {a, b, c} netvoří trojúhelník")



