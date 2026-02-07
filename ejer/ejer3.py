inventario = [
    {"producto": "Laptop", "categoria": "Electrónica", "stock": 5},
    {"producto": "Mouse", "categoria": "Electrónica", "stock": 25},
    {"producto": "Silla", "categoria": "Muebles", "stock": 2},
    {"producto": "Escritorio", "categoria": "Muebles", "stock": 0}
]

#diccionario categoría - lista de productos
categoria_productos = {}

#conjunto de productos agotados
productos_agotados = set()

#lista temporal para stock < 5
stock_bajo = []

#contador por categoría
total_por_categoria = {}

for item in inventario:
    producto = item["producto"]
    categoria = item["categoria"]
    stock = item["stock"]

#categoría productos
    categoria_productos.setdefault(categoria, []).append(producto)

#productos agotados
    if stock == 0:
        productos_agotados.add(producto)
#stock menor a 5
    if stock < 5:
        stock_bajo.append(producto)

#total por categoría
    total_por_categoria[categoria] = total_por_categoria.get(categoria, 0) + 1

#convertir a tupla
stock_bajo_tupla = tuple(stock_bajo)

print("Categoría - Productos:")
print(categoria_productos)

print("\nProductos agotados:")
print(productos_agotados)

print("\nProductos con stock menor a 5:")
print(stock_bajo_tupla)

print("\nTotal de productos por categoria:")
print(total_por_categoria)
