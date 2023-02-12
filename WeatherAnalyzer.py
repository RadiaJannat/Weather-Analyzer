import numpy as np
import matplotlib.pyplot as pyplot

class WeatherAnalyzer:
    def __init__(self,data,temperatureData):
        self.data = data
        self.temperatureData = temperatureData

    def getMinTemp(self):
        all_min_temp = []
       
        for i in range(len(self.data)):
            all_min_temp.append(self.data[i][3])
       
        min_of_all = np.amin(all_min_temp)
        return min_of_all 

    def getMinTempAnnually(self): 
        year = 1990
        min_annually = []
        while year < 2020:
            all_min_of_one_year = self.data[self.data[:,0]==year,3]
            min_of_a_year = np.amin(all_min_of_one_year)

            min_annually.append(year)
            min_annually.append(min_of_a_year)

            year += 1

        arr = np.array(min_annually)
        newarr = arr.reshape(30,2)
        return newarr

    def getMaxTemp(self):
        all_max_temp = []
       
        for i in range(len(self.data)):
            all_max_temp.append(self.data[i][2])
       
        max_of_all = np.amax(all_max_temp)
        return max_of_all 

    def getMaxTempAnnually(self):
        year = 1990
        max_annually = []
        while year < 2020:
            all_max_of_one_year = self.data[self.data[:,0]==year,2]
            max_of_a_year = np.amax(all_max_of_one_year)

            max_annually.append(year)
            max_annually.append(max_of_a_year)

            year += 1

        arr = np.array(max_annually)
        newarr = arr.reshape(30,2)
        return newarr

    def getAvgSnowFallAnnually(self):
        year = 1990
        snowFall_annually = []
        while year < 2020:
            all_snowFall_of_one_year = self.data[self.data[:,0]==year,4]
            average_of_a_year = np.average(all_snowFall_of_one_year)

            snowFall_annually.append(year)
            snowFall_annually.append(average_of_a_year)

            year += 1

        arr = np.array(snowFall_annually)
        newarr = arr.reshape(30,2)
        return newarr

    def getAvgTempAnnually(self):
        pass

    def getLineChatMinAnnually(self):
 
    def getLineChatMaxAnnually(self):

    def getBarChartAvgSnowFallAnnually(self):
         
    def getBarChartAvgTempAnnually(self):
            