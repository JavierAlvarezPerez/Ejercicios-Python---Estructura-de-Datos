partidas = [
    ("Alex", "Bosque", 120),
    ("Luis", "Desierto", 90),
    ("Alex", "Bosque", 150),
    ("Ana", "Ciudad", 200),
    ("Luis", "Bosque", 110)
]

#total de puntos por jugador
puntos_jugador = {}

#conjunto de mapas jugados
mapas_jugados = set()

#para promedio: jugador - [suma_puntos, partidas]
promedio_aux = {}

#total de puntos por mapa
puntos_mapa = {}

for jugador, mapa, puntos in partidas:

#total por jugador
    puntos_jugador[jugador] = puntos_jugador.get(jugador, 0) + puntos

#mapas
    mapas_jugados.add(mapa)

#promedio
    if jugador not in promedio_aux:
        promedio_aux[jugador] = [0, 0]
    promedio_aux[jugador][0] += puntos
    promedio_aux[jugador][1] += 1

#puntos por mapa
    puntos_mapa[mapa] = puntos_mapa.get(mapa, 0) + puntos

#calcular promedio final
promedio_jugador = {}
for jugador in promedio_aux:
    suma, cantidad = promedio_aux[jugador]
    promedio_jugador[jugador] = suma / cantidad

#mapa con más puntos
mapa_mas_puntos = max(puntos_mapa, key=puntos_mapa.get)

print("Total de puntos por jugador:")
print(puntos_jugador)

print("\nMapas jugados:")
print(mapas_jugados)

print("\nPromedio de puntos por jugador:")
print(promedio_jugador)

print("\nMapa con más puntos:")
print(mapa_mas_puntos)
