print("\033c")
print("\n\t -----Programa para venta de agua purificada-----\t\n")

PRECIO_MEDIO = 10
PRECIO_COMPLETO = 18
PRECIO_LITRO = 4

def obtener_producto(mensaje):
    while True:
        caso = input(mensaje).lower().strip()
        if caso == "medio":
            return 10, PRECIO_MEDIO
        elif caso == "completo":
            return 20, PRECIO_COMPLETO
        elif caso == "litro":
            return 1, PRECIO_LITRO
        else:
            print("  ⚠ Opción no válida. Escribe: Medio, Completo o Litro.")

def pedir_sino(mensaje):
    while True:
        respuesta = input(mensaje).lower().strip()
        if respuesta in ("si", "no"):
            return respuesta
        print("  ⚠ Respuesta no válida. Escribe: Si o No.")

def calcular_totales(litros, precio):
    descuento = precio * 0.10 if litros >= 20 else 0
    precio_final = precio - descuento
    iva = precio_final * 0.16
    total_con_iva = precio_final + iva
    return descuento, iva, total_con_iva

def mostrar_ticket(num_cliente, litros, subtotal, descuento, iva, total):
    print(f"\n  El cliente {num_cliente} compro: {litros} litros")
    print(f"  Subtotal:       ${subtotal:.2f}")
    print(f"  Descuento:     -${descuento:.2f}")
    print(f"  IVA (16%):      ${iva:.2f}")
    print(f"  Total a pagar:  ${total:.2f}")

def mostrar_resumen(clientes, total_litros, total_pesos, total_descuentos):
    print("\n\t -----Resumen del dia-----")
    print(f"  Clientes atendidos:       {clientes}")
    print(f"  Total litros vendidos:    {total_litros} L")
    print(f"  Total recaudado:          ${total_pesos:.2f}")
    print(f"  Total descuentos dados:   ${total_descuentos:.2f}")
    if clientes > 0:
        print(f"  Promedio litros/cliente:  {total_litros / clientes:.2f} L")
        print(f"  Promedio venta/cliente:   ${total_pesos / clientes:.2f}")
    else:
        print("  No se atendió ningún cliente; no hay promedios que calcular.")

i = 0
acumt_l = 0
acumt_p = 0
total_descuento = 0
repeticion = "si"

while repeticion == "si":
    i += 1
    acumc_l = 0
    acumc_p = 0
    print(f"\n\t  Captura {i}  \t\n")

    litros, costo = obtener_producto("Que compro el cliente? (Medio/Completo/Litro): ")
    acumc_l += litros
    acumc_p += costo

    extra = pedir_sino("El cliente compro mas? (Si/No): ")
    while extra == "si":
        litros, costo = obtener_producto("Que compro el cliente? (Medio/Completo/Litro): ")
        acumc_l += litros
        acumc_p += costo
        extra = pedir_sino("El cliente compro mas? (Si/No): ")

    acumt_l += acumc_l

    descuento, iva, total_con_iva = calcular_totales(acumc_l, acumc_p)
    total_descuento += descuento
    acumt_p += total_con_iva

    mostrar_ticket(i, acumc_l, acumc_p, descuento, iva, total_con_iva)

    repeticion = pedir_sino("\nDesea realizar otra captura? (Si/No): ")

mostrar_resumen(i, acumt_l, acumt_p, total_descuento)