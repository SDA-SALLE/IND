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


def calculationPM25(archive, year):

	PM25FRAC = os.path.join('..', 'data', 'in', 'Speciation', 'PM25FRAC_'+year+'.xlsx')
	MPM25FRAC = convertXLSCSVPoint(PM25FRAC)
	PM25FRAC = {}
	for i in range(1, MPM25FRAC.shape[0]):
		if PM25FRAC.get(int(float(MPM25FRAC[i][0]))) is None:
			PM25FRAC[int(float(MPM25FRAC[i][0]))] = float(MPM25FRAC[i][1])
	

	index = 0
	for n in archive: 
		if n == '_':
			pos = index
		index += 1


	MPM = convertCSVMatrizPoint(archive)
	head = MPM[0,:]

	index = 0
	for value in head:
		if value == 'ID':
			colID = index
		if value == 'CATEGORY':
			colCATEGORY = index
		if value == 'PROFID':
			colPROFID = index
		if value == 'ROW':
			colROW = index
		if value == 'COL': 
			colCOL = index
		if value == 'LAT':
			colLAT = index
		if value == 'LON':
			colLON = index
		if value == 'POLNAME':
			colPOLNAME = index
		if value == 'UNIT': 
			colUNIT = index
		if value == 'CIUU':
			colCIUU = index
		if value == 'FUELTYPE':
			colFUELTYPE = index
		index += 1 

	PM = {}
	for i in range(1, MPM.shape[0]):
		ID = MPM[i][colID]

		if PM.get(ID) is None: 
			PM[ID] = {'hour': {}, 'FUELTYPE': MPM[i][colFUELTYPE],'CIUU': MPM[i][colCIUU], 'UNIT': MPM[i][colUNIT], 'POLNAME': MPM[i][colPOLNAME],'CATEGORY': MPM[i][colCATEGORY], 'PROFID': int(float(MPM[i][colPROFID])), 'ROW': int(MPM[i][colROW]), 'COL': int(MPM[i][colCOL]), 'LAT': float(MPM[i][colLAT]), 'LON': float(MPM[i][colLON])}

		hour = 0
		for x in range(colUNIT + 1, MPM.shape[1]):
			if PM[ID]['hour'].get(hour) is None: 
				PM[ID]['hour'][hour] = float(MPM[i][x])
			hour += 1
	
	'''Calculation PM25 fraction'''
	PM25 = PM
	
	for ID in PM25:
		for hour in PM25[ID]['hour']:
			Operation = PM25[ID]['hour'][hour] * PM25FRAC[PM25[ID]['PROFID']]
			PM25[ID]['hour'][hour] = Operation

		PM25[ID]['POLNAME'] = 'PM25'

	WritePM25(PM25, year)
	