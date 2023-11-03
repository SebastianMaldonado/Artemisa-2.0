import os
#import mysql.connector
#from mysql.connector import Error
import pandas as pd

import os
import pyodbc, struct
from azure import identity

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

import sys
sys.path.insert(0, f'{os.path.dirname(os.path.dirname(__file__))}\ClasesGlobales')
from VariablesFuncionamiento import VariablesFuncionamiento

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
        self.proceso = 'CONVERSION_DATOS_A_SQL'

        os.environ["AZURE_SQL_CONNECTIONSTRING"] = self.CLAVE_SERVIDOR_SQL

    def establecerConexionBaseDatos (self):
        try:
            conn = pyodbc.connect(self.CLAVE_SERVIDOR_SQL)
            conexion = conn.cursor()
        except Exception as excepcion:
            return {'proceso': self.proceso,
                    'estado': self.error,
                    'seccion': f'Establecimiento de Conexión con el Servidor',
                    'error': f'{excepcion}'}

        return {'proceso': self.proceso,
                'estado': self.exito,
                'conexion': conexion}