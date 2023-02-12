import numpy as np

def read_weather():
    file_name = "weather.csv"

    data = np.loadtxt(file_name, delimiter=',', skiprows=1, usecols=(0,1), dtype=np.float)

    return data

import matplotlib.pyplot as pyplot

def drawChart(x,y):
    fig = pyplot.figure()
    pyplot.title('Temperatures in Calgary between Jan-Dec in 2000')
    pyplot.ylabel('Min Temperature (F)')
    pyplot.xlabel('Month of Year')

    pyplot.plot(x, y, marker='o')
    pyplot.show()

def main():
    a = read_weather()
    #print(a)

    x = []
    x1= np.loadtxt("CalgaryWeather.csv", delimiter=',', skiprows=1, usecols=(0,1,3), dtype=np.float)     
    i = 0
    while i < len(x1):
        if x1[i][0] == 2000:
            x.append(int(x1[i][1]))
            i+=1
        else:
            i+=1    

    #print(x)        
    y = []
    y1= np.loadtxt("CalgaryWeather.csv", delimiter=',', skiprows=1, usecols=(0,1,3), dtype=np.float)     
    i = 0
    while i < len(y1):
        if y1[i][0] == 2000:
            y.append(y1[i][2])
            i+=1
        else:
            i+=1  
    
    #print(y)

    graph = drawChart(x,y)


if __name__ == "__main__":
    main()