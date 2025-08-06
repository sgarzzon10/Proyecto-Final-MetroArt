from Departamento import Departamento
from Obra import Obra 
import requests

class Museo():
    def iniciar_museo(self):
        self.api_departamento = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        self.api_obra_id = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"
        self.api_busqueda = "https://collectionapi.metmuseum.org/public/collection/v1/search"
        self.api_obras_departamento = "https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds=1"
        self.departamentos = []
        self.obtener_departamentos = []
        
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
                           
                           
                           
                           
                           
                           
                           
        