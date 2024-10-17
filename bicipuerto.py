from typing import List
from bicicleta import Bici


class BiciPuerto:
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre
        self.bicicletas: List[Bici] = []
        
    def insertar_final(self, bici: Bici):
        self.bicicletas.append(bici)
        
    def mostrar(self):
        print('BiciPuerto:' + self.nombre)
        for bici in self.bicicletas:
            print(bici)
        
    def mostrar_tabla(self):
        headers = 'ID'.ljust(5) + 'Uso Total'.ljust(12) + 'Metros recorridos'.ljust(25) + 'Usuario'.ljust(10)
        print(headers)
        print('_' * len(headers))
        for bici in self.bicicletas:
            id = str(bici.id).ljust(5)
            uso_total = str(bici.uso).ljust(12)
            distancia = str(bici.distancia).ljust(25)
            usuario = bici.usuario.ljust(10)
            print(id+uso_total+distancia+usuario)
    
    def guardar(self):
        with open('./csv/bicis.csv', 'w') as archivo:
            for bici in self.bicicletas:
                archivo.write(str(bici.id) +  ',')
                archivo.write(str(bici.uso) + ',')
                archivo.write(str(bici.distancia) + ',')
                archivo.write(bici.usuario + '\n')
                
    def recuperar(self, nombre:str):
        with open(nombre, 'r') as archivo:
            for line in archivo: 
                atributos = line.strip().split(',')#split sirve para dividir 
                bici = Bici(id=int(atributos[0]), uso=int(atributos[1]), distancia=int(atributos[2]), usuario=atributos[3])
                self.bicicletas.append(bici)