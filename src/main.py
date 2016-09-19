#! /usr/bin/env python
#-*- encoding: utf-8 -*-

#created by @ceapalaciosal
#under code Creative Commons

import os
import sys
sys.path.append('core')
from clear import *
from emition import *
from distribution import *
#from split import *
from speciation import *
from calculationPM25 import *
from PMC import *

folder = os.path.join('..','data', 'out', '')
clear(folder)

YEAR = raw_input('Insert Year: ')

database = os.path.join('..', 'data', 'in', 'database.xlsx')
Pollutants = emition(database, YEAR)

emitions = os.path.join('..', 'data', 'out', 'year', 'Year_Emisions_' + YEAR +'.csv')
distribution(emitions, Pollutants, YEAR)

archivePM = os.path.join('..', 'data', 'out', 'distribution', 'PM10_'+YEAR+'.csv')
calculationPM25(archivePM, YEAR)

#distribution = os.path.join('..', 'data','out', 'distribution', '')
#SplitDistribution(distribution)

distribution = os.path.join('..', 'data','out', 'distribution', '')
speciation(distribution, YEAR)

pmc(archivePM, YEAR)
folderspeciation = os.path.join('..','data', 'out', 'speciation', '')
testingpmc(folderspeciation)
