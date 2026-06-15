print("\033c")
print("\n\t -----Programa para venta de agua purificada-----\t\n")

# Constantes
PRECIO_MEDIO = 10
PRECIO_COMPLETO = 18
PRECIO_LITRO = 4

# Variables
i = 0
litros = 0
costo = 0
repeticion = "si"
acumc_l = 0
acumc_p = 0
acumt_l = 0
acumt_p = 0
total_descuento = 0
promedio_litros = 0
promedio_pesos = 0

while repeticion == "si":

    # Contador de clientes
    i = i + 1
    acumc_l = 0
    acumc_p = 0

    print(f"\n\t  Captura {i}  \t\n")

    caso = input("Que compro el cliente? (Medio/Completo/Litro): ").lower()

    # Expresion 1: asignacion con constante segun caso
    if caso == "medio":
        costo = PRECIO_MEDIO
        litros = 10
    elif caso == "completo":
        costo = PRECIO_COMPLETO
        litros = 20
    elif caso == "litro":
        costo = PRECIO_LITRO
        litros = 1
    else:
        costo = 0
        litros = 0

    # Expresion 2: acumulacion de litros y pesos por cliente
    acumc_l = acumc_l + litros
    acumc_p = acumc_p + costo

    # Expresion 3: acumulacion total
    acumt_l = acumt_l + litros
    acumt_p = acumt_p + costo

    extra = input("El cliente compro mas? (Si/No): ").lower()

    while extra == "si":

        caso_ex = input("Que compro el cliente? (Medio/Completo/Litro): ").lower()

        # Expresion 4: misma logica de precios para compras extra
        if caso_ex == "medio":
            costo = PRECIO_MEDIO
            litros = 10
        elif caso_ex == "completo":
            costo = PRECIO_COMPLETO
            litros = 20
        elif caso_ex == "litro":
            costo = PRECIO_LITRO
            litros = 1
        else:
            costo = 0
            litros = 0

        acumc_l = acumc_l + litros
        acumc_p = acumc_p + costo
        acumt_l = acumt_l + litros
        acumt_p = acumt_p + costo

        extra = input("El cliente compro mas? (Si/No): ").lower()

    # Expresion 5: descuento del 10% si compra 20 litros o mas
    if acumc_l >= 20:
        descuento = acumc_p * 0.10
    else:
        descuento = 0

    # Expresion 6: precio final con descuento aplicado
    precio_final = acumc_p - descuento

    # Expresion 7: calculo de IVA
    iva = precio_final * 0.16

    # Expresion 8: total con IVA
    total_con_iva = precio_final + iva

    # Acumulador de descuentos totales
    total_descuento = total_descuento + descuento

    print(f"\n  El cliente {i} compro: {acumc_l} litros")
    print(f"  Subtotal:       ${acumc_p:.2f}")
    print(f"  Descuento:     -${descuento:.2f}")
    print(f"  IVA (16%):      ${iva:.2f}")
    print(f"  Total a pagar:  ${total_con_iva:.2f}")

    repeticion = input("\nDesea realizar otra captura? (Si/No): ").lower()

# Expresion 9: promedio de litros por cliente
promedio_litros = acumt_l / i

# Expresion 10: promedio de venta por cliente
promedio_pesos = acumt_p / i

print("\n\t -----Resumen del dia-----")
print(f"  Clientes atendidos:       {i}")
print(f"  Total litros vendidos:    {acumt_l} L")
print(f"  Total recaudado:          ${acumt_p:.2f}")
print(f"  Total descuentos dados:   ${total_descuento:.2f}")
print(f"  Promedio litros/cliente:  {promedio_litros:.2f} L")
print(f"  Promedio venta/cliente:   ${promedio_pesos:.2f}")