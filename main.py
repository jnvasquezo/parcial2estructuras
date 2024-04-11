# main.py

class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre

# Definir las ciudades
madrid = Ciudad("Madrid")
toledo = Ciudad("Toledo")
segovia = Ciudad("Segovia")
avila = Ciudad("Avila")
guadalajara = Ciudad("Guadalajara")

# Solicitar la cantidad de pasajeros en cada ciudad
pasajeros_por_ciudad = {}
for ciudad in [madrid, toledo, segovia, avila]:
    pasajeros_por_ciudad[ciudad] = int(input(f"Ingrese el número de pasajeros en {ciudad.nombre}: "))

# Ordenar las ciudades por cantidad de pasajeros
ciudades_ordenadas = sorted(pasajeros_por_ciudad, key=pasajeros_por_ciudad.get)

# Planificar la ruta del autobús
ruta_autobus = []
capacidad_autobus = 15
pasajeros_recogidos = 0

for ciudad in ciudades_ordenadas:
    pasajeros_en_ciudad = pasajeros_por_ciudad[ciudad]
    if pasajeros_recogidos + pasajeros_en_ciudad <= capacidad_autobus:
        ruta_autobus.append((ciudad, pasajeros_en_ciudad))
        pasajeros_recogidos += pasajeros_en_ciudad
    else:
        pasajeros_a_recoger = capacidad_autobus - pasajeros_recogidos
        ruta_autobus.append((ciudad, pasajeros_a_recoger))
        pasajeros_recogidos += pasajeros_a_recoger
        break  # El autobús está lleno, detener la recogida de pasajeros

# Imprimir la ruta del autobús
print("Ruta del autobús:")
for ciudad, pasajeros in ruta_autobus:
    print(f"De {ciudad.nombre} recoger {pasajeros} pasajeros.")

# Simular el viaje del autobús
print("\nSimulando el viaje del autobús...")
for i in range(len(ruta_autobus) - 1):
    origen, destino = ruta_autobus[i][0], ruta_autobus[i + 1][0]
    pasajeros_recogidos = ruta_autobus[i][1]
    print(f"De {origen.nombre} a {destino.nombre}, recoger {pasajeros_recogidos} pasajeros.")

# Última parada en Guadalajara
ultima_parada = ruta_autobus[-1][0]
print(f"Llegada a {ultima_parada.nombre}.")

# Verificar si quedaron pasajeros pendientes por recoger
pasajeros_pendientes = sum(pasajeros_por_ciudad.values()) - pasajeros_recogidos
if pasajeros_pendientes > 0:
    print(f"\nQuedaron {pasajeros_pendientes} pasajeros pendientes por recoger en otras ciudades:")
    for ciudad, pasajeros in pasajeros_por_ciudad.items():
        if pasajeros > 0:
            print(f"{pasajeros} pasajeros en {ciudad.nombre}.")
