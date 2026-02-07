asistencias = [
    ("Matemáticas", "Juan", "2024-09-01"),
    ("Matemáticas", "Ana", "2024-09-01"),
    ("Física", "Juan", "2024-09-01"),
    ("Matemáticas", "Juan", "2024-09-02"),
    ("Física", "Ana", "2024-09-02")
]

asignatura_alumnos = {}
asistencias_alumno = {}

for asignatura, alumno, fecha in asistencias:

#asignatura
    if asignatura not in asignatura_alumnos:
        asignatura_alumnos[asignatura] = set()
    asignatura_alumnos[asignatura].add(alumno)

#alumno
    if alumno not in asistencias_alumno:
        asistencias_alumno[alumno] = set()
    asistencias_alumno[alumno].add(fecha)

#contar días distintos por alumno
dias_por_alumno = {}
for alumno in asistencias_alumno:
    dias_por_alumno[alumno] = len(asistencias_alumno[alumno])

#alumno con más asistencias
alumno_mayor = max(dias_por_alumno, key=dias_por_alumno.get)

print("Asignatura - Alumnos:")
print(asignatura_alumnos)

print("\nDías distintos por alumno:")
print(dias_por_alumno)

print("\nAlumno con mayor asistencia:")
print(alumno_mayor)
