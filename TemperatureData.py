import numpy as np
import matplotlib.pyplot as pyplot
from FileIO import *

data = FileIO.dataTable
class TemperatureData:
    def __init__(self,i):
        
        self.i=i
        
        self.date=Date(self.i)
        self.minTemperature=data[self.i][3]
        self.maxTemperature=data[self.i][2]
        self.snowFall=data[self.i][4]

    def class_list(self):
        class_list = self.date.to_return()
        class_list.append(self.minTemperature)
        class_list.append(self.maxTemperature)
        class_list.append(self.snowFall)
        return class_list