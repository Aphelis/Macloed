import sys
import os
import pandas as pd

import numpy as np
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QMdiArea,
    QMdiSubWindow, QFileDialog, QTableWidget,
    QDialogButtonBox, QComboBox, QTableWidgetItem,
    QTabWidget, QPushButton, QWidget, QMessageBox,
    QProgressBar, QTableView
)
from PyQt6.QtGui import QAction, QCloseEvent
from PyQt6.QtCore import Qt, QThreadPool

from PyQt6 import uic, QtWidgets
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from module.Function import Design_thinfilm
from module.Worker import Worker
from module.mplwidget import MplCanvas
from module.TableModel import TableModel
class ResuftWindow(QMdiSubWindow):
    count = 0
    def __init__(self, parent, data, window_name="Resuft"):
        super(ResuftWindow, self).__init__()
        self.parent = parent
        # Get Ui
        uic.loadUi("uic/table_resuft.ui", self)
        self.table = self.findChild(QTableView, "tableView")
        self.setWindowTitle(window_name)
        # Setup data
        self.model = TableModel(data)
        self.table.setModel(self.model)   
class NewMaterialWindow(QMdiSubWindow):
    count = 0
    def __init__(self, parent, data, window_name="New Material"):
        super(NewMaterialWindow, self).__init__()
        self.parent = parent
        self.data = data
        # Get Ui
        uic.loadUi("uic/newMaterial.ui", self)
        self.table = self.findChild(QTableView, "tableView")
        self.button = self.findChild(QDialogButtonBox, "buttonBox")
        self.button.accepted.connect(self.accept)
        self.button.rejected.connect(self.reject)
        self.setWindowTitle(window_name)
        # Setup data
        self.model = TableModel(data)
        self.table.setModel(self.model)  
    def accept(self):
        self.close()
        try:
            fileName = QFileDialog.getSaveFileName(self, "Open...", os.getenv("HOME"), 
                                                    filter = "CSV(*.csv)")
            self.data.to_csv(fileName[0], index=False)
        except:
            pass
    def reject(self):
        self.close()
class FormulaWindow(QMdiSubWindow):
    def __init__(self, parent, table, table_parent):
        super(FormulaWindow, self).__init__()
        # Get Ui
        uic.loadUi("uic/formula.ui", self)
        self.setWindowTitle("Formula")
        self.parent = parent
        self.table = table
        self.table_parent = table_parent
        self.formulaTable = self.findChild(QTableWidget, "formulaTable")
        self.button = self.findChild(QDialogButtonBox, "buttonBox")
        self.button.accepted.connect(self.accept)
        self.button.rejected.connect(self.reject)
        #
        rowCount = self.formulaTable.rowCount()
        for row in range(1, rowCount):
            comboBox = QComboBox(self)
            comboBox.addItems(MainWindow.list_material)  
            self.formulaTable.setCellWidget(row, 1, comboBox)
    def accept(self):
        rowCount = self.table.rowCount()
        formulaData = self.getValue()
        keys = list(formulaData.keys())
        keys = keys[::-1]
        num = 0
        for key in keys:
            if key == "Subtrate":
                subtrate = formulaData[key]["material"]
            num += int(formulaData[key]["num"])
        for i in range(num-rowCount):
            self.table.insertRow(0)
            comboBox = QComboBox(self)
            comboBox.addItems(MainWindow.list_material)  
            self.table.setCellWidget(0, 1, comboBox)
            comboBox.currentTextChanged.connect(self.table_parent.refresh_table)
            self.table.setItem(0, 4, QTableWidgetItem(str(0)))
            self.table_parent.refreshLayerNum()
        rowCount = self.table.rowCount()
        self.table.cellWidget(rowCount-1, 1).setCurrentText(subtrate)
        for row in range(num-1):
            if row%2 == 0:
                material = formulaData["2"]["material"]
            elif row%2 != 0:
                material = formulaData["1"]["material"]
            self.table.cellWidget(row, 1).setCurrentText(material)
        self.table_parent.refresh_table(0)
        self.close()
    def reject(self):
        self.close()
    def getValue(self):
        formulaData = {}
        rowCount = self.formulaTable.rowCount()
        for row in range(1, rowCount):
            value = {}
            key = self.formulaTable.item(row, 0).text()
            widget = self.formulaTable.cellWidget(row, 1)
            if isinstance(widget, QComboBox):
                value.update({"material" : widget.currentText()})
            number = int(self.formulaTable.item(row, 2).text())
            value.update({"num": number})
            formulaData.update({key: value})
        return formulaData
    def closeEvent(self, event: QCloseEvent):
        self.hide()
        super().closeEvent(event) 
