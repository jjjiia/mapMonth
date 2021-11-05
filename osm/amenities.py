from functools import partial
import random
import pprint
#import pylab
import csv
import math
import json
from math import radians, cos, sin, asin, sqrt
from shapely.geometry import *
from shapely.ops import cascaded_union
from operator import itemgetter
import time
from datetime import timedelta
from datetime import datetime
#(40.7534561156999970 -73.9817047118999938)
pointLocation = Point(float(40.7534561156999970),float(-73.9817047118999938))
    
        
def getType(inputFile):
    with open(inputFile,"r") as coords:
        csvReader = csv.reader(coords)
        index = 0

        for row in csvReader:
            print (row)
            break
        count = 0
        obj = {}
        types = ["restaurarnt","fast_food","cafe","butcher","greengrocer","supermarket"]
        
        with open("viewpoints.csv","w")as out:
            csvWriter = csv.writer(out)
        
            for row in csvReader:
                 if row[4] in types:
                      csvWriter.writerow(row)

getType("ny.csv")