import os
import pyodbc
import struct
from azure import identity

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

import sys
sys.path.insert(0, f'{os.path.dirname(os.path.dirname(__file__))}')
from ClasesGlobales.VariablesFuncionamiento import VariablesFuncionamiento

'''
|====================================================================|
*                       |Convertidor a SQL|         
* Descripción:                                                        
*   Clase encargada del establecimiento de la Conexión con la
*   Base de Datos remota del servicio de Microsoft Azure
*   
*   La información de las credenciales y cuentas necesarias para su 
*   funcionamiento se encuentran en la clase VariablesFuncionamiento
|====================================================================|
'''

class ConectorBaseDatos (VariablesFuncionamiento):

    def __init__ (self):
        super().__init__()
        self.proceso = 'CONEXION_BASE_DATOS'

        os.environ["AZURE_SQL_CONNECTIONSTRING"] = self.CLAVE_SERVIDOR_SQL


    #---------------------------|Establecimiento de Conexión|---------------------------#
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