class PlotWindow(QMdiSubWindow):
    def __init__(self, parent, T1, T2):
        super(PlotWindow, self).__init__()
        uic.loadUi("uic/plot.ui", self)
        self.parent = parent

        self.setWindowTitle("Plot Window")

        self.T1 = self.findChild(QWidget, "T1")
        self.plot_matp(self.T1, T1)
        self.T2 = self.findChild(QWidget, "T2")
        self.plot_matp(self.T2, T2)
        #
        self.tabWidget = self.findChild(QTabWidget, "tabWidget")
    def plot_matp(self, plot, data):
        sc = MplCanvas(self, data, width=5, height=4, dpi=100)
        sc.axes1.plot(data[0], data[1],'r-',label='Transmittance') 
        sc.axes2.plot(data[0], data[2],'g-',label='Reflectance') 
        sc.axes1.legend(loc='upper left', bbox_to_anchor=(0, 1), fontsize=7)
        sc.axes2.legend(loc='upper left', bbox_to_anchor=(0, 0.94), fontsize=7)
        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)
        plot.setLayout(layout)
    def addTab(self, tabName):
        page = QWidget(self.tabWidget)
        self.tabWidget.addTab(page, tabName)
    def plot_over(self, T3, TB, TA):
        self.addTab("Target ?????????")
        self.plot_matp(self.tabWidget.widget(2), T3)
        self.addTab("????????????????????????")
        self.plot_matp(self.tabWidget.widget(3), TB)
        self.addTab("????????????????????????")
        self.plot_matp(self.tabWidget.widget(4), TA)
    
    def closeEvent(self, event: QCloseEvent):
        self.parent.menuPlot.setEnabled(True)
        self.parent.menuCalculate.setEnabled(False)
        super().closeEvent(event) 
        
class TargetsWindow(QMdiSubWindow):
    def __init__(self, parent):
        super(TargetsWindow, self).__init__()
        # Get Ui
        uic.loadUi("uic/targets.ui", self)
        self.setWindowTitle("Targets")
        self.tab = self.findChild(QTabWidget, "tabWidget")
        self.parent = parent
        self.initialization()
    def initialization(self):
        target = pd.read_excel(r"C:\Users\letan\OneDrive\M??y t??nh\Macleod2\targets\custom_target.xlsx")
        reflectance = list(target.iloc[:, 1])
        MainWindow.targets = [target for i in range(2)]
        self.targetB = self.findChild(QTableWidget, "tableBeforeWidget")
        self.targetB.setRowCount(len(MainWindow.custom_wavelengths)+1)
        self.targetB.setColumnCount(2)
        for row in range(len(MainWindow.custom_wavelengths)):
            self.targetB.setItem(row, 0, QTableWidgetItem(MainWindow.custom_wavelengths[row]))
            self.targetB.setItem(row, 1, QTableWidgetItem(str(reflectance[row])))
        self.targetA = self.findChild(QTableWidget, "tableAfterWidget")
        self.targetA.setRowCount(len(MainWindow.custom_wavelengths)+1)
        self.targetA.setColumnCount(2)
        for row in range(len(MainWindow.custom_wavelengths)):
            self.targetA.setItem(row, 0, QTableWidgetItem(MainWindow.custom_wavelengths[row]))
            self.targetA.setItem(row, 1, QTableWidgetItem(str(reflectance[row])))
    def refreshTable(self, reflectance, index = 0):
        if index == 0:
            for row in range(len(MainWindow.custom_wavelengths)):
                self.targetB.setItem(row, 1, QTableWidgetItem(str(reflectance[row])))
        elif index == 1:
            for row in range(len(MainWindow.custom_wavelengths)):
                self.targetA.setItem(row, 1, QTableWidgetItem(str(reflectance[row])))
    def closeEvent(self, event: QCloseEvent):
        self.parent.menuOpenTargets.setEnabled(False)
        self.hide()
        super().closeEvent(event)
   
