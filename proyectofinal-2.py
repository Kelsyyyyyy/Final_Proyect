# Install nanoid to run

import mysql.connector
from datetime import datetime
from mysql.connector import Error
from nanoid import generate
from UI import console
from UI import titulo, subtitulo, captura, error, alerta, inputt, show_menu, final_ticket, resume, ticketID, salida, all_orders


def starting():
    titulo("Purified Water")
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
            subtitulo("The connection has been sucessful ")
            return conection
    except Error as e:
        error(f"Error connection MySQL: {e} ")
        return None


def close_conection(conection):
    if conection is not None and conection.is_connected():
        conection.close()
        console.print("[italic red] The conection to MySQL has been closed [/italic red]")


def ID():
    alfabet = "0123456789"
    size = 8
    id_order = generate(alfabet, size)
    return id_order


def obtener_producto(mensaje, datos):
    while True:

        caso = inputt(mensaje).lower().strip()
        if caso == "1":
            return 10, datos["PRECIO_MEDIO"]
        elif caso == "2":
            return 20, datos["PRECIO_COMPLETO"]
        elif caso == "3":
            return 1, datos["PRECIO_LITRO"]
        else:
            alerta("  ⚠ Invalid option. Write: 1, 2 or 3.")


def pedir_sino(mensaje):
    while True:
        respuesta = inputt(mensaje).lower().strip()
        if respuesta in ("yes", "no"):
            return respuesta
        alerta("  ⚠ Invalid Answer. Write: Yes or No.")


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
        alerta("  No costumers were served; there is not average to calculate.")


def validator_ID(message):
    try:
        return message
    except ValueError:
        alerta("You must enter a number ")
        return validator_ID(message)


def search_order(cursor):

    subtitulo("Search Order")
    console.print("[italic cyan] Select an option: \n 1. Search by Ticket ID \n 2. View all orders \n 3. Return to main menu [/italic cyan]")
    option = inputt("Choose an option (1, 2, or 3): ").strip()
    if option == "1":
        search_id = inputt("Enter the Ticket ID to search: ").strip()

        validator_ID(search_id)
        sql = "SELECT * FROM litros WHERE ID = %s"
        try:
            cursor.execute(sql, (search_id,))
            register = cursor.fetchone()

            if register is None:
                alerta(
                    f"\n Order with ID [{search_id}] not found in the database.")
                return

            ticketID(
                register[0], 
                register[1], 
                register[2], 
                register[3], 
                register[4])


        except Error as e:
            error(f" Error executing search query: {e}")
        salida()

    elif option == "2":
        sql = "SELECT * FROM litros"
        try:
            cursor.execute(sql)
            registers = cursor.fetchall()

            if not registers:
                alerta("\n No orders found in the database.")
                return

            all_orders(registers)

        except Error as e:
            error(f" Error executing search query: {e}")
        salida()
    elif option == "3":
        return




def venta(datos, cursor, mi_conexion):
    titulo("Sales software for purified water")

    while datos["repeticion"] == "yes":
        ID_client = ID()
        datos["i"] += 1
        acumc_l = 0
        acumc_p = 0
        captura(datos['i'])

        litros, costo = obtener_producto(
            "What did the costumer bought? 1.Half 2.Full 3.Liter(Choose an option 1, 2 or 3): ", datos)
        acumc_l += litros
        acumc_p += costo

        # Automaticamente obtener fecha y hora de la orden
        ahora = datetime.now()
        fecha = ahora.strftime("%Y-%m-%d")
        hora = ahora.strftime("%H:%M:%S")
        # Pedir fecha y hora de la orden
        # fecha = input(
        # " Date of the order (Format: YYYY-MM-DD, Example: 2026-01-02): ")
        # hora = input(
        # " Put the hour of the order (Format 24h: HH:MM:SS, Example: 23:59:00): ")

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

        final_ticket(ID_client, acumc_l, acumc_p,
                       descuento, iva, total_con_iva)

        try:
            query = "INSERT INTO litros (ID, litros, precio, fecha, hora) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (ID_client, acumc_l,
                           total_con_iva, fecha, hora))
            mi_conexion.commit()
            subtitulo("  Sell registered on the database! ")
        except Error as e:
            error(f"  Error saving on the database: {e}")

        # repeticion = pedir_sino("\nDo you wish to make another order? (Yes/No): ")
        datos["repeticion"] = pedir_sino(
            "\nDo you wish to make another order? (Yes/No): ")

        resume(datos["i"], datos["acumt_l"],
                        datos["acumt_p"], datos["total_descuento"], ID_client)
        console.print("[italic cyan] End of the day [/italic cyan]")
        salida()



def main():
    datos = starting()
    menu_p = ""

    mi_conexion = connector()

    if mi_conexion:
        cursor = mi_conexion.cursor()

        while menu_p != "3":
            menu_p = show_menu()

            if menu_p == "1":
                venta(datos, cursor, mi_conexion)
                # BUSCAR ORDEN
            elif menu_p == "2":
                search_order(cursor)
            elif menu_p == "3":
                titulo("Thank you for your preference")
            else:
                error("Invalid option chosen.")

        cursor.close()
        close_conection(mi_conexion)

    else:
        error("Could not establish connection to the database.")


main()
