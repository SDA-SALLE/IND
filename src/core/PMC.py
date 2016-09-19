# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

import os
from excelmatriz import *
from wcsv import *
import json


def listaCSV(direccion):
   	#Variable para la ruta al directorio
	path = os.path.join(direccion,'')
	#print direccion

	#Lista vacia para incluir los ficheros
	lstFilesEmissions = []

	#Lista con todos los ficheros del directorio:
	lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
	datos = {}

	#Crea una lista de los ficheros que existen en el directorio y los incluye a la lista.
	for root, dirs, files in lstDir:
	    for fichero in files:
	        (nombreFichero, extension) = os.path.splitext(fichero)
	        if(extension == '.csv'):
	        	lstFilesEmissions.append(nombreFichero+extension)

	return lstFilesEmissions

def pmc(archivePM10, year): 
	archivePM10 = archivePM10
	archivePM25 = archivePM10.replace('PM10', 'PM25')

	MPM25 = convertCSVMatrizPoint(archivePM25)
	MPM10 = convertCSVMatrizPoint(archivePM10)

	head = MPM25[0,:]

	JPM25 = {}
	JPM10 = {}
	index = 0

	for value in head: 
		if value == 'ROW': 
			colROW = index
		if value == 'COL':
			colCOL = index
		if value == 'LAT': 
			colLAT = index
		if value == 'LON': 
			colLON = index
		if value == 'POLNAME': 
			colPOL = index
		if value == 'UNIT':
			colUNIT = index
		if value == 'ID':
			colID = index
		index += 1 

	for i in range(1, MPM10.shape[0]):
		if JPM10.get(MPM10[i][colID]) is None:
			JPM10[MPM10[i][colID]] = {'ROW': MPM10[i][colROW], 'COL': MPM10[i][colCOL], 'LAT': MPM10[i][colLAT], 'LON': MPM10[i][colLON], 'POLNAME':MPM10[i][colPOL], 'UNIT': MPM10[i][colUNIT], 'hour': {}}
		hour = 0
		for x in range(colUNIT+1, MPM10.shape[1]):
			JPM10[MPM10[i][colID]]['hour'][hour] = float(MPM10[i][x])
			hour += 1

	for i in range(1, MPM25.shape[0]):
		if JPM25.get(MPM25[i][colID]) is None:
			JPM25[MPM25[i][colID]] = {'ROW': MPM25[i][colROW], 'COL': MPM25[i][colCOL], 'LAT': MPM25[i][colLAT], 'LON': MPM25[i][colLON], 'POLNAME':MPM25[i][colPOL], 'UNIT': MPM25[i][colUNIT], 'hour': {}}
		hour = 0
		for x in range(colUNIT+1, MPM25.shape[1]):
			JPM25[MPM25[i][colID]]['hour'][hour] = float(MPM25[i][x])
			hour += 1


	for ID in JPM25:
		for hour in JPM25[ID]['hour']:
			operation = (JPM10[ID]['hour'][hour] - JPM25[ID]['hour'][hour]) / 3600
			JPM25[ID]['hour'][hour] = operation

	PMC(JPM25, 'PMC', year)

def testingpmc(folder):
	List = listaCSV(folder)
	listPMC = []
	for archive in List:
		if 'PMC' in archive:
			listPMC.append(archive)
	for name in listPMC: 
		MPMC = convertCSVMatrizPoint(folder + name)
		
		head = MPMC[0,:]
		
		index = 0
		
		for value in head: 
			if value == 'UNIT':
				colUNIT = index
			index += 1
		
		for  i in range(1, MPMC.shape[0]):
			for x in range(colUNIT+1, MPMC.shape[1]):
				
				number = float(MPMC[i][x])
				
				if  number < 0 or number < 0.0: 
					print 'Review process number <0'
					#pass
				elif number > 0 or number > 0.0: 
					pass
					#print 'Review process number <0'