#! /usr/bin/env python
#-*- encoding: utf-8 -*-

#created by @ceapalaciosal
#under code Creative Commons

import os
import sys
import json
sys.path.append('core')
from listCSV import * 
from excelmatriz import *
from wcsv import *


def speciation(folder, year):

	''''charged mastfrac the PM25 '''
	PM25 = os.path.join('..', 'data', 'in', 'speciation', 'IND_COM_SCP_PM25_'+ str(year) +'.xlsx')
	MPM25 = convertXLSCSV(PM25)

	head = MPM25[0,:]

	index = 0
	for value in head: 
		if value == 'PROFID':
			colPROFID = index
		if value == 'SPCID':
			colSPCID = index
		if value == 'MASSFRAC':
			colMASSFRAC = index
		index += 1

	PM25 = {}
	for i in range(1, MPM25.shape[0]):
		ID = int(float(MPM25[i][colPROFID]))
		if PM25.get(ID) is None:
			PM25[ID] = {}

		if PM25[ID].get(MPM25[i][colSPCID]) is None:
			PM25[ID][MPM25[i][colSPCID]] = float(MPM25[i][colMASSFRAC])

	CSV = listCSV(folder)

	''''charged mastfrac the VOC '''
	VOC = os.path.join('..', 'data', 'in', 'speciation', 'IND_COM_SCP_VOC_'+ str(year) +'.xlsx')
	MVOC = convertXLSCSV(VOC)

	VOC = {}
	for y in range(2, MVOC.shape[0]):
		POLNAME = MVOC[y][0]
		if VOC.get(POLNAME) is None:
			VOC[POLNAME] = {}
		
		for x in range(1, MVOC.shape[1]):
			ID = MVOC[1][x]
			if VOC[POLNAME].get(ID) is None:
				VOC[POLNAME][ID] = float(MVOC[y][x])

	CSV = listCSV(folder)


	for archive in CSV: 
		index = 0
		pos = []
		for letter in archive: 
			if letter == '_':
				pos.append(index)
			index += 1

		#VOC
		if archive[:pos[0]] == 'VOC':
			archive2 = folder + archive
			
			matriz = convertCSVMatrizPoint(archive2)
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
			 	if value == 'UNIT': 
			 		colUNIT = index
			 	if value == 'POLNAME': 
			 		colPOLNAME = index
			 	if value == 'CATEGORY':
			 		colCATEGORY = index
			 	if value == 'PROFID':
			 		colPROFID = index
			 	if value == 'CIUU':
			 		colCIUU = index
				index += 1

			data = {}	
			for i in range(1, matriz.shape[0]):
				ID = matriz[i][colID]
				if data.get(ID) is None:
					data[ID] = {'hour': {}, 'CIUU': matriz[i][colCIUU], 'UNIT': matriz[i][colUNIT], 'POLNAME': matriz[i][colPOLNAME],'CATEGORY': matriz[i][colCATEGORY], 'PROFID': int(float(matriz[i][colPROFID])), 'ROW': int(matriz[i][colROW]), 'COL': int(matriz[i][colCOL]), 'LAT': float(matriz[i][colLAT]), 'LON': float(matriz[i][colLON])}

				hour = 0
				for x in range(colUNIT + 1, matriz.shape[1]):
					if data[ID]['hour'].get(hour) is None: 
						data[ID]['hour'][hour] = float(matriz[i][x])
					hour += 1

			for POLNAME in VOC:
				JPOLNAME = POLNAME
				JPOLNAME = {}
				for ID in data:
					JPOLNAME[ID] = {'hour': {}, 'UNIT': data[ID]['UNIT'], 'COL': data[ID]['COL'], 'LAT': data[ID]['LAT'], 'LON': data[ID]['LON'], 'ROW': data[ID]['ROW']}
					for hour in data[ID]['hour']:
						if data[ID]['CIUU'] in VOC[POLNAME]:
							JPOLNAME[ID]['hour'][hour] = (data[ID]['hour'][hour] * VOC[POLNAME][data[ID]['CIUU']]) / 3600
						else: 
							print 'Not found CIUU', data[ID]['CIUU']
					JPOLNAME[ID]['UNIT'] = 'g/s'

				WriteSpeciationVOC(JPOLNAME, POLNAME, archive[:pos[0]], year)
		#PM25
		if archive[:pos[0]] == 'PM25' or archive[:pos[0]] == ' PM25 ':

			archive2 = folder + archive
			
			matriz = convertCSVMatrizPoint(archive2)
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
			 	if value == 'UNIT': 
			 		colUNIT = index
			 	if value == 'POLNAME': 
			 		colPOLNAME = index
			 	if value == 'CATEGORY':
			 		colCATEGORY = index
			 	if value == 'PROFID':
			 		colPROFID = index
			 	if value == 'CIUU':
			 		colCIUU = index
				index += 1

			data = {}	
			for i in range(1, matriz.shape[0]):
				ID = matriz[i][colID]
				if data.get(ID) is None:
					data[ID] = {'hour': {}, 'CIUU': matriz[i][colCIUU], 'UNIT': matriz[i][colUNIT], 'POLNAME': matriz[i][colPOLNAME],'CATEGORY': matriz[i][colCATEGORY], 'PROFID': int(float(matriz[i][colPROFID])), 'ROW': int(matriz[i][colROW]), 'COL': int(matriz[i][colCOL]), 'LAT': float(matriz[i][colLAT]), 'LON': float(matriz[i][colLON])}

				hour = 0
				for x in range(colUNIT + 1, matriz.shape[1]):
					if data[ID]['hour'].get(hour) is None: 
						data[ID]['hour'][hour] = float(matriz[i][x])
					hour += 1

			speciation = {}
			
			for SPCID in PM25:
				if speciation.get(SPCID) is None:
			
					speciation[SPCID] = {}
			
				for SPC in PM25[SPCID]:
					if speciation[SPCID].get(SPC) is None:
						speciation[SPCID][SPC] = {}

			for ID in data:
				for SPC in speciation[data[ID]['PROFID']]:
					speciation[data[ID]['PROFID']][SPC][ID] = {'ROW': data[ID]['ROW'], 'COL': data[ID]['COL'], 'LAT': data[ID]['LAT'], 'LON': data[ID]['LON'], 'UNIT': data[ID]['UNIT'],'hour': {}}
					for hour in data[ID]['hour']:
						speciation[data[ID]['PROFID']][SPC][ID]['hour'][hour] = data[ID]['hour'][hour]

					for hour in speciation[data[ID]['PROFID']][SPC][ID]['hour']:

						#print ID, hour, speciation[data[ID]['PROFID']][SPC][ID]['hour'][hour]
						operation = speciation[data[ID]['PROFID']][SPC][ID]['hour'][hour] * PM25[data[ID]['PROFID']][SPC] / 3600
						speciation[data[ID]['PROFID']][SPC][ID]['hour'][hour] = operation

					speciation[data[ID]['PROFID']][SPC][ID]['UNIT'] = 'g/s'
						
				
			WriteSpeciationPM25(speciation, archive[:pos[0]], year)
	
		#NOX
		elif archive[:pos[0]] == 'NOX' or archive[:pos[0]] == ' NOX ':

			for POLNAME in ['NO2', 'NO']:
				
				archive2 = folder + archive
				matriz = convertCSVMatrizPoint(archive2)
				head = matriz[0,:]
				data = {}

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
				 	if value == 'UNIT': 
				 		colUNIT = index
				 	if value == 'POLNAME': 
				 		colPOLNAME = index
				 	if value == 'FUELTYPE':
				 		colFUELTYPE = index
					index += 1
				
				for i in range(1, matriz.shape[0]):
					ID = matriz[i][colID]

					if data.get(ID) is None:
						data[ID] = {'General': {'ROW': int(float(matriz[i][colROW])), 'COL': int(float(matriz[i][colCOL])), 'LAT': float(matriz[i][colLAT]), 'LON': float(matriz[i][colLON]), 'UNIT': matriz[i][colUNIT], 'POLNAME': matriz[i][colPOLNAME], 'FUELTYPE': matriz[i][colFUELTYPE]}, 'hours': {}}

					for x in range(colUNIT + 1, matriz.shape[1]):
						hour = matriz[0][x]
						if data[ID]['hours'].get(hour) is None:
							if POLNAME == 'NO2': 
								data[ID]['hours'][hour] = float(matriz[i][x]) * 0.1 / (3600 * 46)
							elif POLNAME == 'NO': 
								data[ID]['hours'][hour] = float(matriz[i][x]) * 0.9 / (3600 * 30)

					data[ID]['General']['UNIT'] = 'g/s'

				#print data
				WriteSpeciation(data, POLNAME, archive[pos[0]:])
		
		#OTHERS
		if archive[:pos[0]] not in ['VOC', 'PM25', 'NOX', 'PM10']:
			#print archive[:pos[0]]
			archive2 = folder + archive
			matriz = convertCSVMatrizPoint(archive2)
			head = matriz[0,:]
			data = {}

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
			 	if value == 'UNIT': 
			 		colUNIT = index
			 	if value == 'POLNAME': 
			 		colPOLNAME = index
			 	if value == 'FUELTYPE':
			 		colFUELTYPE = index
				index += 1
			
			for i in range(1, matriz.shape[0]):
				ID = matriz[i][colID]

				if data.get(ID) is None:
					data[ID] = {'General': {'ROW': int(float(matriz[i][colROW])), 'COL': int(float(matriz[i][colCOL])), 'LAT': float(matriz[i][colLAT]), 'LON': float(matriz[i][colLON]), 'UNIT': matriz[i][colUNIT], 'POLNAME': matriz[i][colPOLNAME], 'FUELTYPE': matriz[i][colFUELTYPE]}, 'hours': {}}

				for x in range(colUNIT + 1, matriz.shape[1]):
					hour = matriz[0][x]
					if data[ID]['hours'].get(hour) is None:
						#print archive[:pos[0]]
						if archive[:pos[0]] == 'CO' or archive[:pos[0]] == ' CO ': 
							data[ID]['hours'][hour] = float(matriz[i][x])/(3600*28)
						elif archive[:pos[0]] == 'CO2' or archive[:pos[0]] == ' CO2 ': 
							data[ID]['hours'][hour] = float(matriz[i][x])/(3600*44)
						elif archive[:pos[0]] == 'SO2' or archive[:pos[0]] == ' SO2 ': 
							data[ID]['hours'][hour] = float(matriz[i][x])/(3600*64)
						else: 
							data[ID]['hours'][hour] = float(matriz[i][x])/3600


				data[ID]['General']['UNIT'] = 'mol/s'
			
			#if archive[:pos[0]] == 'CO2' or archive[:pos[0]] == ' CO2 ':
			#	print data
			WriteSpeciation(data, archive[:pos[0]], archive[pos[0]:])
