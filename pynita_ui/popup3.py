# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layouts/ui_code_popuptable_v2.ui',
# licensing of 'layouts/ui_code_popuptable_v2.ui' applies.
#
# Created: Fri Jan 18 10:58:12 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 423)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 320, 389))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.Opti = QtWidgets.QWidget()
        self.Opti.setObjectName("Opti")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Opti)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.Opti)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(250, 290))
        self.frame.setMaximumSize(QtCore.QSize(300, 290))
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(7, 7, 7, 7)
        self.gridLayout.setObjectName("gridLayout")
        self.popup_table = QtWidgets.QTableWidget(self.frame)
        self.popup_table.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popup_table.sizePolicy().hasHeightForWidth())
        self.popup_table.setSizePolicy(sizePolicy)
        self.popup_table.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.popup_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.popup_table.setLineWidth(17)
        self.popup_table.setObjectName("popup_table")
        self.popup_table.setColumnCount(1)
        self.popup_table.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.popup_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.popup_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.popup_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.popup_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.popup_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.popup_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.popup_table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.popup_table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.popup_table.setHorizontalHeaderItem(0, item)
        self.popup_table.horizontalHeader().setStretchLastSection(True)
        self.popup_table.verticalHeader().setDefaultSectionSize(29)
        self.gridLayout.addWidget(self.popup_table, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.popup_pushButton = QtWidgets.QPushButton(self.Opti)
        self.popup_pushButton.setObjectName("popup_pushButton")
        self.horizontalLayout.addWidget(self.popup_pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tabWidget.addTab(self.Opti, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.popup_table.verticalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "bail_thresh", None, -1))
        self.popup_table.verticalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "noise_thresh", None, -1))
        self.popup_table.verticalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "penalty", None, -1))
        self.popup_table.verticalHeaderItem(3).setText(QtWidgets.QApplication.translate("MainWindow", "filter_dist", None, -1))
        self.popup_table.verticalHeaderItem(4).setText(QtWidgets.QApplication.translate("MainWindow", "pct", None, -1))
        self.popup_table.verticalHeaderItem(5).setText(QtWidgets.QApplication.translate("MainWindow", "max_complex", None, -1))
        self.popup_table.verticalHeaderItem(6).setText(QtWidgets.QApplication.translate("MainWindow", "min_complex", None, -1))
        self.popup_table.verticalHeaderItem(7).setText(QtWidgets.QApplication.translate("MainWindow", "filter_opt", None, -1))
        self.popup_table.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "Optimized Parameters", None, -1))
        self.popup_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Save to Configuration File", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Opti), QtWidgets.QApplication.translate("MainWindow", "Optimized Parameters", None, -1))

