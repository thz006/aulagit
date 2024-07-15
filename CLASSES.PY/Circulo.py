class Circulo:
    def __init__(self,raio):
        self.raio=raio

    def set_valor_do_raio(self):
        print("O raio será igual a: ",self.raio)

    def calcular_area_do_raio(self):
        area=3.14*(self.raio **2)
        print("A área será igual a: ",area)

    def calcular_circunferencia_do_circulo(self):
        circun=2*3.14*self.raio
        print("A circunferência do círculo será de: ",circun)