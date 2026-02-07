#declaracion de variables
#str
texto:str = ""
##numero entero
entero:int = 10
#los decimales
flotante:float = 1.5
#booleano
booleano:bool = True

#para imprimir texto
print("hola mundo")
#imprecion de variable
print(texto,entero)
#impresion con escape de variable
print(f"este es el valor de una variable: {flotante}")
print("este es un texto", booleano)
#funciones adicionales de print
#rellena los espacios sobrantes que deceas
print("menu de usuario".center(25,"-"))
#end es para laterminacion
print("texto de prueba",end=".")
print("texto de prueba",end=".")

#impresion de tipo de dato
print(type(texto))
print(type(entero))
print(type(flotante))
print(type(booleano))

#impresion de memoria
print(id(texto))
print(id(entero))
print(id(flotante))
print(id(booleano))


#ESTRUCTURA DE CONTROL
if entero > 0 and entero < 100:
    if entero  < 100:
        print("esta dentro del rango")
    else:
        print("esta fuera del rango")
    print("es mayor")
else:
    print("es menor")
#elif entero < 0:

#ciclos de repeticion 
#inicio ,final, incremento
for i in range(5,31,5):
    print (i,end=",")
    
for letra in texto:
    print(letra)
    
#ciclo  de repeticion while
contador = 0
while  contador <=5:
    print("Bucle infinito")
    contador += 1
   """  if contador >= 5:
        break """
    
#lista
lista_frutas:list = []
lista_alterna:list = list()
#imprecion de una lista
print(lista_alterna)
print(lista_frutas)
#imprecion tipo dato
print(type(lista_alterna))
print(type(lista_frutas))

#funciones de las listas
lista_frutas.append("manzana")
lista_frutas.append("uva")
lista_frutas.append("mandarina")
#contar elementos de una lista con la funcion len()
print(len(lista_frutas))
#insercion de un elemento con la funcion insert()
#requiere una posicion y un valor
lista_frutas.insert(1,"pera")
#eliminar el ultimo registro de una lista con la funcion pop()
print(lista_frutas.pop())
#remover un elemento de una lista con la funcion remove()
lista_frutas.remove("manzana")
#limpia una lista con la funcion clear()
lista_frutas.clear()
#eliminar una lista
del lista_frutas

print(lista_frutas)
#recorrer una lista
for i in lista_frutas:
    print(i,end=",")
#recorrer una lista con for normal
for i in range(len(lista_frutas)):
    print(lista_frutas[i])

#imprecion de una posicion
    print(lista_frutas[0])
#cambiar valor de una posicion
lista_frutas[1] = "naranja"
print(lista_frutas)
#cambiar valor de una posicion
lista_frutas[1] = "naranja"
lista_frutas.append("manzana")
lista_frutas.append("uva")
lista_frutas.append("mandarina")
print(lista_frutas[-2:])

#tuplas no son mutables (no se puden cambiar sus valores)
tupla_nombres =("Lorena","Isabel","Ana")
tupla_alterna = tuple()
#imprimir tipo de dato
print(type(tupla_nombres))
print(type(tupla_alterna))
#impresion total
print(tupla_nombres)
#impresion por posicion 
print(tupla_nombres[2])
#impresion total por iteracion
for nombre in tupla_nombres:
    print(nombre)
#borrado de una tupla
#del tupla_nombres
print(tupla_nombres)



#coleccion set
coleccion = {'tierra','marte','jupiter','saturno'}
coleccion_alterna = set()
#impresion de tipo de dato
print(type(coleccion))
print(type(coleccion_alterna))
#imprimir todos los elemtos
print(coleccion[1])
#añadir nuevos elemtos a una coleccion
coleccion.add('mercurio')
#añadir elementos nuevos de otra coleccion 
coleccion.update(lista_frutas)
coleccion.update(tupla_nombres)
#eliminar un elemeto
coleccion.remove('pluton')
#descartar un elemento
coleccion.discard('pluton')
#limpia todo el contenido de una coleccion
coleccion.clear()
print(coleccion)


#diccionarios
diccionario = {"nombre":"diego","carrera":"sis"}
diccionario_alterno = dict()

#impresion de tipo de dato
print(type(diccionario))
print(type(diccionario_alterno))
#mostrar un elemento especifico por medio de su key
print(diccionario['carrera'])
#editar una key del diccionario
diccionario["nombre"]="diego"
#añadir nuevos elementos
diccionario["semestre"]="8"

print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())

for valor in diccionario.values():
    print(f"la key es: {key},el valor es:{valor} ")
#impresion general
print(diccionario)






#funciones

#funcion sensilla
def test():
    print("impresion desde funccion")

#invocacion de una funcion 
test()
#funcion con argumento
def test2(nombre):
    print(f"Hola,  {nombre}")
test2("diego")

