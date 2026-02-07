ventas = [
    ("Ana", "Enero", "Laptop", 2, 15000),
    ("Luis", "Enero", "Mouse", 10, 250),
    ("Ana", "Febrero", "Laptop", 1, 15000),
    ("Luis", "Febrero", "Teclado", 5, 800),
    ("Ana", "Enero", "Mouse", 3, 250)
]

#total de ingresos por empleado
ingresos_empleado = {}

#productos únicos
productos_unicos = set()

#total de ingresos por mes
ingresos_mes = {}

for empleado, mes, producto, cantidad, precio in ventas:
    total = cantidad * precio
    ingresos_empleado[empleado] = ingresos_empleado.get(empleado, 0) + total
    productos_unicos.add(producto)
    ingresos_mes[mes] = ingresos_mes.get(mes, 0) + total

#empleado con mayores ingresos
empleado_mayor = max(ingresos_empleado, key=ingresos_empleado.get)

print("Ingresos por empleado:", ingresos_empleado)
print("Productos únicos vendidos:", productos_unicos)
print("Ingresos por mes:", ingresos_mes)
print("Empleado con mayores ingresos:", empleado_mayor)
