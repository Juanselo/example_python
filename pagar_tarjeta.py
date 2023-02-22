# ejercicio pagar con tarjeta
cliente = str ("Juan")
numero_tarjeta = int ("78452114566")
saldo_disponible = float (4521284.44)
saldo_deposito = float (452.9)
saldo_restante = (saldo_disponible-saldo_deposito)

print ("el numero de tarjeta es:")
print (numero_tarjeta)
print ("Bienvenido", cliente)
print ("La cantidad de dinero que tienes es de: $",saldo_disponible)
print ("Vas a retirar : $",saldo_deposito)
print ("Tu cuenta quedó con : $",saldo_restante)