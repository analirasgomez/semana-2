grade = float (input ("Nota del estudiante sobre 100:"))
assistance = int (input ("Clases atendidas: "))
classes = int (input ("Clases de la asignatura totales:"))
cgrade = int ((assistance/classes)*100)
if cgrade >= 80 and grade >=70 :
    print ("Aprobado")
else: 
    print ("Suspenso")