class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = {}

    def agregar_vecino(self, ciudad, peso):
        self.vecinos[ciudad] = peso

    def obtener_vecinos(self):
        return self.vecinos.keys()

    def obtener_peso(self, ciudad):
        return self.vecinos[ciudad]


class Grafo:
    def __init__(self):
        self.ciudades = {}

    def agregar_ciudad(self, nombre):
        if nombre not in self.ciudades:
            ciudad = Ciudad(nombre)
            self.ciudades[nombre] = ciudad

    def obtener_ciudad(self, nombre):
        return self.ciudades.get(nombre)

    def agregar_conexion(self, origen, destino, peso):
        if origen in self.ciudades and destino in self.ciudades:
            self.ciudades[origen].agregar_vecino(self.ciudades[destino], peso)
            self.ciudades[destino].agregar_vecino(self.ciudades[origen], peso)


# Crear el grafo con las conexiones entre ciudades y sus pesos
def crear_grafo():
    grafo = Grafo()

    grafo.agregar_ciudad("Madrid")
    grafo.agregar_ciudad("Toledo")
    grafo.agregar_ciudad("Segovia")
    grafo.agregar_ciudad("Avila")
    grafo.agregar_ciudad("Guadalajara")

    grafo.agregar_conexion("Madrid", "Toledo", 72.5)
    grafo.agregar_conexion("Madrid", "Segovia", 91.6)
    grafo.agregar_conexion("Toledo", "Segovia", 159)
    grafo.agregar_conexion("Segovia", "Avila", 64.3)
    grafo.agregar_conexion("Segovia", "Guadalajara", 153)
    grafo.agregar_conexion("Avila", "Guadalajara", 171)
    grafo.agregar_conexion("Madrid", "Guadalajara", 66.6)
    grafo.agregar_conexion("Avila", "Toledo", 133)
    grafo.agregar_conexion("Avila", "Madrid", 102)

    return grafo
