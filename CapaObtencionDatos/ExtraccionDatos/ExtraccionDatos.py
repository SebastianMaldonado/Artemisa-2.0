from EnlaceGbif import EnlaceGbif
from Descompresor import Descompresor
import os
import datetime

import sys
sys.path.insert(0, f'{os.path.dirname(os.path.dirname(__file__))}\ClasesGlobales')
from VariablesFuncionamiento import VariablesFuncionamiento

'''
|====================================================================|
*                        |Extracción de Datos|         
* Descripción:                                                        
*   Clase de gestión general encargada de manejar las solicitudes a la
*   capa de Extracción de Datos
*
*   En esta capa se accede a la descarga de los datasets de GBIF en
*   formato .csv
*
*   Se puede solicitar el seguimiento de archivos por parte de la
*   aplicación para su actualización periódica
|====================================================================|
'''

class ExtraccionDatos (VariablesFuncionamiento):

    def __init__(self):
        super().__init__()
        self.enlazadorGBIF = EnlaceGbif()
        self.descompresor = Descompresor()

        self.proceso = 'EXTRACCION_DATOS'
    
    #---------------------------|Verificar Actualización|---------------------------#
    def verificarActualizacionPeriodica (self) -> dict:
        pass

    #------------------------------|Descargar Dataset|------------------------------#
    def ejecutarDescargaDataset (self, criterios_busqueda: dict = {}) -> dict:
        res_consulta = self.enlazadorGBIF.buscarInfoDataset(criterios_busqueda)

        if (res_consulta['estado'] == self.error):
            return res_consulta

        print(res_consulta)

        llave_dataset = res_consulta['resultado búsqueda'][0]
        res_descarga = self.enlazadorGBIF.descargarDataset(llave_dataset)

        if (res_descarga['estado'] == self.error):
            return res_descarga
        
        print(res_descarga)

        res_descompresion = self.descompresor.descomprimirArchivo(res_descarga['nombre_archivo'])

        if (res_descompresion['estado'] == self.error):
            return res_descompresion

        return {'proceso': self.proceso,
                'estado': self.exito}
    
    #-------------------------|Descargar Lista de Datasets|-------------------------#
    def descargarListaDatasets (self):
        archivo = open(f'{self.entradas_extraccion_datos}\ListaDatasets.txt')
        registro = open(f'{self.registro_extraccion_datos}\Registro_descargas.txt', "w")
        
        for dataset in archivo:
            dataset = dataset.replace('\n', '')
            consulta = {'datasetKey ': dataset}
            res = self.ejecutarDescargaDataset(consulta)
            registro.write(f"\t({datetime.datetime.now()}) -> {res}\n")
    
extraccion = ExtraccionDatos()
gbif = extraccion.enlazadorGBIF
extraccion.descargarListaDatasets()


'''
datasets = ['5fdcdc28-2a80-4236-a257-866b42ed250c',
            'edaa3a20-1d73-42ee-85f2-19105c1c8525',
            'd0a95d44-3622-4c40-bbaf-79a5968c697d',
            'eaa86a97-f30f-4240-979c-7160052e9327',
            'd1af197e-f7f5-4ba7-bffb-c11bf9cb6b79',
            'f1065731-92e2-43fe-b402-ed7736b95c79',
            '4af23e2d-30ab-4bea-a7a6-bee77285dfc3',
            'fa5d6d5c-adf3-4395-9ef4-548cb318cc5a',
            'cf5bf349-8151-4437-9298-8dc285726fb7']

for dataset in datasets:
    consulta = {'datasetKey ': dataset}
    res = extraccion.ejecutarDescargaDataset(consulta)
    print(res)'''
    