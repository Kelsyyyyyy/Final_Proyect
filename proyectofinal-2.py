# Install nanoid to run

import mysql.connector
from mysql.connector import Error
from nanoid import generate


def starting():
    datos = {
        "PRECIO_MEDIO": 10,
        "PRECIO_COMPLETO": 18,
        "PRECIO_LITRO": 4,
        "i": 0,
        "acumt_l": 0,
        "acumt_p": 0,
        "total_descuento": 0,
        "repeticion": "yes"
    }
    print("\033c")

    return datos


def connector():

    conection = None
    try:
        conection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="usuario",
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
        print("The conection to MySQL has been closed ")


def ID():
    alfabet = "0123456789"
    size = 8
    id_order = generate(alfabet, size)
    return id_order


def obtener_producto(mensaje, datos):
    while True:
        caso = input(mensaje).lower().strip()
        if caso == "1":
            return 10, datos["PRECIO_MEDIO"]
        elif caso == "2":
            return 20, datos["PRECIO_COMPLETO"]
        elif caso == "3":
            return 1, datos["PRECIO_LITRO"]
        else:
            print("  ⚠ Invalid option. Write: 1, 2 or 3.")


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


def mostrar_resumen(clientes, total_litros, total_pesos, total_descuentos, ID_client):
    print("\n\t -----Day Resume-----")
    print(f"  Costumers Reached:       {clientes}")
    print(f"  Liters Selled:    {total_litros} L")
    print(f"  Total Collected:          ${total_pesos:.2f}")
    print(f"  Total Discount Amount:   ${total_descuentos:.2f}")
    print(f"   Your order is the {ID_client}")
    if clientes > 0:
        print(f"  Average liters/client:  {total_litros / clientes:.2f} L")
        print(f"  Average sell/client:   ${total_pesos / clientes:.2f}")
    else:
        print("  No costumers were served; there is not average to calculate.")


def validator_ID(message):
    try:
        return message
    except ValueError:
        print("You must enter a number ")
        return validator_ID(message)


def search_order(cursor):
    print("\n\t -----Search Order-----\t\n")
    search_id = input("Enter the Ticket ID to search: ").strip()
    validator_ID(search_id)
    sql = "SELECT * FROM litros WHERE ID = %s"
    try:
        cursor.execute(sql, (search_id,))
        register = cursor.fetchone()

        if register is None:
            print(f"\n Order with ID [{search_id}] not found in the database.")
            return

        print(f" Ticket ID:   {register[0]}")
        print(f" Total Water: {register[1]} Liters")
        print(f" Total Paid:  ${register[2]:.2f} MXN")
        print(f" Date:        {register[3]}")
        print(f" Time:        {register[4]}")

    except Error as e:
        print(f" Error executing search query: {e}")
    input("\nPress Enter to return to the main menu...")


def menu():
    print("\033c")
    print("=== PURIFIED WATER SYSTEM ===")
    print("1. Register a new sale")
    print("2. Search for an existing order")
    print("3. Exit the program")
    menu_p = input("Choose an option (1,2,3): ").strip()
    return menu_p


def venta(datos):
    print("\n\t -----Sales software for purified water-----\t\n")

    while datos["repeticion"] == "yes":
        ID_client = ID()
        datos["i"] += 1
        acumc_l = 0
        acumc_p = 0
        print(f"\n\t  Capture {datos['i']}  \t\n")

        litros, costo = obtener_producto(
            "What did the costumer bought? 1.Half 2.Full 3.Liter(Choose an option 1, 2 or 3): ", datos)
        acumc_l += litros
        acumc_p += costo
        fecha = input(
            " Date of the order (Format: YYYY-MM-DD, Example: 2026-01-02): ")
        hora = input(
            " Put the hour of the order (Format 24h: HH:MM:SS, Example: 23:59:00): ")

        extra = pedir_sino("Did the costumer bought more? (Yes/No): ")
        while extra == "yes":
            litros, costo = obtener_producto(
                "What did the costumer bought? 1.Half 2.Full 3.Liter(Choose an option 1, 2 or 3): ", datos)
            acumc_l += litros
            acumc_p += costo
            extra = pedir_sino("Did the costumer bought more? (Yes/No): ")

        datos["acumt_l"] += acumc_l

        descuento, iva, total_con_iva = calcular_totales(acumc_l, acumc_p)
        datos["total_descuento"] += descuento
        datos["acumt_p"] += total_con_iva

        mostrar_ticket(ID_client, acumc_l, acumc_p,
                       descuento, iva, total_con_iva)

        try:
            query = "INSERT INTO litros (ID, litros, precio, fecha, hora) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (ID_client, acumc_l,
                           total_con_iva, fecha, hora))
            mi_conexion.commit()
            print("  Sell registered on the database! ")
        except Error as e:
            print(f"  Error saving on the database: {e}")

        # repeticion = pedir_sino("\nDo you wish to make another order? (Yes/No): ")
        datos["repeticion"] = pedir_sino(
            "\nDo you wish to make another order? (Yes/No): ")

        mostrar_resumen(datos["i"], datos["acumt_l"],
                        datos["acumt_p"], datos["total_descuento"], ID_client)


starting()


def main():
    datos = starting()
    menu_p = ""

    mi_conexion = connector()

    if mi_conexion:
        cursor = mi_conexion.cursor()

        while menu_p != "3":
            menu_p = menu()

            if menu_p == "1":
                venta(datos)
                # BUSCAR ORDEN
            elif menu_p == "2":
                search_order(cursor)
            elif menu_p == "3":
                print("Exiting the program.")
            else:
                print("Invalid option chosen.")

            cursor.close()
            close_conection(mi_conexion)
    else:
        print("Could not establish connection to the database.")


main()
