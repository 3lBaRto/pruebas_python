import numpy as np



class Cliente:

    def __init__(self,nombre):
        self.nombre=nombre
        self.monto=0

    def depositar(self,monto):
        self.monto += monto

    def extraer(self,monto):
        self.monto -= monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print(self.nombre, "tiene depositado la suma de", self.monto)

class Banco:

    def __init__(self):
        self.clientes = dict()
        self.obtener_clientes()        

    def obtener_clientes(self):

        clientes = dict()
        for idx in range(1,4):
          name = input(f"Por favor ingrese el nombre del cliente {idx}: ")
          obj = Cliente(name)
          clientes[f"cliente{idx}"] = obj

        self.clientes = clientes    
    
    def retornar_Clientes (self):
        return self.clientes  

    def operar(self):
        self.clientes["cliente1"].depositar(100)
        self.clientes["cliente2"].depositar(200)
        self.clientes["cliente3"].depositar(50)
        self.clientes["cliente2"].extraer(80)

    def depositos_totales(self):
        total=self.clientes["cliente1"].retornar_monto()+self.clientes["cliente2"].retornar_monto()+self.clientes["cliente3"].retornar_monto()
        print("El total de dinero del banco es:",total)
        self.clientes["cliente1"].imprimir()
        self.clientes["cliente2"].imprimir()
        self.clientes["cliente3"].imprimir()


Bank = Banco()
x = 1



while x != 0:
    nombre = str(input("Digite su nombre: "))
    for i in Bank.depositos_totales():
        if(nombre==i.nombre):
            print("estas dentro")
        else:
            print("No estas")


    