# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

import os
import sys
import json
import math
sys.path.append('core')
from excelmatriz import * 
from wcsv import *

def emition(archive, YEAR): 

	#Read factors emissions
	''''
	Realizamos la lectura de los factores de emision ubicados en el archivo /data/in/EmissionFactors/EmissionsFactors.xlsx
	Es necesario, respetar los nombres dentro del archivo.
	Entra a esta función el archivo y utilizamos la funcion convertir xlsx a csv para cargarlo como matriz
	'''''

	archiveEmissions = os.path.join('..', 'data', 'in', 'EmissionsFactors', 'EmissionFactors.xlsx')
	matriz = convertXLSCSV(archiveEmissions)

	EmissionFactors = {}
	for i in range(1, matriz.shape[0]):
		category = matriz[i][0]
		
		if EmissionFactors.get(category) is None: 
			EmissionFactors[category] = {}

		for x in range(1, matriz.shape[1]):
			pollname = matriz[0][x]

			if EmissionFactors[category].get(pollname) is None:
				EmissionFactors[category][pollname] = float(matriz[i][x])

	matriz = None
	matriz = convertXLSCSV(archive)

	head = matriz[0,:]
	index = 0

	for value in head: 
	 	if value == 'LAT':
	 		colLAT = index
	 	if value == 'LON':
	 		colLON = index
	 	if value == 'ROW':
	 		colROW = index
	 	if value == 'COL':
	 		colCOL = index
	 	if value == 'ID' or value ==  'id':
	 		colID = index
	 	if value == 'S_TYPE' or value == 'SOURCETYPE':
	 		colSOURCETYPE = index
	 	if value == 'CIUU':
	 		colCIUU = index
	 	if value == 'FUEL_TYPE':
	 		colFUELTYPE = index		
	 	if value == 'CATEGORY':
	 		colCATEGORY = index
	 	if value == 'GROW RATE' or value == 'GROWRATE':
	 		colGROWRATE = index
	 	if value == 'BASE_FUEL':
	 		colBASEFUEL = index
	 	if value == 'PROYECTED_FUEL':
	 		colPROYECTEDFUEL = index
	 	if value == 'FUEL UNIT':
	 		colFUELUNIT = index
	 	if value == 'VOC RM' or value == 'VOCRM':
	 		colVOCRM = index
	 	if value == 'VOCFE' or value == 'VOC FE': 
	 		colVOCFE = index
	 	if value == 'YEAR':
	 		colYEAR = index
	 	index += 1

	data = {}
	for i in range(1, matriz.shape[0]):
	 	ID = matriz[i][colID]
	 	if data.get(ID) is None:
	 		data[ID] = {} 
	 		data[ID]['base'] = {'LAT': [], 'LON': [], 'ROW': [], 'COL': [], 'SOURCETYPE': [], 'CIUU': [], 'FUELTYPE': [], 'CATEGORY': [], 'GROWRATE': [], 'BASEFUEL': [], 'PROYECTEDFUEL': [], 'FUELUNIT': [], 'VOCRM': [], 'VOCFE': [], 'YEAR': []}
	 		data[ID]['results'] = {}
	 	
	 	entryResults = data[ID]['results']
 		category = EmissionFactors.keys()
 		Pollutants = EmissionFactors[category[0]].keys()
 		for pollutant in Pollutants: 
  			if entryResults.get(pollutant) is None:
  				entryResults[pollutant] = []

	 	if data[ID]['base']['LAT'] == []:
	 		data[ID]['base']['LAT'].append(float(matriz[i][colLAT]))
	 		data[ID]['base']['LON'].append(float(matriz[i][colLON]))
	 		data[ID]['base']['ROW'].append(int(float(matriz[i][colROW])))
	 		data[ID]['base']['COL'].append(int(float(matriz[i][colCOL])))
	 		data[ID]['base']['SOURCETYPE'].append(matriz[i][colSOURCETYPE])
	 		data[ID]['base']['CIUU'].append(matriz[i][colCIUU])
	 		data[ID]['base']['FUELTYPE'].append(matriz[i][colFUELTYPE])
	 		data[ID]['base']['CATEGORY'].append(matriz[i][colCATEGORY])
	 		data[ID]['base']['GROWRATE'].append(float(matriz[i][colGROWRATE]))
	 		data[ID]['base']['BASEFUEL'].append(matriz[i][colBASEFUEL])
	 		data[ID]['base']['PROYECTEDFUEL'].append(int(float(matriz[i][colPROYECTEDFUEL])))
	 		data[ID]['base']['FUELUNIT'].append(matriz[i][colFUELUNIT])
	 		data[ID]['base']['VOCRM'].append(float(matriz[i][colVOCRM]))
	 		data[ID]['base']['VOCFE'].append(float(matriz[i][colVOCFE]))
	 		data[ID]['base']['YEAR'].append(int(float(matriz[i][colYEAR])))

	for ID in data: 

		Pollutants = EmissionFactors[data[ID]['base']['CATEGORY'][0]]
		n = int(YEAR) - data[ID]['base']['YEAR'][0]
		if n < 0: 
			print 'Review YEAR, number negative. ID = ',ID
		
		'''Calculation VOC Industrial'''
		data[ID]['results']['VOC'] = []
		data[ID]['results']['VOC'].append(float(data[ID]['base']['VOCRM'][0] * data[ID]['base']['VOCFE'][0] * math.exp(data[ID]['base']['GROWRATE'][0] * n)))

	 	for pollutant in Pollutants: 
	 		data[ID]['results'][pollutant] = []
	 		if data[ID]['base']['FUELUNIT'][0] == 'kg' or data[ID]['base']['FUELUNIT'][0] == 'kg ':
	 			mult = float(data[ID]['base']['BASEFUEL'][0]) * float(EmissionFactors[data[ID]['base']['CATEGORY'][0]][pollutant]) * (math.exp(data[ID]['base']['GROWRATE'][0] * n))
	 			div = 10**6
	 			result = mult / div
	 			data[ID]['results'][pollutant].append(result)

	 		elif data[ID]['base']['FUELUNIT'][0] == 'm3' or data[ID]['base']['FUELUNIT'][0] == 'm3 ':
	 			mult = float(data[ID]['base']['BASEFUEL'][0]) * float(EmissionFactors[data[ID]['base']['CATEGORY'][0]][pollutant]) * (math.exp(data[ID]['base']['GROWRATE'][0] * n))
	 			div = 10**9
	 			result = mult / div
	 			data[ID]['results'][pollutant].append(result)
	 		else: 
	 			print 'not FUELUNIT, Review', ID

	Pollutants['VOC'] = []
	WriteYear(data, YEAR)
	#print data
	return Pollutants