import numpy as np
import matplotlib.pyplot as pyplot
from FileIO import *
from Date import *
from TemperatureData import *
from WeatherAnalyzer import *
#from Chart import *

def main():
    temp_data = TemperatureData
    temperatureData = temp_data.class_list

    data = FileIO.dataTable

    weatherAnalyzer = WeatherAnalyzer(data,temperatureData)
    
    while True:
        print(" 1- Get Minimum Temperature of 1990-2019 \n",
          "2- Get Maximum Temperature of 1990-2019 \n",
          "3- Get Minimum Temperature of 1990-2019 Annually \n",
          "4- Get Maximum Temperature of 1990-2019 Annually \n",
          "5- Get Average Snowfall between 1990-2019 \n",
          "6- Get Average Temperature between 1990-2019 Annually \n",
          "7- LineChart Minimum Temperature of 1990-2019 Annually \n",
          "8- LineChart Maximum Temperature of 1990-2019 Annually \n",
          "9- BarChart Average Snowfall between 1990-2019 Annually\n",
          "10- BarChart Average Temperature between 1990-2019 Annually9 \n")

        user_input = int(input("Enter a section number: ")) 

        if user_input == 1:
            print(weatherAnalyzer.getMinTemp())
        elif user_input == 2:
            print(weatherAnalyzer.getMaxTemp())  
        elif user_input == 3:
            a = weatherAnalyzer.getMinTempAnnually()
            print(a)
        elif user_input == 4:
            a = weatherAnalyzer.getMaxTempAnnually()
            print(a)
        elif user_input == 5:
            a = weatherAnalyzer.getAvgSnowFallAnnually()
            print(a)
        elif user_input == 6:
            a = weatherAnalyzer.getAvgTempAnnually()
            print(a)
        elif user_input == 7:
            a = weatherAnalyzer.getLineChatMinAnnually()
            print(a)
        elif user_input == 8:
            a = weatherAnalyzer.getLineChatMaxAnnually()
            print(a)
        elif user_input == 9:
            a = weatherAnalyzer.getBarChartAvgSnowFallAnnually()
            print(a)
        elif user_input == 10:
            a = weatherAnalyzer.getBarChartAvgTempAnnually()
            print(a)
        else:
            print("Option not vaialable")

        go_again = input("Would you like to try again (y/n)? :")
        go_again = go_again.lower()
        if go_again == 'n':
            break

if __name__ == "__main__":
    main()       