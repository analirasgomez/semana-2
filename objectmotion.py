#metemos los parametros 
posicion_inicial = float (input ("Posición inicial (m):")) 
velocidad_inicial = float (input ("Velocidad inicial (m/s):"))
aceleracion = float (input ("Aceleración (m/s^2):"))
tiempo = float (input ("Tiempo (s):"))

#calculamos la posicion final 
posicion_final = float (posicion_inicial + velocidad_inicial*tiempo + (1/2*aceleracion*tiempo**2))
print (f"La posicion final es {posicion_final} metros.")

#calculamos la velocidad final
velocidad_final = float (velocidad_inicial+aceleracion*tiempo)
print (f"La velocidad final es {velocidad_final} metros por segundo.")