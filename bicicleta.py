class Bici:
    def __init__(self, id=0, uso=0, distancia=0, usuario='') -> None:
        self.id = id
        self.uso = uso
        self.distancia = distancia
        self.usuario = usuario
        
    def __repr__(self) -> str:
        return "ID: " + str(self.id) + ' Uso Total: ' + str(self.uso) + ' Distancia Recorrida: ' + str(self.distancia) + ' Usuario: ' + self.usuario
    
    def to_dict(self):
        return{
            "id": self.id, 
            "uso":  self.uso,
            "distancia": self.distancia,
            "usuario": self.usuario
        }