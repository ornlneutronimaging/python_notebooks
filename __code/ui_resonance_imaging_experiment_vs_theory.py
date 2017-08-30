# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/j35/git/IPTS/notebooks/ui/ui_resonance_imaging_experiment_vs_theory.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1014, 494)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.widget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_5.addWidget(self.widget)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.file_index_ratio_button = QtGui.QRadioButton(self.groupBox)
        self.file_index_ratio_button.setChecked(True)
        self.file_index_ratio_button.setObjectName(_fromUtf8("file_index_ratio_button"))
        self.horizontalLayout_8.addWidget(self.file_index_ratio_button)
        self.tof_radio_button = QtGui.QRadioButton(self.groupBox)
        self.tof_radio_button.setObjectName(_fromUtf8("tof_radio_button"))
        self.horizontalLayout_8.addWidget(self.tof_radio_button)
        self.lambda_radio_button = QtGui.QRadioButton(self.groupBox)
        self.lambda_radio_button.setObjectName(_fromUtf8("lambda_radio_button"))
        self.horizontalLayout_8.addWidget(self.lambda_radio_button)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.list_to_plot_widget = QtGui.QListWidget(self.centralwidget)
        self.list_to_plot_widget.setMinimumSize(QtCore.QSize(200, 100))
        self.list_to_plot_widget.setMaximumSize(QtCore.QSize(300, 300))
        self.list_to_plot_widget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.list_to_plot_widget.setObjectName(_fromUtf8("list_to_plot_widget"))
        self.verticalLayout.addWidget(self.list_to_plot_widget)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.distance_source_detector_value = QtGui.QLineEdit(self.centralwidget)
        self.distance_source_detector_value.setMinimumSize(QtCore.QSize(80, 0))
        self.distance_source_detector_value.setMaximumSize(QtCore.QSize(80, 16777215))
        self.distance_source_detector_value.setObjectName(_fromUtf8("distance_source_detector_value"))
        self.horizontalLayout.addWidget(self.distance_source_detector_value)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.detector_offset_value = QtGui.QLineEdit(self.centralwidget)
        self.detector_offset_value.setMinimumSize(QtCore.QSize(80, 0))
        self.detector_offset_value.setMaximumSize(QtCore.QSize(80, 16777215))
        self.detector_offset_value.setObjectName(_fromUtf8("detector_offset_value"))
        self.horizontalLayout_2.addWidget(self.detector_offset_value)
        self.detector_offset_units = QtGui.QLabel(self.centralwidget)
        self.detector_offset_units.setObjectName(_fromUtf8("detector_offset_units"))
        self.horizontalLayout_2.addWidget(self.detector_offset_units)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(130, 16777215))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.time_spectra_file = QtGui.QLabel(self.centralwidget)
        self.time_spectra_file.setObjectName(_fromUtf8("time_spectra_file"))
        self.horizontalLayout_3.addWidget(self.time_spectra_file)
        self.time_spectra_file_browse_button = QtGui.QPushButton(self.centralwidget)
        self.time_spectra_file_browse_button.setMinimumSize(QtCore.QSize(100, 0))
        self.time_spectra_file_browse_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.time_spectra_file_browse_button.setObjectName(_fromUtf8("time_spectra_file_browse_button"))
        self.horizontalLayout_3.addWidget(self.time_spectra_file_browse_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.done_button = QtGui.QPushButton(self.centralwidget)
        self.done_button.setObjectName(_fromUtf8("done_button"))
        self.verticalLayout_2.addWidget(self.done_button)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1014, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.done_button, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.done_button_clicked)
        QtCore.QObject.connect(self.distance_source_detector_value, QtCore.SIGNAL(_fromUtf8("editingFinished()")), MainWindow.distance_source_detector_validated)
        QtCore.QObject.connect(self.detector_offset_value, QtCore.SIGNAL(_fromUtf8("returnPressed()")), MainWindow.detector_offset_validated)
        QtCore.QObject.connect(self.time_spectra_file_browse_button, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.time_spectra_file_browse_button_clicked)
        QtCore.QObject.connect(self.file_index_ratio_button, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.radio_button_clicked)
        QtCore.QObject.connect(self.tof_radio_button, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.radio_button_clicked)
        QtCore.QObject.connect(self.lambda_radio_button, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.radio_button_clicked)
        QtCore.QObject.connect(self.list_to_plot_widget, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), MainWindow.plot_selection_changed)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Xaxis", None))
        self.file_index_ratio_button.setText(_translate("MainWindow", "File Index", None))
        self.tof_radio_button.setText(_translate("MainWindow", "TOF (us)", None))
        self.lambda_radio_button.setText(_translate("MainWindow", "lambda (A)", None))
        self.label_4.setText(_translate("MainWindow", "Plot Selection", None))
        self.label.setText(_translate("MainWindow", "Distance Source-Detector", None))
        self.label_2.setText(_translate("MainWindow", "m", None))
        self.label_3.setText(_translate("MainWindow", "Detector Offset", None))
        self.detector_offset_units.setText(_translate("MainWindow", "us", None))
        self.label_5.setText(_translate("MainWindow", "Time Spectra File:", None))
        self.time_spectra_file.setText(_translate("MainWindow", "N/A", None))
        self.time_spectra_file_browse_button.setText(_translate("MainWindow", "Browse ...", None))
        self.done_button.setText(_translate("MainWindow", "DONE", None))

