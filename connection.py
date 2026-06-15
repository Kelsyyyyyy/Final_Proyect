#holao
import mysql.connector
from mysql.connector import Error
def connector():
    conection=None 
    try:
        conection=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="Usuario",
                port=3306
                )
        if conection.is_connected():
            print("The connection has been sucessful ")
            return conection
    except Error as e:
        print(f"Error connection MySQL: {e} ")
        return None
def close_conection(conection):
    if conection is None and conection.is_connected():
        conection.close()
        print ("The conection to MySQL has been closed ")
if __name__ == "__main__":
    mi_conexion = connector()
    if mi_conexion:
        close_conection(mi_conexion)        
