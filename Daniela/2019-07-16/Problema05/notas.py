# print()
archivo = open("notas.txt")

aprobados = 0
reprobados = 0
rango1 = 0
rango2 = 0
rango3 = 0
rango4 = 0
rango5 = 0
rango6 = 0

i = 0
linea = archivo.readline()
while linea != "":
    i = i + 1
    
    lista = linea.split(';')
    alumno = lista[0]
    nota = lista[1]

    numero = float(nota)
    if numero >= 4.0:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1

    if   numero >= 1.0 and numero <= 1.9:
        rango1 = rango1 + 1
    elif numero >= 2.0 and numero <= 2.9:
        rango2 = rango2 + 1 
    elif numero >= 3.0 and numero <= 3.9:
        rango3 = rango3 + 1 
    elif numero >= 4.0 and numero <= 4.9:
        rango4 = rango4 + 1 
    elif numero >= 5.0 and numero <= 5.9:
        rango5 = rango5 + 1 
    elif numero >= 6.0 and numero <= 70:
        rango6 = rango6 + 1 

    linea = archivo.readline()

archivo.close()

total = i

print("Total = ", total)
print("Aprobados  = ", round(aprobados/total*100, 1), "%")
print("Reprobados  = ", round(reprobados/total*100, 1), "%")

print("Notas entre 1.0 y 1.9 = ", rango1, "(", round(rango1/total*100, 1), "%)")
print("Notas entre 2.0 y 2.9 = ", rango2, "(", round(rango2/total*100, 1), "%)")
print("Notas entre 3.0 y 3.9 = ", rango3, "(", round(rango3/total*100, 1), "%)")
print("Notas entre 4.0 y 4.9 = ", rango4, "(", round(rango4/total*100, 1), "%)")
print("Notas entre 5.0 y 5.9 = ", rango5, "(", round(rango5/total*100, 1), "%)")
print("Notas entre 6.0 y 7.0 = ", rango6, "(", round(rango6/total*100, 1), "%)")
