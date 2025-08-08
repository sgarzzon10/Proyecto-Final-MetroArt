from Departamento import Departamento
from Obra import Obra 
from nationalities import nacionalities
import requests

class Museo():
    def iniciar_museo(self):
        self.api_departamento = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        self.api_obra_id = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"
        self.api_busqueda = "https://collectionapi.metmuseum.org/public/collection/v1/search?q="
        self.api_obras_departamento = "https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds=1"
        self.departamentos = []
        self.obtener_departamentos()
        
        while True:
            opcion = input('''Seleccione una opcion valida: 
                           1- Ver lista de obras por departamento
                           2- Ver lista de obras por nacionalidad del autor
                           3- Ver lista de obras por nombre del autor
                           4- Mostrar detalles del museo
                           5- Salir del museo
                           ''')
                           
                           
                           
            if opcion == '1':
                self.obras_depto()
                
            elif opcion == "2":
                self.obras_nacionalidades()
                
            elif opcion == "3":
                self.obras_nombre_autor()
            elif opcion == "4":
                self.mostrar_detalles()
            elif opcion == "5":
                break
            else:
                print("Seleccione una opcion valida!")
    
    
    
    def obras_nombre_autor():
        nombre_autor = input("Ingrese el nombre del autor: ")
        response = requests.get(self.api_busqueda + nombre_autor)
        response = response.json()
        ids = response['objectIDs']
        if not ids:
            print("No se encontraron obras para el autor seleccionado. ")
        total = len(ids)
        i = 0
        while i < total:
            bloque_ids = ids[i:i+10]
            bloque_obras = []
            for id in bloque_ids:
                response2 = requests.get(self.api_obra_id + str(id))
                obra = response2.json()
                obra_obj = Obra(
                    obra['objectID'],
                    obra['title'],
                    obra['artistDisplayName']
                )
                bloque_obras.append(obra_obj)
            print(f"Mostrar obras: {i+1} a {min(i+10, total)}:")
            for obra_obj in bloque_obras:
                obra_obj.mostrar()
            i += 10
            if i < total:
                opcion_mas = input("Desea ver mas obras? (s para si, cualquier otra tecla para salir): ")
                if opcion_mas.lower() != "s":
                    break
            else:
                print("No hay mas obras para mostrar. ")
            
    
    
    
    
    
    
    
    
    def mostrar_detalles():
        obra_id = input("Ingrese el ID de la obra: ")
        response = requests.get(self.api_obra_id + obra_id)
        obra = response.json()
        if not obra:
            print("Obra no encontrada.")
        
        obra_obj = Obra(
            obra['objectID'],
            obra["title"],
            obra["artistDisplayName"]
        )
        obra_obj.detalles_obra(
            obra["artistNationality"],
            obra["artistBeginDate"],
            obra["artistEndDate"],
            obra["objectDate"], 
            obra["primaryImage"]
        )
        obra_obj.mostrar_detalles()
        
    
    
    
    def obras_depto(self):
        for departamento in self.departamentos:
                    departamento.mostrar()
        eleccion = input("Ingrese el ID del departamento: ")
        response = requests.get(self.api_obras_departamento + eleccion)
        response = response.json()
        ids = response['objectIDs']
        departamento_opcion = None
        for departamento in self.departamentos:
            if str(departamento.id) == eleccion:
                departamento_opcion = departamento
            if departamento_opcion is None:
                print("Departamento no encontrado. Intente de nuevo.")
                continue
            total = len(ids)
            i = 0
            while i < total:
                bloque_ids = ids[i:i+10]
                bloque_obras = []
                for id in bloque_ids:
                    response2 = requests.get(self.api_obra_id + str(id))
                    obra = response2.json()
                    obra_obj = Obra(
                        obra['objectID'],
                        obra["title"],
                        obra["artistDisplayName"]
                    )         
                        
                    departamento_opcion.nueva_obra(obra_obj)
                    bloque_obras.append(obra_obj)
                        
                print(f"Mostrando obras {i+1} a {min(i+10, total)}:")
                for obra in bloque_obras:
                    print(f"ID: {obra.id}, Título: {obra.titulo}, Autor: {obra.artista}")
                i += 10
                if i < total:
                    opcion_mas = input("¿Desea ver más obras? (s para sí, cualquier otra tecla para salir): ")
                    if opcion_mas.lower() != 's':
                        break
                else:
                    print("No hay más obras para mostrar.")
    
    def obras_nacionalidades(self):
        print("Nacionalidades: ")
        for nacionalidad in nacionalities:
            print(nacionalidad)
        nacionalidad = input("Seleccione una opcion: ")
        response = requests.get(self.api_busqueda + nacionalidad)
        response = response.json()
        ids = response["objectIDs"]
        if not ids: 
            print("No se encontraron obras para la nacionalidad seleccionada.")
            
        total = len(ids)
        i = 0 #falta el while
        while i < total:
            bloque_ids = ids[i:i+10]
            bloque_obras = []
            for id in bloque_ids:
                responde2 = requests.get(self.api_obra_id + str(id))
                obra = responde2.json()
                obra_obj = Obra(
                    obra["objectID"],
                    obra["title"],
                    obra['artistDisplayName']
                )
                bloque_obras.append(obra_obj)
            print(f"Mostrando obras {i+1} a {min(i+10, total)}: ")
            for obra_obj in bloque_ids:
                obra_obj.mostrar()
            i += 10
            if i < total:
                opcion_mas = input("¿Desea ver mas obras? (s para si, cualquier otra tecla para salir): ")
                if opcion_mas.lower() != "s":
                    break
                else:
                    print("No hay mas obras para mostrar.")
                
    def obtener_departamentos(self):
        r = requests.get(self.api_departamento)
        r = r.json()
        departamentos = r["departments"]

        for departamento in departamentos:
            self.departamentos.append(Departamento(departamento["departmentId"], departamento["displayName"]))


                
                           
                           
                           
                           
                           
                           
        