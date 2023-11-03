from pygbif import occurrences
from pygbif import species
import os

import sys
sys.path.insert(0, f'{os.path.dirname(os.path.dirname(__file__))}\ClasesGlobales')
from VariablesFuncionamiento import VariablesFuncionamiento

'''
|====================================================================|
*                       |Enlace a GBIF|         
* Descripción:                                                        
*   Clase encargada de manejar la API para Python de GBIF
*   A través de esta clase se solicitan las descargas de dataset y
*   las consultas de incidencia de especies
*   
*   - Los archivos son guardados en la carpeta:
*       -> CapaObtencionDatos\ExtraccionDatos\Dataset Descargados
|====================================================================|
'''

class EnlaceGbif (VariablesFuncionamiento):

    def __init__ (self):
        super().__init__()
        self.proceso = 'DESCARGA_ARCHIVO'

        os.environ['GBIF_USER'] = self.GBIF_USER
        os.environ['GBIF_PWD'] = self.GBIF_PWD
        os.environ['GBIF_EMAIL'] = self.GBIF_EMAIL


    #------------------------------|Buscar Dataset|------------------------------#
    def buscarInfoDataset (self, criterios_busqueda: dict = {}) -> dict:
        #Obtener Llave de descarga del Dataset

        try:
            peticion = []
            for criterio in criterios_busqueda.keys():
                solicitud_criterio = criterios_busqueda[criterio].replace(" ", "")
                criterio = criterio.replace(" ", "")

                consulta = f"{criterio} = {solicitud_criterio}"
                peticion.append(consulta)
            
            if len(peticion) == 1:
                peticion = peticion[0]

            print(peticion)
        except Exception as excepcion:
            return {'proceso': self.proceso,
                    'estado': self.error, 
                    'seccion': 'Estandarización de Solicitudes',
                    'error': f'{excepcion}'}

        try:
            info_dataset = occurrences.download(peticion)
            llave_descarga = info_dataset[0]
            print(f"Llave de descarga: {llave_descarga}")
        except Exception as excepcion:
            return {'proceso': self.proceso,
                    'estado': self.error, 
                    'seccion': 'Solicitud de Llave de descarga',
                    'error': f'{excepcion}'}
        
        return {'proceso': self.proceso,
                'estado': self.exito,
                'resultado búsqueda': info_dataset}

    #------------------------------|Descargar Dataset|------------------------------#
    def descargarDataset (self, llave_descarga) -> dict:
        #Descargar dataset por medio de la llave de descarga
        try:
            reintentar = True
            try:
                occurrences.download_get(llave_descarga, path=self.direccion_descarga)
                reintentar = False
            except Exception as excepcion:
                if not(f'{excepcion}' == f'download "{llave_descarga}" not of status SUCCEEDED'):
                    reintentar = False
                    print("Reintentando")

        except Exception as excepcion:
            return {'proceso': self.proceso,
                    'estado': self.error, 
                    'seccion': 'Descarga de Archivo comprimido',
                    'error': f'{excepcion}'}
        
        return {'proceso': self.proceso,
                'estado': self.exito,
                'nombre_archivo': f"{llave_descarga}.zip"}
    
    #------------------------|Buscar Incidencias de Especie|------------------------#
    def buscarIncidencias (self, especie) -> dict:
        llave_especie = species.name_suggest(q=especie)[0]['key']
        resultados = occurrences.search(taxonKey=llave_especie)
        datasets = list(set([dato['datasetKey'] for dato in resultados['results']]))
        return datasets
