# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons
import os
import sys
import json
sys.path.append('core')
from excelmatriz import * 
from wcsv import *

def distribution(archive, pollutants, year):
	matriz = convertCSVMatrizPoint(archive)
	Position = {}
	Days = {}

	head = matriz[0,:]
	index = 0
	for value in head:
	 	if value == 'ID': 
	 		colID = index
	 	if value == 'ROW': 
	 		colROW = index
	 	if value == 'COL':
	 		colCOL = index
	 	if value == 'LAT': 
	 		colLAT = index
	 	if value == 'LON':
	 		colLON = index
	 	if value == 'FUELTYPE':
	 		colFUELTYPE = index
	 	if value == 'SOURCETYPE': 
	 		colSOURCETYPE = index
	 	if value == 'CIUU':
	 		colCIUU = index
	 	if value == 'CATEGORY':
	 		colCategory = index

	 	for pollutant in pollutants: 
	 		if value == pollutant:
	 			Position[value] = index
	 	index += 1

	data = {}
	for i in range(1, matriz.shape[0]):
		ID = matriz[i][colID]
		if data.get(ID) is None: 
			data[ID] = {}
			data[ID]['General'] = {'FUELTYPE': [], 'COL': [], 'LON': [], 'LAT': [], 'ROW': [], 'SOURCETYPE': [], 'CIUU': [], 'CATEGORY':[]}
			data[ID]['hours'] = {}
			data[ID]['Pollutants'] = {}

		if data[ID]['General']['COL'] == []:
			data[ID]['General']['COL'].append(int(float(matriz[i][colCOL])))
			data[ID]['General']['ROW'].append(int(float(matriz[i][colROW])))
			data[ID]['General']['LAT'].append(float(matriz[i][colLAT]))
			data[ID]['General']['LON'].append(float(matriz[i][colLON]))
			data[ID]['General']['FUELTYPE'].append(matriz[i][colFUELTYPE])
			data[ID]['General']['SOURCETYPE'].append(matriz[i][colSOURCETYPE])
			data[ID]['General']['CIUU'].append(matriz[i][colCIUU])
			data[ID]['General']['CATEGORY'].append(matriz[i][colCategory])
			#data[ID]['General']['WORKEDDAYS'].append(matriz[i][colWORKEDDAYS])

		for pollutant in pollutants: 
			data[ID]['Pollutants'][pollutant] = []
			data[ID]['Pollutants'][pollutant].append(matriz[i][Position[pollutant]])

		for hour in range(0, 25):
			data[ID]['hours'][hour] = []

	matriz = None

	distribution = os.path.join('..', 'data', 'in', 'Constants', 'distribution_' + year +'.xlsx')
	matriz = convertXLSCSVPoint(distribution)

	distribution = {}

	for i in range(1, matriz.shape[0]):

		for x in range(1, 25):
			hour = int(float(matriz[0][x]))
			if distribution.get(hour) is None:
				distribution[hour] = float(matriz[i][x])

	for pollutant in pollutants:
		#print pollutant
		for ID in data: 
			#hours = distribution
			for hour in distribution: 
				#print Days[data[ID]['General']['WORKEDDAYS'][0]]
				data[ID]['hours'][hour] = float(float(data[ID]['Pollutants'][pollutant][0]) * 10**6 / 365 * float(distribution[hour]))
			data[ID]['hours'][24] = float(float(data[ID]['Pollutants'][pollutant][0]) * 10**6 / 365 * float(distribution[0])) #float(data[ID]['Pollutants'][pollutant][0]) * float(distribution[0])
			
		WriteDistribution(data, pollutant, year)




