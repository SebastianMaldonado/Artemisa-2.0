import time
import sys, os
sys.path.insert(0, f'{os.path.dirname(os.path.dirname(__file__))}')

from ConversionDatos.ConversionDatos import ConversionDatos
from ExtraccionDatos.ExtraccionDatos import ExtraccionDatos

'''
|====================================================================|
*                       |Gestión Global|         
* Descripción:                                                        
*   Archivo en el que se tiene acceso a todas las clases del programa
*   con el fin de ejecutar procesos conjuntos entre las diferentes
*   capas del sistema
|====================================================================|
'''

extraccion = ExtraccionDatos()
conversor = ConversionDatos()

# Descargar todos los Datasets ingresados en las Entradas de la Capa de Extracción de Datos
#   -> Artemisa-PC-01/Artemisa-2.0/CapaObtencionDatos/ExtraccionDatos/Entradas de Capa/ListaDatasets.txt
while (True):
  res_descarga = extraccion.descargarListaDatasets()
  print(res_descarga)
  res_descarga = None
  time.sleep(120)

'''
 Para encontrar el resultado de cada operación de descarga consultar:
   -> Artemisa-PC-01/Artemisa-2.0/CapaObtencionDatos/ExtraccionDatos/Historial/Registro_descargas.txt
'''

# Analizar preliminarmente los datasets descargados para registrar las especies
#   -> Artemisa-PC-01/Artemisa-2.0/CapaObtencionDatos/ExtraccionDatos/Entradas de Capa/ListaConsultas.txt
#res_registro = conversor.registrarEspeciesConsultas()
#print(res_registro)

# Consultar todos los nombres de las especies encontradas en los datasets, los resultados se guardarán en
#   -> Artemisa-PC-01/Artemisa-2.0/CapaObtencionDatos/ExtraccionDatos/Entradas de Capa/ListaDatasets.txt
#res_consultas = extraccion.registrarDatasetsIncidencias()
#print(res_consultas)

'''
 Para encontrar el resultado de cada operación de descarga consultar:
   -> Artemisa-PC-01/Artemisa-2.0/CapaObtencionDatos/ExtraccionDatos/Historial/Registro_consultas.txt
'''
