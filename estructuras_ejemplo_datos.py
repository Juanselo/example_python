""" "accion = "ingresé al evento"
accion2 = "Registrado al evento" """

#estructura de control (condicional if o si)
#permite continuar un flujo (realizar algo) si se cumple una condicion
# de no cumplirse, hacer o no hacer.
# esta sentencia (condicional if) va acompañado de los operadores de abajo.
""""
if estructura_datos_uno <  estructura_datos_dos
if estructura_datos_uno <=  estructura_datos_dos
if estructura_datos_uno >  estructura_datos_dos
if estructura_datos_uno >=  estructura_datos_dos
if estructura_datos_uno ==  estructura_datos_dos
if estructura_datos_uno !=  estructura_datos_dos
"""

#Varias maneras de utilizar la sentencia if
#if simple, #if compuesto, #if anidado

"""dato_comparacion = 18
edad = 20
boleta = True
fecha_evento = "27-02-2023"
fecha_comparacion = "27-02-2023"
"""
#if simple+
"""if edad >= dato_comparacion:
    print ("bienvenido")
"""
#if compuesto
""""
if edad >= dato_comparacion:
    print ("bienvenido")
else:
    print ("Ingreso no autorizado")"""

#if anidado
"""if edad >= dato_comparacion and boleta and fecha_evento == fecha_comparacion:
    print ("bienvenido")
else:
    print ("Ingreso no autorizado")
"""
    #switch

"""
menu = """
"""menu
1- M_numero
2- M_texto
3- M_signos
4- M_numero_usado

print(menu)

op = int(input("toma un caso"))

if op is 1:
    print (545)
elif op is 2:
    print ("ksajjad")
"""

print ("Bienvenido, escoja la boleta según su localidad para saber su precio")

opciones = """
Localidades
1- VIP 
2- Preferencial
3- General
4- Baja
"""
print(opciones)

opcion = int (input("Escoger una opción "))

if opcion is 1:
    print("Precio $500")
elif opcion is 2: 
    print("Precio $400")
elif opcion is 3:
    print("Precio $200")
elif opcion is 4: 
    print ("Precio $100")


