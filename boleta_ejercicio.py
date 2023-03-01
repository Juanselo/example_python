print ("Bienvenido, escoja la boleta según su localidad para saber su precio")

opciones = """
Localidades
1- VIP 
2- Preferencial
3- General
4- Baja
"""
print(opciones)

opcion = int (input("Escoger una opción del 1 al 4: "))

if opcion is 1:
    print("Precio $500")
elif opcion is 2: 
    print("Precio $400")
elif opcion is 3:
    print("Precio $200")
elif opcion is 4: 
    print ("Precio $100")

