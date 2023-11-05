import os

import sys
sys.path.insert(0, f'{os.path.dirname(os.path.dirname(__file__))}')
from ClasesGlobales.VariablesFuncionamiento import VariablesFuncionamiento

'''
|====================================================================|
*                       |Lector de Archivos|         
* Descripción:                                                        
*   Clase encargada de la lectura de los archivos resultantes del
*   proceso de extracción de datos
*   
*   - Recibe archivos en formato .csv delimitados por "\t"
*   - Los archivos son guardados en la carpeta:
*       -> CapaObtencionDatos/ConversionDatos/Base de Datos - Sin Procesar
|====================================================================|
'''

class LectorArchivos (VariablesFuncionamiento):

    def __init__ (self):
        super().__init__()
        self.proceso = 'LECTURA_ARCHIVO_CSV'

    '''
    //---------------------------------------------------------------------------\\
    //                         |Lectura de Archivos csv|                         \\
    //---------------------------------------------------------------------------\\
    '''

    #---------------------------|Leer Grupo de Archivos|---------------------------#
    def leerArchivos (self) -> dict:
        lista_archivos = os.listdir(self.direccion_descompresion)

        datos_archivos = {archivo: self.leerArchivo(archivo) for archivo in lista_archivos}

        return {'proceso': self.proceso,
                'estado': self.exito,
                'datos archivos': datos_archivos}


    #--------------------------|Leer Archivo Individual|--------------------------#
    def leerArchivo (self, nombre_archivo:str) -> list:
        try:
            archivo = open(f'{self.direccion_descompresion}/{nombre_archivo}', 'r', encoding='cp932', errors='ignore')
            
            columnas = archivo.readline().split("\t")
            columnas[-1] = columnas[-1].replace("\n", "")
            datos_archivo = {columna: [] for columna in columnas}

            for linea in archivo.readlines():
                datos = linea.split("\t")
                datos[-1] = datos[-1].replace("\n", "")

                for dato, columna in zip(datos, columnas):
                    datos_archivo[columna].append(dato)

        except Exception as excepcion:
            return {'proceso': self.proceso,
                    'estado': self.error, 
                    'seccion': f'Lectura de Archivo [{nombre_archivo}]',
                    'error': f'{excepcion}'}

        return {'proceso': self.proceso,
                'estado': self.exito,
                'datos archivo': datos_archivo}