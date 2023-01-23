from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

from matplotlib.figure import Figure

    
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, data, parent=None, width=5, height=4, dpi=100):
        self.data = data
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes1 = fig.add_subplot(111)
        self.axes1.set_xlabel('Wavelength') 
        self.axes1.set_ylabel('Transmittance', color = 'black') 
        self.axes1.set_xlim([350,700])
        self.axes2 = self.axes1.twinx()
        self.axes2.set_ylabel('k', color = 'black') 
        self.axes2.tick_params(axis ='y', labelcolor = 'black') 
        self.axes2.set_ylabel('Reflectance', color = 'black') 
        fig.suptitle("Transmittance and Reflectance of thin film", fontsize=12)
        super(MplCanvas, self).__init__(fig)
        
       