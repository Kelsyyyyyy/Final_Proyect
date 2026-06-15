import pip 
import mysql.connector

print(mysql.connector.__version__)

def crear_conexion():
    conexion = None
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user ="root",
            password='',
            database='purificadorabd',
            port = 3306   
              )

        if conexion.is_conected():
            print("Conexion exitosa")
            return conexion
        
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
def cerrar_conexion(conexion):
    if conexion is not None and conexion.is_conected():
        conexion.close()
        print("Conexion cerrada")

