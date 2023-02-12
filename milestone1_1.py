import numpy as np

class FileIO:
    filePath = "CalgaryWeather.csv"
    dataTable = np.loadtxt(filePath, delimiter=',', skiprows=1, usecols=(0,1,2,3,4), dtype=np.float)

class Date:
    def __init__(self,i):
        self.i=i
        
        self.Month=int(FileIO.dataTable[self.i][1])
        self.Year=int(FileIO.dataTable[self.i][0])
    
    def to_return(self):
        return [self.Year,self.Month]     
    
class TemperatureData:
    def __init__(self,i):
        self.i=i
        
        self.date=Date(self.i)
        self.minTemperature=FileIO.dataTable[self.i][3]
        self.maxTemperature=FileIO.dataTable[self.i][2]
        self.snowFall=FileIO.dataTable[self.i][4]

    def class_list(self):
        class_list = self.date.to_return()
        class_list.append(self.minTemperature)
        class_list.append(self.maxTemperature)
        class_list.append(self.snowFall)
        return class_list

class Chart:
    pass

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
        #KEEP IN MIND THIS ONLY PRINTS THE TEMPS, NOT YEARS
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
        #KEEP IN MIND THIS ONLY PRINTS THE TEMPS, NOT YEARS
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
        #KEEP IN MIND THIS ONLY PRINTS THE TEMPS, NOT YEARS
        arr = np.array(snowFall_annually)
        newarr = arr.reshape(30,2)
        return newarr

    def getAvgTempAnnually(self):
        pass

def main():
    temp_data = TemperatureData
    temperatureData = temp_data.class_list

    data = FileIO.dataTable

    weatherAnalyzer = WeatherAnalyzer(data,temperatureData)

    print(weatherAnalyzer.getMinTempAnnually())

if __name__ == "__main__":
    main()            
