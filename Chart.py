import numpy as np
import matplotlib.pyplot as pyplot
import FileIO


class Chart:
    def __init__(self):
        self.data = FileIO.FileIO()
        self.dataTable = self.data.dataTable

    def drawLineChart(slef, x, y, title, xlabel, ylabel):
        pyplot.title(title)
        pyplot.ylabel(ylabel)
        pyplot.xlabel(xlabel)

        pyplot.plot(x,y, marker='o')
        pyplot.show()

    def drawBarChart(slef, x, y, title, xlabel, ylabel):
        pyplot.title(title)
        pyplot.ylabel(ylabel)
        pyplot.xlabel(xlabel)

        pyplot.bar(x,y)
        pyplot.show()


import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    def __init__(self):
        pass #The pass statement is used as a placeholder for future code.

    def drawLineChart(self,x,y):
        fig = plt.figure()

        plt.plot(x,y,marker ='o', color="red")
        plt.title('COVID Cases')
        plt.xlabel('Month')
        plt.ylabel('Number of New Cases')

        plt.show()


    def drawBarChart(self,x,y):
        fig = plt.figure()

        y_pos = np.arange(len(x))

        plt.title('Bar Chart for Covid')
        plt.xlabel('Day')
        plt.ylabel('Number of Cases')

        plt.bar(y_pos, y, align='center')
        plt.xticks(y_pos,x)
        plt.show()