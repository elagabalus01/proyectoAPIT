# -*- coding: utf-8 -*-

#Programa hecho por Donovan Riaño Enriquez, APIT 2021-2

import fitz #para leer pdf
from collections import Counter #para conteo palabras
import nltk #natutal language toolkit Python
from nltk.tokenize import sent_tokenize
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import *
import json
import pandas as pd
import numpy as np


#Función para leer papers de los tres idiomas
def readDocument(choose):
	if choose == 1:
		pdf_document = "papers/paper.pdf"
		doc = fitz.open(pdf_document)
		chooseDoc(doc)
	if choose == 2:
		pdf_document = "papers/Modul_uno_de_derecho_empresarial.pdf"
		doc = fitz.open(pdf_document)
		chooseDoc(doc)
	if choose == 3:
		pdf_document = "papers/Capítulo_234_Exploración_física_del_aparato_cardiovascular.pdf"
		doc = fitz.open(pdf_document)
		chooseDoc(doc)

#Función para leer de que página a que página leerá del documento
def chooseDoc(doc):
	print("Selecciona el parámetro de páginas que léeras")

	a = input('Ingresa el inicio de las páginas a analizar: \n-->')
	a = int (a) - 1
	b = input('Ingresa el fin de las páginas a analizar: \n-->')
	b = int (b)

	#For con el inicio y fin de las páginas seleccionadas
	for i in range (a,b):
		page1 = doc.loadPage(i)
		page1text = page1.getText("text")
		count(page1text,i)
		print ("\n\n\n==============================Texto Página==============================\n\n\n")
		print(page1text)#Si quitas este pront, ya no imprime por hoja
		#return i

