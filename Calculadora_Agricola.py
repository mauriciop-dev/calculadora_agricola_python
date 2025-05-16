print("🌾 Calculadora de costos agrícolas 🌾")
print("--------------------------------------")

# 1. Solicitar tamaño del terreno en hectáreas
hectareas = float(input("Ingresa el tamaño del terreno (en hectáreas): "))

# 2. Crear una lista vacía para los insumos
insumos = []

print("\n✅ Ahora vamos a ingresar los insumos (escribe 'fin' para terminar)\n")
while True:
    nombre = input("Nombre del insumo (o escribe 'fin' para terminar): ").strip()
    
    if nombre.lower() == 'fin':
        break

    costo_unitario = float(input(f"Costo por unidad de {nombre} ($): "))
    cantidad_por_hectarea = float(input(f"Cantidad necesaria por hectárea de {nombre}: "))

    # Guardamos los datos en un diccionario
    insumo = {
        "nombre": nombre,
        "costo_unitario": costo_unitario,
        "cantidad_por_hectarea": cantidad_por_hectarea
    }

    # Agregamos el diccionario a la lista
    insumos.append(insumo)

    print(f"✅ Insumo '{nombre}' agregado.\n")
print(insumos)

print("\n📊 Resumen de costos")
print("---------------------")

costo_total_hectarea = 0

for insumo in insumos:
    costo = insumo["costo_unitario"] * insumo["cantidad_por_hectarea"]
    cantidad_total = insumo["cantidad_por_hectarea"] * hectareas
    costo_total_hectarea += costo

    print(f"- {insumo['nombre']}:")
    print(f"   • ${costo:.2f} por hectárea")
    print(f"   • Debe comprar {cantidad_total:.2f} unidades en total")


costo_total_general = costo_total_hectarea * hectareas

print("\n💵 Costo total por hectárea: ${:.2f}".format(costo_total_hectarea))
print("🌍 Costo total para {:.2f} hectáreas: ${:.2f}".format(hectareas, costo_total_general))

# Crear el archivo de salida con detalles mejorados
with open("resumen_costos.txt", "w", encoding='utf-8') as archivo:
    archivo.write("📊 Resumen de costos agrícolas\n")
    archivo.write("--------------------------------------\n")
    archivo.write(f"Tamaño del terreno: {hectareas:.2f} hectáreas\n\n")

    for insumo in insumos:
        costo = insumo["costo_unitario"] * insumo["cantidad_por_hectarea"]
        cantidad_total = insumo["cantidad_por_hectarea"] * hectareas

        archivo.write(f"- {insumo['nombre']}:\n")
        archivo.write(f"   • ${costo:.2f} por hectárea\n")
        archivo.write(f"   • Debe comprar {cantidad_total:.2f} unidades en total\n")

    archivo.write(f"\n💵 Costo total por hectárea: ${costo_total_hectarea:.2f}\n")
    archivo.write(f"🌍 Costo total para {hectareas:.2f} hectáreas: ${costo_total_general:.2f}\n")

print("\n📝 El resumen también fue guardado en 'resumen_costos.txt'")
