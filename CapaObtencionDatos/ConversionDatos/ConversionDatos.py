import os
import pandas as pd

from .LectorArchivos import LectorArchivos
from .ConectorBaseDatos import ConectorBaseDatos
from .AnalisisPreliminarDatos import AnalisisPreliminarDatos

import sys
sys.path.insert(0, f'{os.path.dirname(os.path.dirname(__file__))}')
from ClasesGlobales.VariablesFuncionamiento import VariablesFuncionamiento

'''
|====================================================================|
*                       |Convertidor a SQL|         
* Descripción:                                                        
*   Clase encargada de la lectura de los archivos resultantes del
*   proceso de extracción de datos
*   
*   - Los archivos son guardados en la carpeta:
*       -> CapaObtencionDatos\ExtraccionDatos\Dataset Descargados
|====================================================================|
'''

class ConversionDatos (VariablesFuncionamiento):
    
    def __init__ (self):
        super().__init__()
        self.conector_bd = ConectorBaseDatos()
        self.lector_archivos = LectorArchivos()
        self.analizador = AnalisisPreliminarDatos()

        self.proceso = 'CONVERSION_DATOS_A_SQL'

    #---------------------------|Registrar Especies para Consulta|---------------------------#
    def registrarEspeciesConsultas (self):
        res_lectura = self.lector_archivos.leerArchivos()

        if (res_lectura['estado'] == self.error):
            return res_lectura

        lista_datasets = [res_lectura['datos archivos'][archivo]['datos archivo'] for archivo in res_lectura['datos archivos'].keys()]

        res_analisis = self.analizador.registrarEspeciesConsultas(lista_datasets)

        return res_analisis
