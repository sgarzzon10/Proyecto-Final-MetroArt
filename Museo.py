from Departamento import Departamento
from Obra import Obra 
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
            elif opcion == "2":
                pass
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            elif opcion == "5":
                break
            else:
                print("Seleccione una opcion valida!")
                
    def obtener_departamentos(self):
        r = requests.get(self.api_departamento)
        r = r.json()
        departamentos = r["departments"]

        for departamento in departamentos:
            self.departamentos.append(Departamento(departamento["departmentId"], departamento["displayName"]))


                
                           
                           
                           
                           
                           
                           
        