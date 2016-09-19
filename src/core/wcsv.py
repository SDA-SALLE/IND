#created by @ceapalaciosal
#under code Creative Commons
# -*- encoding: utf-8 -*-

#! /usr/bin/env python
import csv
import os
from excelmatriz import *

def WriteYear(data, year):
	#print data 
	folder = os.path.join('..', 'data', 'out','year', '')
	csvsalida = open(folder + 'Year_Emisions_' + year + '.csv', 'w')

	keys = data.keys()
	identi = 0
	for ID in keys: 
		if identi == 0:
			names = sorted(data[ID]['base'].keys())
			names.insert(0, 'ID')
			for name in names: 
				csvsalida.write(name)
				csvsalida.write(',')

			names = sorted(data[ID]['results'].keys())
			for name in names: 
				if name == names[0]:
					csvsalida.write(name)
				else: 
					csvsalida.write(',')
					csvsalida.write(name)
			csvsalida.write('\n')
			identi = 1

		csvsalida.write(str(ID))
		csvsalida.write(',')
		
		names = sorted(data[ID]['base'].keys())
		for name in names:
			csvsalida.write(str(data[ID]['base'][name][0]))
			csvsalida.write(',')

		names = sorted(data[ID]['results'].keys())
		for name in names:
			if name == names[0]:
				csvsalida.write(str(data[ID]['results'][name][0]))
			else: 
				csvsalida.write(',')
				csvsalida.write(str(data[ID]['results'][name][0]))
		csvsalida.write('\n')
	csvsalida.close()

def WriteDistribution(data, pollutant, year):
	'''Charged ID for speciation''' 
	ARCHPROFID =  os.path.join('..', 'data', 'in', 'Constants', 'PROFID_'+ year +'.xlsx')
	MPROFID = convertXLSCSV(ARCHPROFID)
	PROFID = {}
	for i in range(1, MPROFID.shape[0]):
		CATEGORY = MPROFID[i][0]
		if PROFID.get(CATEGORY) is None:
			PROFID[CATEGORY] = int(float(MPROFID[i][1]))

	#print PROFID


	folder = os.path.join('..', 'data', 'out','distribution', '')
	csvsalida = open(folder + pollutant + '_'  + year +'.csv', 'w')

	names = ['ID', 'CIUU','CATEGORY', 'PROFID','FUELTYPE', 'ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	for name in names: 
		if name == names[0]:
			csvsalida.write(name)
		else: 
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')

	keys = data.keys()
	for ID in keys:
		csvsalida.write(str(ID))
		csvsalida.write(',')
		csvsalida.write(data[ID]['General']['CIUU'][0])
		csvsalida.write(',')
		csvsalida.write(data[ID]['General']['CATEGORY'][0])
		csvsalida.write(',')
		csvsalida.write(str(PROFID[data[ID]['General']['CATEGORY'][0]]))
		csvsalida.write(',')
		csvsalida.write(data[ID]['General']['FUELTYPE'][0])
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['ROW'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['COL'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['LAT'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['LON'][0]))
		csvsalida.write(',')
		csvsalida.write(pollutant)
		csvsalida.write(',')
		csvsalida.write('g/h')
		hours = data[ID]['hours'].keys()
		for hours in hours: 
			csvsalida.write(',')
			csvsalida.write(str(data[ID]['hours'][hours]))
		csvsalida.write('\n')

def WritePM25(data, year):

	folder = os.path.join('..', 'data', 'out', 'distribution', '')
	csvsalida = open(folder + 'PM25_' + year +'.csv', 'w')
	names = ['ID', 'CIUU','CATEGORY', 'PROFID','FUELTYPE', 'ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	for name in names: 
		if name == names[0]:
			csvsalida.write(name)
		else: 
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')

	keys = data.keys()
	for ID in keys:
		csvsalida.write(str(ID))
		csvsalida.write(',')
		csvsalida.write(data[ID]['CIUU'])
		csvsalida.write(',')
		csvsalida.write(data[ID]['CATEGORY'])
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['PROFID']))
		csvsalida.write(',')
		csvsalida.write(data[ID]['FUELTYPE'])
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['ROW']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['COL']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['LAT']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['LON']))
		csvsalida.write(',')
		csvsalida.write(data[ID]['POLNAME'])
		csvsalida.write(',')
		csvsalida.write('g/h')
		hours = data[ID]['hour']
		for hours in hours: 
			csvsalida.write(',')
			csvsalida.write(str(data[ID]['hour'][hours]))
		csvsalida.write('\n')
	
