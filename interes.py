interest = float (input("Establecer interes anual:"))
period = float (input ("Vida de la hipoteca:"))
value = float (input ("Cantidad de dinero prestado:"))
monthly_payments = (((interest/100)*value+value)/(period*12))
print (f"Tu pago mensual es de: {monthly_payments}")