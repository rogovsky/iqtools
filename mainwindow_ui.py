# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Sep 16 15:53:45 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 688)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_color = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_color.setObjectName("comboBox_color")
        self.gridLayout.addWidget(self.comboBox_color, 4, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 0, 0, 1, 1)
        self.spinBox_lframes = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_lframes.setMaximum(10000)
        self.spinBox_lframes.setProperty("value", 1024)
        self.spinBox_lframes.setObjectName("spinBox_lframes")
        self.gridLayout.addWidget(self.spinBox_lframes, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBox_nframes = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_nframes.setMaximum(10000)
        self.spinBox_nframes.setProperty("value", 100)
        self.spinBox_nframes.setObjectName("spinBox_nframes")
        self.gridLayout.addWidget(self.spinBox_nframes, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.spinBox_sframes = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_sframes.setMaximum(1500)
        self.spinBox_sframes.setProperty("value", 0)
        self.spinBox_sframes.setObjectName("spinBox_sframes")
        self.gridLayout.addWidget(self.spinBox_sframes, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.lcdNumber_sframes = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber_sframes.setDigitCount(7)
        self.lcdNumber_sframes.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_sframes.setObjectName("lcdNumber_sframes")
        self.gridLayout.addWidget(self.lcdNumber_sframes, 3, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_choose_file = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_choose_file.setObjectName("pushButton_choose_file")
        self.verticalLayout.addWidget(self.pushButton_choose_file)
        self.pushButton_replot = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_replot.setObjectName("pushButton_replot")
        self.verticalLayout.addWidget(self.pushButton_replot)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalSlider_sframes = QtWidgets.QSlider(self.groupBox_3)
        self.verticalSlider_sframes.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_sframes.setInvertedAppearance(False)
        self.verticalSlider_sframes.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSlider_sframes.setTickInterval(1)
        self.verticalSlider_sframes.setObjectName("verticalSlider_sframes")
        self.verticalLayout_3.addWidget(self.verticalSlider_sframes)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mplWidget = MatplotLibWidget(self.groupBox_4)
        self.mplWidget.setObjectName("mplWidget")
        self.gridLayout_3.addWidget(self.mplWidget, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1114, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionReplot = QtWidgets.QAction(MainWindow)
        self.actionReplot.setObjectName("actionReplot")
        self.actionChoose_file = QtWidgets.QAction(MainWindow)
        self.actionChoose_file.setObjectName("actionChoose_file")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionChoose_file)
        self.menuFile.addAction(self.actionReplot)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.spinBox_sframes.valueChanged['int'].connect(self.verticalSlider_sframes.setValue)
        self.verticalSlider_sframes.sliderMoved['int'].connect(self.spinBox_sframes.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "barion"))
        self.groupBox.setTitle(_translate("MainWindow", "Navigation"))
        self.label_20.setText(_translate("MainWindow", "Points per frames:"))
        self.label_2.setText(_translate("MainWindow", "No. of frames:"))
        self.label_3.setText(_translate("MainWindow", "Starting frame:"))
        self.label_21.setText(_translate("MainWindow", "Color map:"))
        self.label.setText(_translate("MainWindow", "Starting time [s]:"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Actions"))
        self.pushButton_choose_file.setText(_translate("MainWindow", "Choose file"))
        self.pushButton_replot.setText(_translate("MainWindow", "Plot"))
        self.groupBox_2.setTitle(_translate("MainWindow", "File Info"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sliders"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Plot"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionReplot.setText(_translate("MainWindow", "Replot"))
        self.actionReplot.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionChoose_file.setText(_translate("MainWindow", "Choose file"))
        self.actionChoose_file.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

from matplotlibwidget import MatplotLibWidget
