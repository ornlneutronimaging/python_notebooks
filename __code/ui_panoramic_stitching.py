# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/j35/git/python_notebooks/ui/ui_panoramic_stitching.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(982, 833)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.main_vertical_splitter = QtWidgets.QSplitter(self.centralwidget)
        self.main_vertical_splitter.setOrientation(QtCore.Qt.Vertical)
        self.main_vertical_splitter.setObjectName("main_vertical_splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.main_vertical_splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter_between_previews_and_table = QtWidgets.QSplitter(self.tab)
        self.splitter_between_previews_and_table.setOrientation(QtCore.Qt.Vertical)
        self.splitter_between_previews_and_table.setObjectName("splitter_between_previews_and_table")
        self.splitter_between_previews = QtWidgets.QSplitter(self.splitter_between_previews_and_table)
        self.splitter_between_previews.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_between_previews.setObjectName("splitter_between_previews")
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter_between_previews)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.reference_widget = QtWidgets.QWidget(self.groupBox_2)
        self.reference_widget.setObjectName("reference_widget")
        self.horizontalLayout_3.addWidget(self.reference_widget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.groupBox = QtWidgets.QGroupBox(self.splitter_between_previews)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.target_widget = QtWidgets.QWidget(self.groupBox)
        self.target_widget.setObjectName("target_widget")
        self.horizontalLayout_2.addWidget(self.target_widget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.splitter_between_previews_and_table)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 200))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_4.addWidget(self.splitter_between_previews_and_table)
        self.run_stitching_button = QtWidgets.QPushButton(self.tab)
        self.run_stitching_button.setObjectName("run_stitching_button")
        self.verticalLayout_4.addWidget(self.run_stitching_button)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.listView = QtWidgets.QListView(self.tab_2)
        self.listView.setObjectName("listView")
        self.verticalLayout_6.addWidget(self.listView)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.preview_widget = QtWidgets.QWidget(self.tab_2)
        self.preview_widget.setObjectName("preview_widget")
        self.horizontalLayout_5.addWidget(self.preview_widget)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.up_up_button = QtWidgets.QPushButton(self.groupBox_4)
        self.up_up_button.setText("")
        self.up_up_button.setFlat(True)
        self.up_up_button.setObjectName("up_up_button")
        self.gridLayout.addWidget(self.up_up_button, 0, 3, 1, 1)
        self.up_button = QtWidgets.QPushButton(self.groupBox_4)
        self.up_button.setText("")
        self.up_button.setFlat(True)
        self.up_button.setObjectName("up_button")
        self.gridLayout.addWidget(self.up_button, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.left_left_button = QtWidgets.QPushButton(self.groupBox_4)
        self.left_left_button.setText("")
        self.left_left_button.setFlat(True)
        self.left_left_button.setObjectName("left_left_button")
        self.gridLayout.addWidget(self.left_left_button, 2, 1, 1, 1)
        self.left_button = QtWidgets.QPushButton(self.groupBox_4)
        self.left_button.setStyleSheet("border: None")
        self.left_button.setText("")
        self.left_button.setIconSize(QtCore.QSize(150, 150))
        self.left_button.setAutoDefault(False)
        self.left_button.setDefault(False)
        self.left_button.setFlat(True)
        self.left_button.setObjectName("left_button")
        self.gridLayout.addWidget(self.left_button, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        self.right_button = QtWidgets.QPushButton(self.groupBox_4)
        self.right_button.setText("")
        self.right_button.setFlat(True)
        self.right_button.setObjectName("right_button")
        self.gridLayout.addWidget(self.right_button, 2, 4, 1, 1)
        self.right_right_button = QtWidgets.QPushButton(self.groupBox_4)
        self.right_right_button.setText("")
        self.right_right_button.setFlat(True)
        self.right_right_button.setObjectName("right_right_button")
        self.gridLayout.addWidget(self.right_right_button, 2, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 6, 1, 1)
        self.down_button = QtWidgets.QPushButton(self.groupBox_4)
        self.down_button.setText("")
        self.down_button.setFlat(True)
        self.down_button.setObjectName("down_button")
        self.gridLayout.addWidget(self.down_button, 3, 3, 1, 1)
        self.down_down_button = QtWidgets.QPushButton(self.groupBox_4)
        self.down_down_button.setText("")
        self.down_down_button.setFlat(True)
        self.down_down_button.setObjectName("down_down_button")
        self.gridLayout.addWidget(self.down_down_button, 4, 3, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_4.addWidget(self.spinBox)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_2.setMinimum(5)
        self.spinBox_2.setMaximum(100)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_4.addWidget(self.spinBox_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox_3 = QtWidgets.QGroupBox(self.main_vertical_splitter)
        self.groupBox_3.setBaseSize(QtCore.QSize(0, 100))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.stitched_table = QtWidgets.QTableWidget(self.groupBox_3)
        self.stitched_table.setBaseSize(QtCore.QSize(0, 100))
        self.stitched_table.setObjectName("stitched_table")
        self.stitched_table.setColumnCount(0)
        self.stitched_table.setRowCount(0)
        self.horizontalLayout_6.addWidget(self.stitched_table)
        self.stitched_widget = QtWidgets.QWidget(self.groupBox_3)
        self.stitched_widget.setObjectName("stitched_widget")
        self.horizontalLayout_6.addWidget(self.stitched_widget)
        self.verticalLayout_8.addWidget(self.main_vertical_splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_button.setObjectName("export_button")
        self.horizontalLayout.addWidget(self.export_button)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport_ROIs = QtWidgets.QAction(MainWindow)
        self.actionImport_ROIs.setObjectName("actionImport_ROIs")
        self.actionExport_ROIs = QtWidgets.QAction(MainWindow)
        self.actionExport_ROIs.setObjectName("actionExport_ROIs")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.cancel_button.clicked.connect(MainWindow.cancel_clicked)
        self.export_button.clicked.connect(MainWindow.apply_clicked)
        self.tableWidget.itemSelectionChanged.connect(MainWindow.table_widget_selection_changed)
        self.run_stitching_button.clicked.connect(MainWindow.run_stitching_button_clicked)
        self.left_button.pressed.connect(MainWindow.left_button_pressed)
        self.left_button.released.connect(MainWindow.left_button_released)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Reference Image"))
        self.groupBox.setTitle(_translate("MainWindow", "Target Image"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Reference Images"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Target Images"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        self.run_stitching_button.setText(_translate("MainWindow", "Run Stitching "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Step 1"))
        self.label.setText(_translate("MainWindow", "File Names"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Manual Mode"))
        self.label_2.setText(_translate("MainWindow", ">"))
        self.label_3.setText(_translate("MainWindow", ":"))
        self.label_5.setText(_translate("MainWindow", ">>"))
        self.label_4.setText(_translate("MainWindow", ":"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Step 2"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Stiched Image"))
        self.cancel_button.setText(_translate("MainWindow", "Close"))
        self.export_button.setText(_translate("MainWindow", "Export ..."))
        self.actionImport_ROIs.setText(_translate("MainWindow", "Import ..."))
        self.actionExport_ROIs.setText(_translate("MainWindow", "Export ..."))

