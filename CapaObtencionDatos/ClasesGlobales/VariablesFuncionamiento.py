from abc import ABC
import os

class VariablesFuncionamiento (ABC):

    def __init__ (self):
 
        #Variables de control de errores
        self.exito = 'EXITO'
        self.error = 'ERROR'

        #Variables de Validación de Usuario de GBIF
        self.GBIF_USER = 'artemisa'
        self.GBIF_PWD = 'Artemisa1945'
        self.GBIF_EMAIL = 'artemisa1945@outlook.com'

        #Variables de Validación de Usuario para MySQL
        self.SQL_HOST = ''
        self.SQL_USER = 'artemisa'
        self.SQL_PWD = 'Datachallenge2023'

        self.CLAVE_SERVIDOR_SQL = 'Driver={SQL Server};Server=tcp:artemisa-2.database.windows.net,1433;Database=artemisa-base-datos;Uid=azureuser;Pwd={Datachallenge2023};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

        #Variables de manejo de direcciones
        self.direccion_carpeta = f'{os.path.dirname(os.path.dirname(__file__))}'
        
        self.direccion_descarga = f"{self.direccion_carpeta}\ExtraccionDatos\Dataset Descargados"
        self.direccion_descompresion = f"{self.direccion_carpeta}\ExtraccionDatos\Dataset Descomprimidos"
        self.direccion_bd_sin_procesar = f'{self.direccion_carpeta}\ConversionDatos\Base de Datos - Sin Procesar'
        self.entradas_extraccion_datos = f'{self.direccion_carpeta}\ExtraccionDatos\Entradas de Capa'
        self.registro_extraccion_datos = f'{self.direccion_carpeta}\ExtraccionDatos\Historial'
        
        self.direccion_datos_globales = f'{self.direccion_carpeta}\DatosGlobales'