import numpy as np
import matplotlib.pyplot as pyplot

class FileIO:
    filePath = "CalgaryWeather.csv"
    dataTable = np.loadtxt(filePath, delimiter=',', skiprows=1, usecols=(0,1,2,3,4), dtype=np.float)