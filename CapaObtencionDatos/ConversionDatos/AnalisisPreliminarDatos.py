import os
import sys
sys.path.insert(0, f'{os.path.dirname(os.path.dirname(__file__))}')
from ClasesGlobales.VariablesFuncionamiento import VariablesFuncionamiento

'''
|====================================================================|
*                       |Análisis Preliminar|         
* Descripción:                                                        
*   Clase encargada de realizar un análisis simple de los dataset
*
*   Su funcionalidad es principalmente para la obtención de 
*   información de los dataset originales para su consulta
*
*   - Los archivos son guardados en la carpeta:
*       -> CapaObtencionDatos/ExtraccionDatos/Entradas de Capa/ListaConsultas.txt
|====================================================================|
'''

class AnalisisPreliminarDatos (VariablesFuncionamiento):

    def __init__ (self):
        super().__init__()
        self.proceso = 'ANALISIS_PRELIMINAR_DE_DATOS'


    #---------------------------|Obtener Especies de un Dataset|---------------------------#
    def obtenerEspeciesDatasets (self, datasets: list):
        try:
            lista_especies = []
            for archivo in datasets:
                especies = archivo['species']
                lista_especies += especies

            conjunto_especies = set(lista_especies)
            lista_especies = list(conjunto_especies)
        except Exception as excepcion:
            return {'proceso': self.proceso,
                    'estado': self.error, 
                    'seccion': 'Contabilizar Especies en Conjunto',
                    'error': f'{excepcion}'}

        
        return {'proceso': self.proceso,
                'estado': self.exito,
                'resultado busqueda': lista_especies}
    
    #---------------------------|Registrar Especies para Consulta|---------------------------#
    def registrarEspeciesConsultas (self, datasets: list):
        res = self.obtenerEspeciesDatasets(datasets)

        if (res['estado'] == self.error):
            return res
        
        lista_especies = res['resultado busqueda']
        direccion_registro = f'{self.entradas_extraccion_datos}/ListaConsultas.txt'
        
        try:
            archivo = open(direccion_registro, 'w')

            for especie in lista_especies:
                archivo.write(f'{especie}\n')
        except Exception as excepcion:
            return {'proceso': self.proceso,
                    'estado': self.error, 
                    'seccion': 'Escritura de Especies en Archivo de Consultas',
                    'error': f'{excepcion}'}
        
        return {'proceso': self.proceso,
                'estado': self.exito,
                'direccion registro': direccion_registro}