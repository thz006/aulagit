class Triangulo:
    def __init__(self,lado_a,lado_b,lado_c):
        self.lado_a=lado_a
        self.lado_b=lado_b
        self.lado_c=lado_c

    def calcular_perimetro(self):
        perimetro= self.lado_a + self.lado_b + self.lado_c
        print("O perímetro será: ",perimetro)
    
    def get_maior_lado(self):
        if self.lado_a > self.lado_b and self.lado_a > self.lado_c:
            print("O lado maior é o lado: ",self.lado_a)
        elif self.lado_b > self.lado_a and self.lado_b > self.lado_c:
            print("O lado maior é o lado: ",self.lado_b)
        elif self.lado_c > self.lado_a and self.lado_c > self.lado_b:
            print("O lado maior é o lado: ",self.lado_c)
        area=(self.lado_b * self.lado_a) / 2
        print("A área será: ",area)