class NewDesignWindow(QMdiSubWindow):
    def __init__(self, parent, windowName):
        super(NewDesignWindow, self).__init__()
    
        # Get Ui
        self.parent = parent
        self.parent.menuOpenDesign.setEnabled(True)
        self.parent.menuSaveDesign.setEnabled(True)
        uic.loadUi("uic/design.ui", self)
        self.setWindowTitle(windowName)
        #
        self.progressBar = self.findChild(QProgressBar, "progressBar")
        self.progressBar.hide()
        #
        self.beforeTable = self.findChild(QTableWidget, "before_table")
        self.afterTable = self.findChild(QTableWidget, "after_table")
        self.buttonB = self.findChild(QPushButton, "BeforeButton")
        self.buttonB.clicked.connect(self.parent.formula_before)
        self.buttonA = self.findChild(QPushButton, "AfterButton")
        self.buttonA.clicked.connect(self.parent.formula_after)
        #
        self.reference_wavelength_value = MainWindow.custom_wavelengths[0]
        self.currentSelecRow = -1
        #
        self.reference_wavelength_Box = self.findChild(QComboBox, "reference_wavelength")
        self.reference_wavelength_Box.addItems(MainWindow.custom_wavelengths)
        # Reference wavelength Combobox changes, the signal will be returned to
        self.reference_wavelength_Box.currentTextChanged.connect(self.reference_wavelength_Box_text_change)
        # Set material ComboBox
        rowCount = self.beforeTable.rowCount()
        for row in range(rowCount):
            comboBox = QComboBox(self)
            comboBox.addItems(MainWindow.list_material)  
            comboBox.currentTextChanged.connect(self.refresh_table)
            self.beforeTable.setCellWidget(row, 1, comboBox)
        for row in range(rowCount):
            comboBox = QComboBox(self)
            comboBox.addItems(MainWindow.list_material)  
            comboBox.currentTextChanged.connect(self.refresh_table)
            self.afterTable.setCellWidget(row, 1, comboBox)
        #
        self.refresh_table(0)
        #Set Signal
        self.beforeTable.itemChanged.connect(self.beforeTableThicknessChange)
        self.afterTable.itemChanged.connect(self.afterTableThicknessChange)
    def beforeTableThicknessChange(self, item):
        col = self.beforeTable.column(item)
        row = self.beforeTable.row(item)
        #
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        text = QTableWidgetItem(item.text())
        text.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        #
        if col == 4 and item.text() != "0" and self.afterTable.item(row, col).text() != item.text():
            self.afterTable.setItem(row, col, text)
        
    def afterTableThicknessChange(self, item):
        col = self.afterTable.column(item)
        row = self.afterTable.row(item)
        #
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        text = QTableWidgetItem(item.text())
        text.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        #
        if (col == 4) and (item.text() != "0") and (self.beforeTable.item(row, col).text() != item.text()):
            self.beforeTable.setItem(row, col, QTableWidgetItem(item.text()))
    def refresh_table(self, text):
        """ Refresh n and k value
            Setup begining n and k value"""
        rowCount = self.beforeTable.rowCount()
        for row in range(rowCount):
            widget = self.beforeTable.cellWidget(row, 1)
            if isinstance(widget, QComboBox):
                name = widget.currentText()
                data = MainWindow.data_material[name]
                try: 
                    row_data = data[data["wavelength"] == np.float64(self.reference_wavelength_value)]
                except KeyError:
                    row_data = data[data["Wavelength"] == np.float64(self.reference_wavelength_value)]
                n = QTableWidgetItem(str(float(row_data["n"])))
                k = QTableWidgetItem(str(float(row_data["k"])))  
                self.beforeTable.setItem(row, 2, n)
                self.beforeTable.setItem(row, 3, k)
            # ater table
            widget = self.afterTable.cellWidget(row, 1)
            if isinstance(widget, QComboBox):
                name = widget.currentText()
                data = MainWindow.data_material[name]
                try: 
                    row_data = data[data["wavelength"] == np.float64(self.reference_wavelength_value)]
                except KeyError:
                    row_data = data[data["Wavelength"] == np.float64(self.reference_wavelength_value)]
                n = QTableWidgetItem(str(float(row_data["n"])))
                k = QTableWidgetItem(str(float(row_data["k"])))  
                self.afterTable.setItem(row, 2, n)
                self.afterTable.setItem(row, 3, k)
            
    def reference_wavelength_Box_text_change(self, text):
        self.reference_wavelength_value = text
        self.refresh_table(0)
    def addRow(self):
        '''Add a row to before_table
           custom: highest'''
        # Get insert row index
        row = self.currentSelecRow
        if row == -1:
            row = self.beforeTable.rowCount() - 1
        elif row == 0:
            row = 1
        #Insert row
        self.beforeTable.insertRow(row)
        self.afterTable.insertRow(row)
        #Refresh layer number
        self.refreshLayerNum()
        #Give new row Combobox
        comboBox = QComboBox(self)
        comboBox.addItems(MainWindow.list_material)  
        comboBox.currentTextChanged.connect(self.refresh_table)
        self.beforeTable.setCellWidget(row, 1, comboBox)
        self.beforeTable.setItem(row, 4, QTableWidgetItem(str(0)))
        
        comboBox = QComboBox(self)
        comboBox.addItems(MainWindow.list_material)  
        comboBox.currentTextChanged.connect(self.refresh_table)
        self.afterTable.setCellWidget(row, 1, comboBox)
        self.afterTable.setItem(row, 4, QTableWidgetItem(str(0)))

        self.refresh_table(0)
        self.parent.check_menu_Remove()
    def removeRow(self):
        # Get insert row index
        row = self.beforeTable.currentRow()
        if row == self.beforeTable.rowCount() - 1:
            row = self.beforeTable.rowCount() - 2
        elif row == 0:
            row = 1
        elif row == -1:
            row = row = self.beforeTable.rowCount() - 2
        #Remove row
        self.beforeTable.removeRow(row)
        #Refresh layer number
        self.refreshLayerNum()
        #Give new row Combobox
        comboBox = QComboBox(self)
        comboBox.addItems(MainWindow.list_material)  
        self.beforeTable.setCellWidget(row, 1, comboBox)
        comboBox.currentTextChanged.connect(self.refresh_table)

        comboBox = QComboBox(self)
        comboBox.addItems(MainWindow.list_material)  
        self.afterTable.setCellWidget(row, 1, comboBox)
        comboBox.currentTextChanged.connect(self.refresh_table)
        self.refresh_before_table(0)
        self.parent.check_menu_Remove()
    def refreshLayerNum(self):
        '''Refresh layer numer'''
        index = 1
        for row in range(self.beforeTable.rowCount()-2, -1, -1):
            row_text = QTableWidgetItem(str(index))
            row_text.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.beforeTable.setItem(row, 0, row_text)
            index += 1
        index = 1
        for row in range(self.afterTable.rowCount()-2, -1, -1):
            row_text = QTableWidgetItem(str(index))
            row_text.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.afterTable.setItem(row, 0, row_text)
            index += 1
    def getValue(self):
        beforeTableData = {}
        afterTableData = {}
        #Before Table
        rowCount = self.beforeTable.rowCount()
        for row in range(rowCount):
            value = {}
            key = self.beforeTable.item(row, 0).text()
            widget = self.beforeTable.cellWidget(row, 1)
            if isinstance(widget, QComboBox):
                value.update({"material" : widget.currentText()})
            try: 
                n = float(self.beforeTable.item(row, 2).text())
                k = float(self.beforeTable.item(row, 3).text())
                d = float(self.beforeTable.item(row, 4).text())
                value.update({"n": n, "k": k, "d": d})
            except AttributeError as error:
                print(error)
            beforeTableData.update({key: value})
        #After Table
        rowCount = self.afterTable.rowCount()
        colCount = self.afterTable.columnCount()
        for row in range(rowCount):
            value = {}
            key = self.afterTable.item(row, 0).text()
            widget = self.afterTable.cellWidget(row, 1)
            if isinstance(widget, QComboBox):
                value.update({"material": widget.currentText()})
            try: 
                n = float(self.afterTable.item(row, 2).text())
                k = float(self.afterTable.item(row, 3).text())
                d = float(self.afterTable.item(row, 4).text())
                value.update({"n": n, "k": k, "d": d})
            except AttributeError as error:
                print(error)
            afterTableData.update({key: value})
        return beforeTableData, afterTableData, rowCount
    def resetWindowName(self, windowName):
        self.setWindowTitle(windowName)
    def closeEvent(self, event: QCloseEvent):
        self.parent.menuInsertRow.setEnabled(False)
        self.parent.menuRemoveRow.setEnabled(False)
        self.parent.menuOpenDesign.setEnabled(False)
        self.parent.menuSaveDesign.setEnabled(False)
        self.parent.formulaB = None
        self.parent.formulaA = None
        self.parent.menuNewDesign.setEnabled(True)
        super().closeEvent(event)
    def resizeEvent(self, event):
        super().resizeEvent(event)
