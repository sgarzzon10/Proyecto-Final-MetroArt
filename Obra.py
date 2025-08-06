class Obra:
    def __init__(self,id,titulo,artista):
        self.id=id
        self.titulo=titulo
        self.artista=artista
        
    def mostrar(self):
        print(f"ID: {self.id}")
        print(f"Titulo: {self.titulo}")
        print(f"Artista: {self.artista}")
        
    def detalles_obra(self,nacionalidad_artista,fecha_nacimiento,fecha_muerte,creacion,imagen):
        self.nacionalidad_artista=nacionalidad_artista
        self.fecha_nacimiento=fecha_nacimiento
        self.fecha_muerte=fecha_muerte
        self.creacion=creacion
        self.imagen=imagen
    
    def mostrar_detalles(self):
        print(f"ID: {self.id}")
        print(f"Titulo: {self.titulo}")
        print(f"Artista: {self.artista}")
        print(f"Nacionalidad del artista: {self.nacionalidad_artista}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Fecha de muerte: {self.fecha_muerte}")
        print(f"Creacion: {self.creacion}")
        print(f"Imagen: {self.imagen}")
        
        
        
    
        
        
        

