class Departamento:
    def __init__(self,id,nombre):
        self.id=id
        self.nombre=nombre
        
    def mostrar(self):
        print(f"Id: {self.id} - {self.nombre}" )
        
    def nueva_obra(self,obra):
        self.obras.append(obra)
        
    def mostrar_obras(self):
        for obra in self.obras:
            obra.mostrar()
            print()
    
        