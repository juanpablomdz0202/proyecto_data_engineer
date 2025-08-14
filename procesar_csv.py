import csv
#1.Leer el archivo csv
with open("personas.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    datos = list(lector) #Lo guardamos como lista de diccionario

#2.Limpiar datos (quedarnos solo con edades numericas)
datos_limpios = []
for fila in datos:
    try:
        edad = int(fila["edad"])
        datos_limpios.append({"nombre":fila["nombre"], "edad": edad})
    except ValueError:
        print(f"Edad ivalida para {fila['nombre']}:{fila['edad']}")   
        
#3.Calcular estadisticas
edades = [p["edad"] for p in datos_limpios]
edad_min = min(edades)
edad_max = max(edades)
edad_promedio = sum(edades) / len(edades)

#4.Mostrar resultados
print("estadisticas de edades:")
print(f"Edad minima:{edad_min}")
print(f"Edad maxima{edad_max}")
print(f"Edad promedio{edad_promedio:.2f}")

#5. Guardar datos limpios en un nuevo csv
with open("personas_limpias.csv", "w", newline="", encoding="utf-8") as archivo:
    campos = ["nombre", "edad"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(datos_limpios)

print("Archivo 'personas_limpias.csv' creado con exito")    