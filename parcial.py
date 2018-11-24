import os
import sys
from string import Template

filein = open("Template/style.html")
src= Template(filein.read())

print("Programa que acepta datos de estudiantes")

mat = input("Ingresa la matricula")
nom = input("Ingrese el nombre")

notas = []
continuar = True
while(continuar):
	cal = input("Ingresa la nota: ")
	notas.append(cal)
	stop = input("Escribe 'ya' si ya no quieres mas calificaciones o enter para continuar agregando calificaciones")
	if (stop == 'ya'):
		continuar = False

n = str(notas)
d = {'nom':nom, 'mat':mat, 'n':n}

result= src.substitute(d)

if(os.path.isdir("Calificaciones") == False):
	os.mkdir("Calificaciones")
filein2 = open('Calificaciones/'+str(mat)+'.html', 'w')
filein2.writelines(result)
filein2.close()

print("Tus datos han sido agregados")

while True:
	pregunta= input("Presione 'C' para agregar otro usuario y 'Y' para salir ")
	if(pregunta == 'C'):
		os.system(r"parcial.py")
	elif(pregunta == 'Y'):
		sys.exit()


