# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OptionsWindow(object):
    def setupUi(self, OptionsWindow):
        OptionsWindow.setObjectName("OptionsWindow")
        OptionsWindow.resize(301, 283)
        self.centralwidget = QtWidgets.QWidget(OptionsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setWhatsThis("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.line_duration = QtWidgets.QLineEdit(self.centralwidget)
        self.line_duration.setMaximumSize(QtCore.QSize(39, 16777215))
        self.line_duration.setPlaceholderText("")
        self.line_duration.setObjectName("line_duration")
        self.horizontalLayout_2.addWidget(self.line_duration)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.check_gear = QtWidgets.QCheckBox(self.centralwidget)
        self.check_gear.setObjectName("check_gear")
        self.horizontalLayout.addWidget(self.check_gear)
        self.radio_cube = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_cube.setEnabled(False)
        self.radio_cube.setObjectName("radio_cube")
        self.horizontalLayout.addWidget(self.radio_cube)
        self.radio_equipment = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_equipment.setEnabled(False)
        self.radio_equipment.setObjectName("radio_equipment")
        self.horizontalLayout.addWidget(self.radio_equipment)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.check_inventory = QtWidgets.QCheckBox(self.centralwidget)
        self.check_inventory.setWhatsThis("")
        self.check_inventory.setObjectName("check_inventory")
        self.horizontalLayout_3.addWidget(self.check_inventory)
        self.line_boost_inventory = QtWidgets.QLineEdit(self.centralwidget)
        self.line_boost_inventory.setEnabled(False)
        self.line_boost_inventory.setMaximumSize(QtCore.QSize(27, 16777215))
        self.line_boost_inventory.setObjectName("line_boost_inventory")
        self.horizontalLayout_3.addWidget(self.line_boost_inventory)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.check_merge_inventory = QtWidgets.QCheckBox(self.centralwidget)
        self.check_merge_inventory.setObjectName("check_merge_inventory")
        self.horizontalLayout_4.addWidget(self.check_merge_inventory)
        self.line_merge_inventory = QtWidgets.QLineEdit(self.centralwidget)
        self.line_merge_inventory.setEnabled(False)
        self.line_merge_inventory.setMaximumSize(QtCore.QSize(27, 16777215))
        self.line_merge_inventory.setObjectName("line_merge_inventory")
        self.horizontalLayout_4.addWidget(self.line_merge_inventory)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_5.addWidget(self.checkBox)
        self.check_fruits = QtWidgets.QCheckBox(self.centralwidget)
        self.check_fruits.setWhatsThis("")
        self.check_fruits.setObjectName("check_fruits")
        self.horizontalLayout_5.addWidget(self.check_fruits)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.button_ok = QtWidgets.QPushButton(self.centralwidget)
        self.button_ok.setObjectName("button_ok")
        self.verticalLayout_2.addWidget(self.button_ok, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        OptionsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OptionsWindow)
        QtCore.QMetaObject.connectSlotsByName(OptionsWindow)

    def retranslateUi(self, OptionsWindow):
        _translate = QtCore.QCoreApplication.translate
        OptionsWindow.setWindowTitle(_translate("OptionsWindow", "NGU Script by Satyric - Options"))
        self.label_2.setText(_translate("OptionsWindow", "Duration in seconds to run:"))
        self.line_duration.setText(_translate("OptionsWindow", "300"))
        self.check_gear.setText(_translate("OptionsWindow", "Boost gear"))
        self.radio_cube.setToolTip(_translate("OptionsWindow", "This will only right click the cube"))
        self.radio_cube.setText(_translate("OptionsWindow", "Boost cube"))
        self.radio_equipment.setToolTip(_translate("OptionsWindow", "This will boost all equipment before clicking the cube"))
        self.radio_equipment.setText(_translate("OptionsWindow", "Boost equipment"))
        self.check_inventory.setToolTip(_translate("OptionsWindow", "Put the gear you wish to boost starting in the first slot on inventory page 1. A value of 4 will boost the first 4 slots in the inventory. This overrides the Boost cube setting!"))
        self.check_inventory.setText(_translate("OptionsWindow", "Boost inventory"))
        self.check_merge_inventory.setToolTip(_translate("OptionsWindow", "Put the gear you wish to merge starting in the first slot on inventory page 1. A value of 4 will merge the first 4 slots in the inventory. "))
        self.check_merge_inventory.setText(_translate("OptionsWindow", "Merge inventory"))
        self.checkBox.setText(_translate("OptionsWindow", "CheckBox"))
        self.check_fruits.setToolTip(_translate("OptionsWindow", "This will click \"harvest all max tier fruits\""))
        self.check_fruits.setText(_translate("OptionsWindow", "Eat fruits"))
        self.button_ok.setText(_translate("OptionsWindow", "Ok"))

