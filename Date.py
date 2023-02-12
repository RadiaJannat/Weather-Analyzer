import numpy as np
import matplotlib.pyplot as pyplot
from FileIO import *

data = FileIO.dataTable
class Date:
    def __init__(self,i):
        self.i=i
        
        self.Month=int(data[self.i][1])
        self.Year=int(data[self.i][0])
    
    def to_return(self):
        return [self.Year,self.Month]