# Form implementation generated from reading ui file 'c:\Users\letan\OneDrive\Máy tính\Macleod2\uic\main.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 785)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\letan\\OneDrive\\Máy tính\\Macleod2\\uic\\../icon/icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(10, 0, 1421, 720))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy)
        self.mdiArea.setMaximumSize(QtCore.QSize(1920, 1080))
        self.mdiArea.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.mdiArea.setLineWidth(3)
        self.mdiArea.setActivationOrder(QtWidgets.QMdiArea.WindowOrder.CreationOrder)
        self.mdiArea.setViewMode(QtWidgets.QMdiArea.ViewMode.SubWindowView)
        self.mdiArea.setDocumentMode(False)
        self.mdiArea.setObjectName("mdiArea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 26))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(self.menuFile)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\letan\\OneDrive\\Máy tính\\Macleod2\\uic\\../icon/new_folder.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menuNew.setIcon(icon1)
        self.menuNew.setObjectName("menuNew")
        self.menuOpen = QtWidgets.QMenu(self.menuFile)
        self.menuOpen.setObjectName("menuOpen")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFormula_2 = QtWidgets.QMenu(self.menuEdit)
        self.menuFormula_2.setObjectName("menuFormula_2")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuParameter = QtWidgets.QMenu(self.menubar)
        self.menuParameter.setObjectName("menuParameter")
        self.menuRefinerment = QtWidgets.QMenu(self.menuParameter)
        self.menuRefinerment.setObjectName("menuRefinerment")
        self.menuPerformance = QtWidgets.QMenu(self.menubar)
        self.menuPerformance.setObjectName("menuPerformance")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.toolBar.setFont(font)
        self.toolBar.setIconSize(QtCore.QSize(20, 20))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionNewDesign = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\letan\\OneDrive\\Máy tính\\Macleod2\\uic\\../icon/icons/address-book-open.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionNewDesign.setIcon(icon2)
        self.actionNewDesign.setObjectName("actionNewDesign")
        self.actionOpen = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\letan\\OneDrive\\Máy tính\\Macleod2\\uic\\../icon/open_folder.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon3)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNewMaterial = QtGui.QAction(MainWindow)
        self.actionNewMaterial.setObjectName("actionNewMaterial")
        self.actionInsert_Row = QtGui.QAction(MainWindow)
        self.actionInsert_Row.setObjectName("actionInsert_Row")
        self.actionRemove_Layer = QtGui.QAction(MainWindow)
        self.actionRemove_Layer.setObjectName("actionRemove_Layer")
        self.actionTest = QtGui.QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.actionPlot = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\letan\\OneDrive\\Máy tính\\Macleod2\\uic\\../icon/icons/chart--pencil.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPlot.setIcon(icon4)
        self.actionPlot.setObjectName("actionPlot")
        self.actionTargets = QtGui.QAction(MainWindow)
        self.actionTargets.setObjectName("actionTargets")
        self.actionOpenTargets = QtGui.QAction(MainWindow)
        self.actionOpenTargets.setObjectName("actionOpenTargets")
        self.actionBeforeFormula = QtGui.QAction(MainWindow)
        self.actionBeforeFormula.setObjectName("actionBeforeFormula")
        self.actionAfterFormula = QtGui.QAction(MainWindow)
        self.actionAfterFormula.setObjectName("actionAfterFormula")
        self.actionCaculator = QtGui.QAction(MainWindow)
        self.actionCaculator.setObjectName("actionCaculator")
        self.menuNew.addAction(self.actionNewDesign)
        self.menuNew.addAction(self.actionNewMaterial)
        self.menuOpen.addAction(self.actionOpenTargets)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.actionTest)
        self.menuFormula_2.addAction(self.actionBeforeFormula)
        self.menuFormula_2.addAction(self.actionAfterFormula)
        self.menuEdit.addAction(self.actionInsert_Row)
        self.menuEdit.addAction(self.actionRemove_Layer)
        self.menuEdit.addAction(self.menuFormula_2.menuAction())
        self.menuRefinerment.addAction(self.actionTargets)
        self.menuParameter.addAction(self.menuRefinerment.menuAction())
        self.menuPerformance.addAction(self.actionPlot)
        self.menuPerformance.addAction(self.actionCaculator)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuParameter.menuAction())
        self.menubar.addAction(self.menuPerformance.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionNewDesign)
        self.toolBar.addAction(self.actionPlot)
        self.toolBar.addAction(self.actionTest)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mr.Ngoc App"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuNew.setTitle(_translate("MainWindow", "New.."))
        self.menuOpen.setTitle(_translate("MainWindow", "Open.."))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuFormula_2.setTitle(_translate("MainWindow", "Formula..."))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuParameter.setTitle(_translate("MainWindow", "Parameters"))
        self.menuRefinerment.setTitle(_translate("MainWindow", "Refinerment"))
        self.menuPerformance.setTitle(_translate("MainWindow", "Performance"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNewDesign.setText(_translate("MainWindow", "Design"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionNewMaterial.setText(_translate("MainWindow", "Material"))
        self.actionInsert_Row.setText(_translate("MainWindow", "Insert Layer"))
        self.actionRemove_Layer.setText(_translate("MainWindow", "Remove Layer"))
        self.actionTest.setText(_translate("MainWindow", "Test"))
        self.actionPlot.setText(_translate("MainWindow", "Plot"))
        self.actionTargets.setText(_translate("MainWindow", "Targets"))
        self.actionOpenTargets.setText(_translate("MainWindow", "Targets"))
        self.actionBeforeFormula.setText(_translate("MainWindow", "Before"))
        self.actionAfterFormula.setText(_translate("MainWindow", "After"))
        self.actionCaculator.setText(_translate("MainWindow", "Caculator"))