def WriteSpeciationVOC(data, POLNAME, Type, year):

	folder = os.path.join('..', 'data', 'out', 'speciation', '')
	csvsalida = open(folder + Type +  '_' + POLNAME + '_' + year +'.csv', 'w')

	names = ['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	for name in names: 
		if name == names[0]:
			csvsalida.write(name)
		else: 
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')

	for ID in data:
		csvsalida.write(str(data[ID]['ROW']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['COL']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['LAT']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['LON']))
		csvsalida.write(',')
		csvsalida.write(POLNAME)
		csvsalida.write(',')
		csvsalida.write(data[ID]['UNIT'])
		hours = data[ID]['hour']
		for hour in hours:
			csvsalida.write(',')
			csvsalida.write(str(data[ID]['hour'][hour]))
		csvsalida.write('\n')

def WriteSpeciationPM25(data, POLNAME, year):

	for SPCID in data:
		
		'''Charged ID for speciation''' 
		ARCHPROFID =  os.path.join('..', 'data', 'in', 'Constants', 'PROFID_'+year+'.xlsx')
		MPROFID = convertXLSCSV(ARCHPROFID)
		#PROFID = {}
		for i in range(1, MPROFID.shape[0]):
			CATEGORY = MPROFID[i][0]
			SPCIDO = int(float(MPROFID[i][1]))
			#print SPCID
			if SPCIDO == SPCID:
				NSPCID = CATEGORY

		folder = os.path.join('..', 'data', 'out', 'speciation', '')

		csvsalida = open(folder + POLNAME + '_' + NSPCID + '_' + year + '.csv', 'w')

		names = ['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
		for name in names: 
			if name == names[0]:
				csvsalida.write(name)
			else: 
				csvsalida.write(',')
				csvsalida.write(name)
		csvsalida.write('\n')

		
		for SPC in data[SPCID]:
			for ID in data[SPCID][SPC]:
				csvsalida.write(str(data[SPCID][SPC][ID]['ROW']))
				csvsalida.write(',')
				csvsalida.write(str(data[SPCID][SPC][ID]['COL']))
				csvsalida.write(',')
				csvsalida.write(str(data[SPCID][SPC][ID]['LAT']))
				csvsalida.write(',')
				csvsalida.write(str(data[SPCID][SPC][ID]['LON']))
				csvsalida.write(',')
				csvsalida.write(SPC)
				csvsalida.write(',')
				csvsalida.write(data[SPCID][SPC][ID]['UNIT'])
				hours = data[SPCID][SPC][ID]['hour']
				for hour in hours:
					csvsalida.write(',')
					csvsalida.write(str(data[SPCID][SPC][ID]['hour'][hour]))
				csvsalida.write('\n')

def WriteSpeciation(data, POLNAME, Type):
	folder = os.path.join('..', 'data', 'out', 'speciation', '')
	csvsalida = open(folder + POLNAME + Type, 'w')

	names = ['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	for name in names: 
		if name == names[0]:
			csvsalida.write(name)
		else: 
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')

	keys = data.keys()
	for ID in keys:
		csvsalida.write(str(data[ID]['General']['ROW']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['COL']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['LAT']))
		csvsalida.write(',')
		csvsalida.write(str(data[ID]['General']['LON']))
		csvsalida.write(',')
		csvsalida.write(POLNAME)
		csvsalida.write(',')
		csvsalida.write(data[ID]['General']['UNIT'])
		hours = names[6:]
		for hour in hours:
			csvsalida.write(',')
			csvsalida.write(str(data[ID]['hours'][hour]))
		csvsalida.write('\n')

def PMC(data, noun, year):

	folder = os.path.join('..', 'data', 'out', 'speciation', '')
	csvsalida = open(folder + noun + '_' + year + '.csv', 'w')
	salida = csv.writer(csvsalida, delimiter=',')


	salida.writerow(["ROW", "COL", "LAT", "LON", "POLNAME", "UNIT", "E00h", "E01h", "E02h", "E03h", "E04h", "E05h", "E06h" ,"E07h", "E08h", "E09h", "E10h", "E11h", "E12h", "E13h", "E14h", "E15h", "E16h", "E17h", "E18h", "E19h", "E20h", "E21h", "E22h", "E23h", "E24h"])
	
	for key in data: 
		# csvsalida.write(key)
		# csvsalida.write(',')
		csvsalida.write(str(int(data[key]['ROW'])))
		csvsalida.write(',')
		csvsalida.write(str(int(data[key]['COL'])))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['LAT']))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['LON']))
		csvsalida.write(',')
		csvsalida.write('PMC')
		csvsalida.write(',')
		csvsalida.write('g/s')
		hours = data[key]['hour']
		for hour in hours:
			csvsalida.write(',')
			csvsalida.write(str(data[key]['hour'][hour]))
		csvsalida.write('\n')
			
	csvsalida.close()




