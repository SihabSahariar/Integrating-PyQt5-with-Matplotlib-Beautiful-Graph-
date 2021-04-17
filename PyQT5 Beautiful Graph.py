import sys
import pandas as pd
from PyQt5.QtWidgets import * 
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib as mpl 
mpl.rcParams['toolbar'] = 'None'
plt.style.use("dark_background")
for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  # very light grey
for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#212946'  # bluish dark grey
colors = [
    '#08F7FE',  # teal/cyan
    '#FE53BB',  # pink
    '#F5D300',  # yellow
    '#00ff41',  # matrix green
    '#fff', #White
]
import random

class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        
        self.setWindowTitle("PyQt5 Beautiful Graph - Matplotlib")       
        self.btn_plot = QPushButton('Plot')
        layout = QGridLayout()
        self.setLayout(layout)
        self.btn_plot.clicked.connect(self.plot)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
    


        layout.addWidget(self.btn_plot)
        layout.addWidget(self.canvas)
        #self.move(300,300)
        self.setLayout(layout)

    def plot(self):
       
        # data = [random.random() for i in range(10)]
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        # ax.plot(data, '*-')
        df = pd.DataFrame({'CO2': [1, 3, 9, 5, 2, 1, 1],
                   'Humadity': [4, 5, 5, 7, 9, 8, 6],'NO2':[17,68,99,3,2,1,2],'H20':[1,4,3,3,8,10,2],'S':[12,18,19,13,21,11,2]})

        fig = plt.subplots()
        df.plot(marker='o', color=colors, ax=ax)
        # Redraw the data with low alpha and slighty increased linewidth:
        n_shades = 10

        diff_linewidth = 1.05
        alpha_value = 0.3 / n_shades
        for n in range(1, n_shades+1):
            ax.plot(marker='o',
                    linewidth=2+(diff_linewidth*n),
                    alpha=alpha_value,
                    legend=False,
                    ax=ax,
                    color=colors)
        # Color the areas below the lines:
        for column, color in zip(df, colors):
            ax.fill_between(x=df.index,
                            y1=df[column].values,
                            y2=[0] * len(df),
                            color=color,
                            alpha=0.1)
        ax.grid(color='#2A3459')
        ax.set_xlim([ax.get_xlim()[0] - 0.2, ax.get_xlim()[1] + 0.2])  # to not have the markers cut off
        ax.set_ylim(0)

        #plt.show()

        self.canvas.draw()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())