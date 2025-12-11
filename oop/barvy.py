class Barva:

    def __init__(self, _r, _g, _b):
        self.r = _r
        self.g = _g
        self.b = _b

    def __str__(self):
        return f'RGB({self.r}, {self.g}, {self.b})'
    
    def __add__(self, jina):
        n_r = int((self.r + jina.r)/2)
        n_g = int((self.g + jina.g)/2)
        n_b = int((self.b + jina.b)/2)
        return Barva(n_r, n_g, n_b)

    def __mul__(self, nasobek):
        n_r = max(0, min(255, int(self.r * nasobek)))
        n_g = max(0, min(255, int(self.g * nasobek)))
        n_b = max(0, min(255, int(self.b * nasobek)))

        return Barva(n_r, n_g, n_b)


    def invertuj(self):
        n_r = 255 - self.r
        n_g = 255 - self.g
        n_b = 255 - self.b

        return Barva(n_r, n_g, n_b)
    
    def to_hex(self):
        h_r = hex(self.r)
        print(h_r)
        h_g = hex(self.g)
        print(h_g)
        h_b = hex(self.b)
        print(h_b)

        return f'#{h_r[-2:]}{h_g[-2:]}{h_b[-2:]}'


oranzova = Barva(255, 100, 0)
print(f"{oranzova} = {oranzova.to_hex()}")  
# RGB(255, 100, 0) = #FF6400

bila = Barva(255, 255, 255)
print(f"{bila} = {bila.to_hex()}")  
# RGB(255, 255, 255) = #FFFFFF