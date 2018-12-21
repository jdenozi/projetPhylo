import sys 
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout 

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar 
import matplotlib.pyplot as plt 

import random 

class Window(QDialog): 
    def __init__(self, parent=None): 
     super(Window, self).__init__(parent) 

     # a figure instance to plot on 
     
     self.figure,(self.ax,self.ax2)= plt.subplots(nrows=1, ncols=2) 

     self.canvas = FigureCanvas(self.figure) 

     # je garde le truc de navigation en haut plutot propre 
     self.toolbar = NavigationToolbar(self.canvas, self) 

     # connecter la méthode et le boutton
     self.button = QPushButton('Comparaison des arbres') 
     self.button.clicked.connect(self.plot) 

     # layout
     layout = QVBoxLayout() 
     layout.addWidget(self.toolbar) 
     layout.addWidget(self.canvas) 
     layout.addWidget(self.button) 
     self.setLayout(layout) 

    def plot(self): 
      
     data = [random.random() for i in range(10)] 
     data2=[random.random() for i in range(40)]
     self.figure.clear() 
     # create an axis 
     ax = self.figure.add_subplot(121)
     ax2 = self.figure.add_subplot(122)
      # plot data 
     ax.plot(data, '*-') 
     ax2.plot(data, '*-')

     # refresh canvas 
     self.canvas.draw() 


if __name__ == '__main__': 
    app = QApplication(sys.argv) 

    main = Window() 
    main.show() 

    sys.exit(app.exec_()) 