#Insertion sort es un algoritmo ávido para el ordenamiento de listas
#Función para ordenar por orden Alfabético de menor a mayor
def insertionSortAlf(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

#Función para ordenar por orden Alfabético de mayor a menor
def insertionSortMayor(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key > arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key


def count(page1text, i):
	lista = []
	datos = {}
	listaParseo=page1text.split()
	interception(listaParseo)
	kindSort = int(input("Ingresa el tipo de ordenamiento que necesitas: \n1.Alfabético, 2.Alfabético de Mayor a menor, 3. Por claves menor, 4. Por claves mayor\n-->"))
	if kindSort == 1:
		print(' ---------------------------------------------------')
		print('|               Página Seleccionada '+str(i)+'              |')
		print(' ---------------------------------------------------')

		#Ordena por orden alfabético de manera ávida
		insertionSortAlf (listaParseo)
		frecuencia = nltk.FreqDist(listaParseo)
		for key,val in frecuencia.items():
			print (str(key) + ':' + str(val))

			#Este bloque se supone que divide por la cantidad de letras de cada elemento de la lista
			#Pero se buggea por cada item y no lo imprime
			"""
			kindNGrama = int(input("Ingresa el tipo de n-grama que necesitas: \n1.Mono, 2.Bi, 3. Tri\n-->"))
			for j in range(0,len(key)):
			    #print (cadena [i])
				palabra = key[j]
			    #print (palabra)

				if kindNGrama == 1:
					cadenaGrama = palabra[:1].replace(' ','')
					freqMono = nltk.FreqDist(cadenaGrama)
					print (str(cadenaGrama) + ':' + str(freqGrama))
					#print (cadenaGrama)
				if kindNGrama == 2:
					cadenaGrama = palabra[:1].replace(' ','')
					freqGrama = nltk.FreqDist(cadenaGrama)
					print (str(cadenaGrama) + ':' + str(freqGrama))
					#print (cadenaGrama)
				if kindNGrama == 3:
					cadenaGrama = palabra[:1].replace(' ','')
					freqGrama = nltk.FreqDist(cadenaGrama)
					print (str(cadenaGrama) + ':' + str(freqGrama))
					#print (cadenaGrama)
			#print(sent_tokenize(page1text))"""

			#Se pretende alojar en UTF-8 los valores para guardarlos en un json y posteriormente
			#y graficarlos con Matplotlib
			"""
			datos = {
				key : val,
			}
			with open ('valores/spanish.json', 'w') as file:
				json.dump (datos, file)"""

		#graficacion (key, val)
		#return key, val
		count_n_gram(key,2)

	if kindSort == 2:
		print(' ---------------------------------------------------')
		print('|               Página Seleccionada '+str(i)+'              |')
		print(' ---------------------------------------------------')

		#Ordena por orden alfabético de manera ávida
		insertionSortMayor (listaParseo)
		frecuencia = nltk.FreqDist(listaParseo)
		for key,val in frecuencia.items():
			print (str(key) + ':' + str(val))
			#print(sent_tokenize(page1text))
		#graficacion (key, val)
		#return key, val

	if kindSort == 3:
		print(' ---------------------------------------------------')
		print('|               Página Seleccionada '+str(i)+'              |')
		print(' ---------------------------------------------------')

		#Ordena por orden alfabético de manera ávida
		frecuencia = nltk.FreqDist(listaParseo)
		insertionSortMayor (frecuencia)
		for key,val in frecuencia.items():
			print (str(key) + ':' + str(val))
			#print(sent_tokenize(page1text))
		#graficacion (key, val)
		#return key, val
	if kindSort == 4:
		print(' ---------------------------------------------------')
		print('|               Página Seleccionada '+str(i)+'              |')
		print(' ---------------------------------------------------')

		#Ordena por orden alfabético de manera ávida
		frecuencia = nltk.FreqDist(listaParseo)
		insertionSortAlf (frecuencia)
		for key,val in frecuencia.items():
			print (str(key) + ':' + str(val))
			#print(sent_tokenize(page1text))
		#graficacion (key, val)
		#return key, val



def interception(listaParseo):
	glosario = pd.read_csv('glosario.csv')
	ing = glosario['Area1']
	salud = glosario['Area2']
	sociales = glosario['Area3']
	artes = glosario['Area4']

	if (listaParseo !=[]):
		interIng = set (ing).intersection(listaParseo)
		interSalud = set (salud).intersection(listaParseo)
		interSociales = set (sociales).intersection(listaParseo)
		interArtes = set (artes).intersection(listaParseo)
		interAll = set (interIng).intersection(interSalud).intersection(interSociales).intersection(interArtes)

		if (len(interIng)!=0):
			print("Las coincidencias del área 1 son:")
			print ("-->"+ str(interIng))

		if (len(interSalud)!=0):
			print("Las coincidencias del área 2 son:")
			print ("-->"+ str(interSalud))

		if (len(interSociales)!=0):
			print("Las coincidencias del área 3 son:")
			print ("-->"+ str(interSociales))

		if (len(interArtes)!=0):
			print("Las coincidencias del área 4 son:")
			print ("-->"+ str(interArtes))

		if (len(interAll)!=0):
			print("Las coincidencias de todas las áreas son:")
			print ("-->"+ str(interAll))

		if ((len(interIng) > len(interSalud)) and (len(interIng) > len(interSociales) and (len(interIng) > len(interArtes)))):
			maximo = len(interIng)
			print ("El área predominante es área 1 con: "+ str(maximo) + " elementos")
		if ((len(interSalud) > len(interIng)) and (len(interSalud) > len(interSociales) and (len(interSalud) > len(interArtes)))):
			maximo = len(interIng)
			print ("El área predominante es área 2 con: "+ str(maximo) + " elementos")
		if ((len(interSociales) > len(interIng)) and (len(interSociales) > len(interSalud) and (len(interSociales) > len(interArtes)))):
			maximo = len(interIng)
			print ("El área predominante es área 3 con: "+ str(maximo) + " elementos")
		if ((len(interArtes) > len(interIng)) and (len(interArtes) > len(interSalud) and (len(interArtes) > len(interSociales)))):
			maximo = len(interIng)
			print ("El área predominante es área 4 con: "+ str(maximo) + " elementos")

		graficacion(interIng, interSalud, interSociales, interArtes)




#Función en espera, aún falta por arreglar el bug de pasar todos los elementos
#Función de plot
def graficacion (interIng, interSalud, interSociales, interArtes):
	# plt.subplot(1,4,1)
	# plt.bar(['Ingeniería','Biológicas','Sociales','Humanidades'],[len(interIng),len(interSalud),
	len(interSociales),len(interArtes)])
	# p1 = plot(list(interIng),len(interIng), label = 'Gráfica área 1',color = 'blue')
	plt.ylabel("Palabras", fontsize=12)
	plt.legend()
	plt.grid(True)

	# plt.subplot(1,4,2)
	# p2 = plot(list(interSalud),len(interSalud), label = 'Gráfica área 2',color = 'orange')
	# plt.legend()
	# plt.grid(True)
	#
	# plt.xlabel("Cantidad de repeticiones", fontsize=12)
	#
	# plt.title("Gráfica Comparaciones repeticiones áreas conocimiento")
	#
	# plt.subplot(1,4,3)
	# p3 = plot(list(interIng),len(interSociales), label = 'Gráfica área 3',color = 'green')
	# plt.legend()
	# plt.grid(True)
	#
	# plt.subplot(1,4,4)
	# p3 = plot(list(interIng),len(interArtes), label = 'Gráfica área 4',color = 'purple')
	# plt.legend()
	# plt.grid(True)


	#plt.savefig("Sujeto16/Comparaciones/GraficaSubElectroSujeto16.jpg", bbox_inches = 'tight')

	plt.show()
	#fig.savefig("GraficaPidBub.png")"""

#Método main
def main ():
	choose = int(input("Ingresa el número del doc  que deseas leer: \n1.Ingenieria, 2.Derecho, 3.Medicina\n-->"))
	readDocument(choose)

#Sin el play, el programa no hace nada
main()