class MainWindow(QMainWindow):
    list_material = []
    custom_wavelengths = []
    data_material = {}
    targets = []
    formulaData = {}
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("uic/main.ui", self)
        self.program_initialization()
        self.threadpool = QThreadPool()
        self.formulaB = None
        self.formulaA = None
        self.table_window = None
        # MDI Area
        self.mdi = self.findChild(QMdiArea, "mdiArea")
        self.targets_window = TargetsWindow(self)
        
        self.mdi.addSubWindow(self.targets_window)
        self.targets_window.hide()
        # Menu File
        self.menuNewDesign = self.findChild(QAction, "actionNewDesign")
        self.menuNewDesign.setShortcut('Ctrl+N')
        self.menuNewDesign.triggered.connect(self.new_design_window)
        self.menuNewMaterial = self.findChild(QAction, "actionNewMaterial")
        self.menuNewMaterial.setShortcut('Ctrl+Shift+N')
        self.menuNewMaterial.triggered.connect(self.new_material_window)
        self.menuOpenTargets = self.findChild(QAction, "actionOpenTargets")
        self.menuOpenTargets.triggered.connect(self.open_targets)
        self.menuOpenTargets.setEnabled(False)
        self.menuSaveDesign = self.findChild(QAction, "actionSave")
        self.menuSaveDesign.setShortcut('Ctrl+S')
        self.menuSaveDesign.triggered.connect(self.saveDesign)
        self.menuSaveDesign.setEnabled(False)
        self.menuOpenDesign = self.findChild(QAction, "actionOpenDesign")
        self.menuOpenDesign.setShortcut('Ctrl+O')
        self.menuOpenDesign.triggered.connect(self.openDesign)
        # Menu Edit
        self.menuInsertRow = self.findChild(QAction, "actionInsert_Row")
        self.menuInsertRow.setEnabled(False)
        self.menuRemoveRow = self.findChild(QAction, "actionRemove_Layer")
        self.menuRemoveRow.setEnabled(False)
        self.menuBeforeFormula = self.findChild(QAction, "actionBeforeFormula")
        self.menuBeforeFormula.triggered.connect(self.formula_before)
        self.menuBeforeFormula.setEnabled(False)
        self.menuAfterFormula = self.findChild(QAction, "actionAfterFormula")
        self.menuAfterFormula.triggered.connect(self.formula_after)
        self.menuAfterFormula.setEnabled(False)
        # Menu Parameters
        self.menuTargets = self.findChild(QAction, "actionTargets")
        self.menuTargets.triggered.connect(self.targetsWindow)
        # Menu Performance
        self.menuPlot = self.findChild(QAction, "actionPlot")
        self.menuPlot.triggered.connect(self.plotWindow)
        self.menuPlot.setEnabled(False)
        self.menuCalculate = self.findChild(QAction, "actionCaculator")
        self.menuCalculate.triggered.connect(self.plot_Optimize)
        self.menuCalculate.setEnabled(False)
    def program_initialization(self):
        MainWindow.list_material = []
        MainWindow.data_material = {}
        path = os.getcwd()  + r"\material"
        for f_name in os.listdir(path):
            if f_name.endswith('.csv'):
                row = 0
                while f_name[row] != ".":
                    row +=1
                MainWindow.list_material.append(f_name[:row])
                MainWindow.data_material[f_name[:row]] = pd.read_csv(path + "/" + f_name)
                data = pd.read_csv(path + "/" + f_name)
        wavelengths = list(data["Wavelength"])
        MainWindow.custom_wavelengths = [str(w) for w in wavelengths]
    def new_design_window(self, Unknown, windowName = "New Design"):
        
        self.menuNewDesign.setEnabled(False)
        self.program_initialization()
        self.table_window = NewDesignWindow(self, windowName=windowName)
        self.mdi.addSubWindow(self.table_window)
        self.table_window.show()
        self.menuInsertRow.setEnabled(True)
        self.menuInsertRow.triggered.connect(self.table_window.addRow)
        self.menuRemoveRow.triggered.connect(self.table_window.removeRow)
        self.check_menu_Remove()
        self.menuPlot.setEnabled(True)
        self.menuBeforeFormula.setEnabled(True)
        self.menuAfterFormula.setEnabled(True)
    def check_menu_Remove(self):
        if self.table_window.before_table.rowCount() > 3:
            self.menuRemoveRow.setEnabled(True)
        else:
            self.menuRemoveRow.setEnabled(False)
    def formula_before(self):
        if self.formulaB == None:
            self.formulaB = FormulaWindow(self, self.table_window.beforeTable, self.table_window)
            self.mdi.addSubWindow(self.formulaB)
            self.formulaB.show()
        elif self.formulaB != None:
            self.formulaB.show()
    def formula_after(self):
        if self.formulaA == None:
            self.formulaA = FormulaWindow(self, self.table_window.afterTable, self.table_window)
            self.mdi.addSubWindow(self.formulaA)
            self.formulaA.show()
        elif self.formulaA != None:
            self.formulaA.show()
    def new_material_window(self):
        # try:
            path = QFileDialog.getOpenFileName(self, "Open...", os.getenv(r"C:/"), 
                                            filter = "All(*.*);;CSV(*.csv);;Excel(*.xlsx);;Text(*.txt)")
            file_name = os.path.basename(path[0])
            if path[0] != "":
                if file_name.endswith(".csv"):
                    data = pd.read_csv(path[0])
                elif file_name.endswith(".xlsx"):
                    data = pd.read_excel(path[0])
                elif file_name.endswith(".txt"):
                    data = pd.read_clipboard(path[0])
            wavelength = data.iloc[:,0]
            n = data.iloc[:,1]
            k = data.iloc[:,2]
            save_data = pd.DataFrame({"Wavelength": wavelength, "n": n, "k": k})
            sub = NewMaterialWindow(self, save_data)
            self.mdi.addSubWindow(sub)
            sub.show()
            
        # except:
        #     pass
    def open_targets(self):
            tab_index = self.targets_window.tab.currentIndex()
            path = QFileDialog.getOpenFileName(self, "Open...", os.getenv(r"..\targets"), 
                                            filter = "All(*.*);;CSV(*.csv);;Excel(*.xlsx);;Text(*.txt)")
            file_name = os.path.basename(path[0])
            if path[0] != "":
                if file_name.endswith(".csv"):
                    data = pd.read_csv(path[0])
                elif file_name.endswith(".xlsx"):
                    data = pd.read_excel(path[0])
                elif file_name.endswith(".txt"):
                    data = pd.read_clipboard(path[0])
                wavelength = data.iloc[:, 0]
                reflectance = data.iloc[:, 1]
                targets = pd.DataFrame({"Wavelength (nm)": wavelength, "Reflectance": reflectance})
                MainWindow.targets[tab_index] = targets
                self.targets_window.refreshTable(reflectance = reflectance, index = tab_index)
    def saveDesign(self):
        try:
            beforeData = pd.DataFrame.from_dict(beforeData, orient = "index")
            aftbeforeData, afterData = self.getSaveValue()
            erData = pd.DataFrame.from_dict(afterData, orient = "index")
            data = beforeData.append(afterData)
            data.index.name = "Layer"
            path = QFileDialog.getSaveFileName(self, "Save...", os.getenv(r"..\design"), 
                                                    filter = "All(*.*);;CSV(*.csv);;Excel(*.xlsx);;Text(*.txt)")
            data.to_csv(path[0])
        except:
            pass
    def getSaveValue(self):
        beforeData, afterData, _ = self.table_window.getValue()
        return beforeData, afterData
    def openDesign(self):
        try:
            materials = [[] for _ in range(2)]
            thickness = [[] for _ in range(2)]
            path = QFileDialog.getOpenFileName(self, "Open...", os.getenv(r"..\targets"), 
                                                filter = "All(*.*);;CSV(*.csv);;Excel(*.xlsx);;Text(*.txt)")
            file_name = os.path.splitext(os.path.basename(path[0]))
            if self.table_window == None:
                self.new_design_window(None, windowName=file_name[0])
            else:
                self.table_window.resetWindowName(file_name[0])
            data = pd.read_csv(path[0]).to_dict()
            keys = list(data.keys())
            layerKeys = data[keys[0]].keys()
            i = 0
            for key in layerKeys:
                materials[i].append(data["material"][key])
                thickness[i].append(data["d"][key])
                if data["Layer"][key] == "Subtrate":
                    i += 1
            self.updateTableMaterial(materials[0], self.table_window.beforeTable)
            self.updateTableMaterial(materials[1], self.table_window.afterTable)
            self.updateTableThickness(thickness[0], self.table_window.beforeTable)
        except:
            pass
    def updateTableMaterial(self, materials, table):
        num = len(materials)
        rowCount = table.rowCount()
        for _ in range(num-rowCount):
            table.insertRow(0)
            comboBox = QComboBox(self)
            comboBox.addItems(MainWindow.list_material)  
            table.setCellWidget(0, 1, comboBox)
            comboBox.currentTextChanged.connect(self.table_window.refresh_table)
            table.setItem(0, 4, QTableWidgetItem(str(0)))
            self.table_window.refreshLayerNum()
        table.cellWidget(rowCount-1, 1).setCurrentText(materials[-1])
        for row in range(num-1):
            table.cellWidget(row, 1).setCurrentText(materials[row])
        self.table_window.refresh_table(0)
    def updateTableThickness(self, thickness, table):
        num = len(thickness)
        for row in range(num):
            table.setItem(row, 4, QTableWidgetItem(str(thickness[row])))
        self.table_window.refresh_table(0)
    def selec_material_folder(self):
        MainWindow.list_material = []
        path = QFileDialog.getExistingDirectory(self)
        for f_name in os.listdir(path):
            if f_name.endswith('.csv'):
                row = 0
                while f_name[row] != ".":
                    row +=1
                MainWindow.list_material.append(f_name[:row])
    def targetsWindow(self):
        self.targets_window.show()
        self.menuOpenTargets.setEnabled(True)
    def plotWindow(self):
        try:
            T1, T2 = self.calculate_T1_T2()
            self.plot_window = PlotWindow(self, self.Pd2Lst(T1), self.Pd2Lst(T2))
            self.mdi.addSubWindow(self.plot_window)
            self.plot_window.show()
            self.menuCalculate.setEnabled(True)
            self.menuPlot.setEnabled(False)
        except IndexError:
            self.warning()
    def plot_Optimize(self):
        self.worker = Worker(self.calculate_O)
        self.worker.signals.start.connect(self.start_fitting)
        self.worker.signals.progress.connect(self.progress_fn)
        self.worker.signals.error.connect(self.calculate_errror)
        self.worker.signals.result.connect(self.print_output)
        self.worker.signals.finished.connect(self.thread_complete)
        # Execute
        self.threadpool.start(self.worker)
    def getValue(self):
        beforeData, afterData, layerNum = self.table_window.getValue()
        thickness = [0 for i in range(10)]
        wavelength = [float(wavelength) for wavelength in MainWindow.custom_wavelengths]
        #Before Table
        materials = []
        i = 0
        keys = list(beforeData.keys())
        keys = keys[::-1]
        for key in keys:
                if key == "Subtrate":
                    subtrate = MainWindow.data_material[beforeData[key]["material"]]
                    continue
                if beforeData[key]['material'] not in materials:
                    materials.append(beforeData[key]['material'])
                thickness[i] = beforeData[key]['d']
                i += 1
        material_B1 = MainWindow.data_material[materials[0]]
        material_B2 = MainWindow.data_material[materials[1]]
        #After Table
        materials = []
        i = 0
        keys = list(afterData.keys())
        keys = keys[::-1]
        for key in keys:
                if key == "Subtrate":
                    subtrate = MainWindow.data_material[afterData[key]["material"]]
                    continue
                if afterData[key]['material'] not in materials:
                    materials.append(afterData[key]['material'])
                    i += 1
        material_A1 = MainWindow.data_material[materials[0]]
        material_A2 = MainWindow.data_material[materials[1]]
        return subtrate, material_B1, material_B2, material_A1, material_A2, thickness, layerNum, wavelength
    def calculate_T1_T2(self):
        subtrate, material_B1, material_B2, material_A1, material_A2, thickness, layerNum, wavelength = self.getValue()
        #
        O1=Design_thinfilm( subtrate = subtrate , 
                                material_1 = material_B1,
                                material_2 = material_B2,
                                layer_num=layerNum)
        O2=Design_thinfilm( subtrate = subtrate, 
                                material_1 = material_A1,
                                material_2 = material_A2,
                                layer_num = layerNum)
        # thickness = [50, 125.1, 17.83, 41.57, 9.11, 48.15, 0, 0, 0, 0]
        T1=O1.Layer_10(wavelength,thickness_1=thickness[0],
                                    thickness_2 =thickness[1],
                                    thickness_3 =thickness[2],
                                    thickness_4 =thickness[3],
                                    thickness_5 =thickness[4],
                                    thickness_6 =thickness[5],
                                    thickness_7 =thickness[6],
                                    thickness_8 =thickness[7],
                                    thickness_9 =thickness[8],
                                    thickness_10=thickness[9])
        T2=O2.Layer_10(wavelength,thickness_1=thickness[0],
                                    thickness_2 =thickness[1],
                                    thickness_3 =thickness[2],
                                    thickness_4 =thickness[3],
                                    thickness_5 =thickness[4],
                                    thickness_6 =thickness[5],
                                    thickness_7 =thickness[6],
                                    thickness_8 =thickness[7],
                                    thickness_9 =thickness[8],
                                    thickness_10=thickness[9])
        return T1, T2
    def calculate_O(self):
        subtrate, material_B1, material_B2, material_A1, material_A2, thickness, layerNum, wavelength = self.getValue()
        O1=Design_thinfilm( subtrate = subtrate , 
                                material_1 = material_B1,
                                material_2 = material_B2,
                                layer_num=layerNum)
        O2=Design_thinfilm( subtrate = subtrate, 
                                material_1 = material_A1,
                                material_2 = material_A2,
                                layer_num = layerNum)
        RB_weight=100
        Target= O1.R_Target(RB_target = MainWindow.targets[0],
                                RA_target = MainWindow.targets[1],
                                RB_weight = RB_weight)

        Target_nk=O1.Target_nk(material_B2, material_A2, RB_weight)
        O3=Design_thinfilm( subtrate = subtrate, 
                                material_1 = material_B1,
                                material_2 = Target_nk,
                                layer_num=layerNum)
        T3=O3.Layer_10(wavelength, thickness_1=thickness[0],
                                    thickness_2 =thickness[1],
                                    thickness_3 =thickness[2],
                                    thickness_4 =thickness[3],
                                    thickness_5 =thickness[4],
                                    thickness_6 =thickness[5],
                                    thickness_7 =thickness[6],
                                    thickness_8 =thickness[7],
                                    thickness_9 =thickness[8],
                                    thickness_10=thickness[9])
        bounds=[[49,0,0,0,0,0,0,0,0,0], # ??????
        [50,200,200,200,200,200,1e-20,1e-20,1e-20,1e-20]] #??????

        maxfe=100
        F=O3.Optimization(O3.Optimize_Layer_10, Target, p0=thickness, bounds=bounds, maxfev=maxfe)
        TB = O1.Layer_10_Optimi(F, wavelength=wavelength)
        TA = O2.Layer_10_Optimi(F, wavelength=wavelength)
        d = {'Layer': ['d1', 'd2', 'd3', 'd4','d5','d6','d7','d8','d9','d10'], 
                'Input': thickness,
                'Optimize':[F[0],round(F[1],2),round(F[2],2),round(F[3],2),round(F[4],2),round(F[5],2),round(F[6],2),round(F[7],2),round(F[8],2),round(F[9],2)]}

        df=pd.DataFrame(data=d, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
            
        print("df", df)
        return T3, TB, TA, df
    def start_fitting(self):
        print("Start..")
        self.menuCalculate.setEnabled(False)
        self.plot_window.setWindowTitle("Fitting...")
        self.table_window.progressBar.show()
    def print_output(self, resuft):
        T3, TB, TA, df = resuft
        self.plot_window.plot_over(self.Pd2Lst(T3), self.Pd2Lst(TB), self.Pd2Lst(TA))
        sub = ResuftWindow(self, df)
        self.mdi.addSubWindow(sub)
        sub.show()
    def progress_fn(self, n):
        print("%d%% done" % n)
    def calculate_errror(self, error):
        self.critical("Can't find a parameter")
    def thread_complete(self):
        print("Finish")
        self.table_window.progressBar.hide()
        self.plot_window.setWindowTitle("Plot Window")
    def Pd2Lst(self, data):
        """Convert Pandas to List"""
        data = [list(data["wavelength"]), list(data["Transmittance"]), list(data["Reflectance"])]
        return data
    def warning(self):
        QMessageBox.warning(
            self,
            'Warning',
            'Please choice 2(s) material.'
        )
    def critical(self, text = 'Can\'t find an parameter .'):
        QMessageBox.critical(
            self,
            'Critical',
            text
        )
    def closeEvent(self, event: QCloseEvent):
        super().closeEvent(event) 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()