# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mte90/Desktop/Prog/Plessc/MainWindow.ui'
#
# Created: Wed Feb  6 00:35:36 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(503, 389)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.verticalGroupBox.setObjectName(_fromUtf8("verticalGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.setMinify = QtGui.QRadioButton(self.verticalGroupBox)
        self.setMinify.setObjectName(_fromUtf8("setMinify"))
        self.verticalLayout.addWidget(self.setMinify)
        self.setYUI = QtGui.QRadioButton(self.verticalGroupBox)
        self.setYUI.setChecked(True)
        self.setYUI.setObjectName(_fromUtf8("setYUI"))
        self.verticalLayout.addWidget(self.setYUI)
        self.horizontalLayout_2.addWidget(self.verticalGroupBox)
        self.verticalGroupBox1 = QtGui.QGroupBox(self.centralwidget)
        self.verticalGroupBox1.setObjectName(_fromUtf8("verticalGroupBox1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalGroupBox1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.setStandard = QtGui.QRadioButton(self.verticalGroupBox1)
        self.setStandard.setChecked(True)
        self.setStandard.setObjectName(_fromUtf8("setStandard"))
        self.verticalLayout_2.addWidget(self.setStandard)
        self.setBoth = QtGui.QRadioButton(self.verticalGroupBox1)
        self.setBoth.setObjectName(_fromUtf8("setBoth"))
        self.verticalLayout_2.addWidget(self.setBoth)
        self.horizontalLayout_2.addWidget(self.verticalGroupBox1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.info = QtGui.QLabel(self.centralwidget)
        self.info.setMinimumSize(QtCore.QSize(400, 0))
        self.info.setText(_fromUtf8(""))
        self.info.setObjectName(_fromUtf8("info"))
        self.horizontalLayout.addWidget(self.info)
        self.compile = QtGui.QPushButton(self.centralwidget)
        self.compile.setObjectName(_fromUtf8("compile"))
        self.horizontalLayout.addWidget(self.compile)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.inputChoose = QtGui.QPushButton(self.centralwidget)
        self.inputChoose.setObjectName(_fromUtf8("inputChoose"))
        self.gridLayout_3.addWidget(self.inputChoose, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.inputFile = QtGui.QLineEdit(self.centralwidget)
        self.inputFile.setObjectName(_fromUtf8("inputFile"))
        self.gridLayout_3.addWidget(self.inputFile, 0, 1, 1, 1)
        self.outputFile = QtGui.QLineEdit(self.centralwidget)
        self.outputFile.setObjectName(_fromUtf8("outputFile"))
        self.gridLayout_3.addWidget(self.outputFile, 1, 1, 1, 1)
        self.outputChoose = QtGui.QPushButton(self.centralwidget)
        self.outputChoose.setObjectName(_fromUtf8("outputChoose"))
        self.gridLayout_3.addWidget(self.outputChoose, 1, 2, 1, 1)
        self.inputEdit = QtGui.QPushButton(self.centralwidget)
        self.inputEdit.setObjectName(_fromUtf8("inputEdit"))
        self.gridLayout_3.addWidget(self.inputEdit, 0, 3, 1, 1)
        self.outputLog = QtGui.QPushButton(self.centralwidget)
        self.outputLog.setObjectName(_fromUtf8("outputLog"))
        self.gridLayout_3.addWidget(self.outputLog, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.log = QtWebKit.QWebView(self.centralwidget)
        self.log.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.log.setObjectName(_fromUtf8("log"))
        self.gridLayout.addWidget(self.log, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 503, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSetting = QtGui.QMenu(self.menubar)
        self.menuSetting.setObjectName(_fromUtf8("menuSetting"))
        self.menuInfo = QtGui.QMenu(self.menubar)
        self.menuInfo.setObjectName(_fromUtf8("menuInfo"))
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout_Kless = QtGui.QAction(MainWindow)
        self.actionAbout_Kless.setObjectName(_fromUtf8("actionAbout_Kless"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.menuSetting.addAction(self.actionSettings)
        self.menuInfo.addAction(self.actionAbout_Kless)
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalGroupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Option ", None, QtGui.QApplication.UnicodeUTF8))
        self.setMinify.setText(QtGui.QApplication.translate("MainWindow", "Minify", None, QtGui.QApplication.UnicodeUTF8))
        self.setYUI.setText(QtGui.QApplication.translate("MainWindow", "YUI Compress", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalGroupBox1.setTitle(QtGui.QApplication.translate("MainWindow", "Save Method", None, QtGui.QApplication.UnicodeUTF8))
        self.setStandard.setText(QtGui.QApplication.translate("MainWindow", "Only minified version", None, QtGui.QApplication.UnicodeUTF8))
        self.setBoth.setText(QtGui.QApplication.translate("MainWindow", "Standard and minified version", None, QtGui.QApplication.UnicodeUTF8))
        self.compile.setText(QtGui.QApplication.translate("MainWindow", "Compile it!", None, QtGui.QApplication.UnicodeUTF8))
        self.inputChoose.setText(QtGui.QApplication.translate("MainWindow", "Choose", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Input File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Output File", None, QtGui.QApplication.UnicodeUTF8))
        self.outputChoose.setText(QtGui.QApplication.translate("MainWindow", "Choose", None, QtGui.QApplication.UnicodeUTF8))
        self.inputEdit.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.outputLog.setText(QtGui.QApplication.translate("MainWindow", "Open Log", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSetting.setTitle(QtGui.QApplication.translate("MainWindow", "Setting", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInfo.setTitle(QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Kless.setText(QtGui.QApplication.translate("MainWindow", "About Kless", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
