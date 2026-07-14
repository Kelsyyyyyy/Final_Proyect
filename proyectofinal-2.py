#Install nanoid to run
import mysql.connector
from mysql.connector import Error
from nanoid import generate
PRECIO_MEDIO = 10
PRECIO_COMPLETO = 18
PRECIO_LITRO = 4
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
def ID():
    alfabet="0123456789"
    size=8
    id_order= generate(alfabet, size)
    return id_order

def obtener_producto(mensaje):
    while True:
        caso = input(mensaje).lower().strip()
        if caso == "half":
            return 10, PRECIO_MEDIO
        elif caso == "full":
            return 20, PRECIO_COMPLETO
        elif caso == "liter":
            return 1, PRECIO_LITRO
        else:
            print("  ⚠ Invalid option. Write: Half, Full or Liter.")

def pedir_sino(mensaje):
    while True:
        respuesta = input(mensaje).lower().strip()
        if respuesta in ("yes", "no"):
            return respuesta
        print("  ⚠ Invalid Answer. Write: Yes or No.")

def calcular_totales(litros, precio):
    descuento = precio * 0.10 if litros >= 20 else 0
    precio_final = precio - descuento
    iva = precio_final * 0.16
    total_con_iva = precio_final + iva
    return descuento, iva, total_con_iva

def mostrar_ticket(num_cliente, litros, subtotal, descuento, iva, total):
    print(f"\n  The client {num_cliente} bought: {litros} liters")
    print(f"  Subtotal:       ${subtotal:.2f}")
    print(f"  Discount:     -${descuento:.2f}")
    print(f"  IVA (16%):      ${iva:.2f}")
    print(f"  Total Due:  ${total:.2f}")


def mostrar_resumen(clientes, total_litros, total_pesos, total_descuentos):
    print("\n\t -----Day Resume-----")
    print(f"  Costumers Reached:       {clientes}")
    print(f"  Liters Selled:    {total_litros} L")
    print(f"  Total Collected:          ${total_pesos:.2f}")
    print(f"  Total Discount Amount:   ${total_descuentos:.2f}")
    if clientes > 0:
        print(f"  Average liters/client:  {total_litros / clientes:.2f} L")
        print(f"  Average sell/client:   ${total_pesos / clientes:.2f}")
    else:
        print("  No costumers were served; there is not average to calculate.")
i = 0
acumt_l = 0
acumt_p = 0
total_descuento = 0
repeticion = "yes"
print("\033c")
#Connection
if __name__ == "__main__":
    mi_conexion = connector()
    if mi_conexion:
        cursor = mi_conexion.cursor()      

print("\n\t -----Sales software for purified water-----\t\n")

print("Libro registrado correctamente.")

while repeticion == "yes":
    ID_client=ID()
    i += 1
    acumc_l = 0
    acumc_p = 0
    print(f"\n\t  Capture {i}  \t\n")

    litros, costo = obtener_producto("What did the costumer bought? (Half/Full/Liter): ")
    acumc_l += litros
    acumc_p += costo

    extra = pedir_sino("Did the costumer bought more? (Yes/No): ")
    while extra == "yes":
        litros, costo = obtener_producto("What did the costumer bought? (Half/Full/Liter): ")
        acumc_l += litros
        acumc_p += costo
        extra = pedir_sino("Did the costumer bought more? (Yes/No): ")

    acumt_l += acumc_l

    descuento, iva, total_con_iva = calcular_totales(acumc_l, acumc_p)
    total_descuento += descuento
    acumt_p += total_con_iva

    mostrar_ticket(i, acumc_l, acumc_p, descuento, iva, total_con_iva)
    try:
        query = "INSERT INTO litros (ID, litros, precio, fecha, hora) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (ID_client, acumc_l, total_con_iva))
        mi_conexion.commit() 
        print("  ✓ Venta registrada en la Base de Datos.")
    
    except Error as e:
        print(f"  ❌ Error al guardar en la BD: {e}")
    repeticion = pedir_sino("\nDo you wish to make another order? (Yes/No): ")

mostrar_resumen(i, acumt_l, acumt_p, total_descuento)
