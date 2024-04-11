def encontrar_rutas_dfs(grafo, inicio, fin, ruta=[], visitado=set()):
    ruta = ruta + [inicio]
    visitado.add(inicio)

    if inicio == fin:
        return [ruta]
    
    rutas = []
    for vecino in grafo[inicio]:
        if vecino not in visitado:
            nuevas_rutas = encontrar_rutas_dfs(grafo, vecino, fin, ruta[:], visitado.copy())
            for nueva_ruta in nuevas_rutas:
                rutas.append(nueva_ruta)
    
    return rutas

def calcular_costo_total(grafo, ruta):
    costo_total = 0
    for i in range(len(ruta) - 1):
        ciudad_actual = ruta[i]
        siguiente_ciudad = ruta[i + 1]
        costo_total += grafo[ciudad_actual][siguiente_ciudad]
    return costo_total

if __name__ == "__main__":
    # Grafo de ciudades y distancias entre ellas
    grafo = {
        'Madrid': {'Toledo': 72.5, 'Segovia': 91.6, 'Guadalajara': 66.6},
        'Toledo': {'Madrid': 72.5, 'Segovia': 159.0},
        'Segovia': {'Madrid': 91.6, 'Toledo': 159.0, 'Avila': 64.3, 'Guadalajara': 153.0},
        'Avila': {'Segovia': 64.3, 'Guadalajara': 171.0},
        'Guadalajara': {'Madrid': 66.6, 'Segovia': 153.0, 'Avila': 171.0}
    }

    # Encontrar todas las rutas de Madrid a Guadalajara
    rutas = encontrar_rutas_dfs(grafo, 'Madrid', 'Guadalajara')

    # Imprimir las rutas y sus costos
    print("Todas las rutas de Madrid a Guadalajara:")
    for i, ruta in enumerate(rutas):
        costo = calcular_costo_total(grafo, ruta)
        print(f"Ruta {i+1}: {ruta}, Costo total: {costo} km")
