# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DailyBackup_SettingsUI_v002.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from Modules.Qt import QtCore, QtGui, QtWidgets

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)

except AttributeError:
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig)

class Ui_settings_dialog(object):
    def setupUi(self, settings_dialog):
        settings_dialog.setObjectName("settings_dialog")
        settings_dialog.resize(325, 372)
        settings_dialog.setWindowOpacity(0.965)
        auxText = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, "
        auxText = auxText + "stop:0 rgba(0, 3, 14, 255), stop:1 rgba(7, 47, 55, 255));\n"
        auxText = auxText + "\nborder-top-color: rgb(46, 255, 23);\n"
        auxText = auxText + "\ncolor: rgb(8, 255, 239);\n"
        auxText = auxText + "\nQMenuBar{\n    background-color:transparent;\n"
        auxText = auxText + "}\nQMenuBar::item {\n    background-color: transparent;\n}"
        settings_dialog.setStyleSheet(auxText)
        self.verticalLayout = QtWidgets.QVBoxLayout(settings_dialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_tittleSettings = QtWidgets.QLabel(settings_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_tittleSettings.sizePolicy().hasHeightForWidth())
        self.lbl_tittleSettings.setSizePolicy(sizePolicy)
        self.lbl_tittleSettings.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_tittleSettings.setFont(font)
        self.lbl_tittleSettings.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.lbl_tittleSettings.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_tittleSettings.setObjectName("lbl_tittleSettings")
        self.verticalLayout.addWidget(self.lbl_tittleSettings)
        self.frame = QtWidgets.QFrame(settings_dialog)
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbl_backupTime = QtWidgets.QLabel(self.frame)
        self.lbl_backupTime.setObjectName("lbl_backupTime")
        self.horizontalLayout.addWidget(self.lbl_backupTime)
        self.timeEdit_BackupTime = QtWidgets.QTimeEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_BackupTime.sizePolicy().hasHeightForWidth())
        self.timeEdit_BackupTime.setSizePolicy(sizePolicy)
        self.timeEdit_BackupTime.setMinimumSize(QtCore.QSize(80, 0))
        self.timeEdit_BackupTime.setAutoFillBackground(False)
        self.timeEdit_BackupTime.setStyleSheet("background-color: rgb(0, 0, 0,);")
        self.timeEdit_BackupTime.setTime(QtCore.QTime(2, 30, 0))
        self.timeEdit_BackupTime.setObjectName("timeEdit_BackupTime")
        self.horizontalLayout.addWidget(self.timeEdit_BackupTime)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(settings_dialog)
        self.frame_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.snBox_frequency = QtWidgets.QSpinBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.snBox_frequency.sizePolicy().hasHeightForWidth())
        self.snBox_frequency.setSizePolicy(sizePolicy)
        self.snBox_frequency.setMinimumSize(QtCore.QSize(50, 0))
        self.snBox_frequency.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.snBox_frequency.setObjectName("snBox_frequency")
        self.horizontalLayout_2.addWidget(self.snBox_frequency)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(settings_dialog)
        self.frame_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_origin = QtWidgets.QLabel(self.frame_3)
        self.lbl_origin.setObjectName("lbl_origin")
        self.horizontalLayout_3.addWidget(self.lbl_origin)
        self.LEdit_source = QtWidgets.QLineEdit(self.frame_3)
        self.LEdit_source.setObjectName("LEdit_source")
        self.horizontalLayout_3.addWidget(self.LEdit_source)
        self.btn_source = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_source.sizePolicy().hasHeightForWidth())
        self.btn_source.setSizePolicy(sizePolicy)
        self.btn_source.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btn_source.setObjectName("btn_source")
        self.horizontalLayout_3.addWidget(self.btn_source)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(settings_dialog)
        self.frame_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_origin_2 = QtWidgets.QLabel(self.frame_4)
        self.lbl_origin_2.setObjectName("lbl_origin_2")
        self.horizontalLayout_4.addWidget(self.lbl_origin_2)
        self.LEdit_backup = QtWidgets.QLineEdit(self.frame_4)
        self.LEdit_backup.setObjectName("LEdit_backup")
        self.horizontalLayout_4.addWidget(self.LEdit_backup)
        self.btn_backup = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_backup.sizePolicy().hasHeightForWidth())
        self.btn_backup.setSizePolicy(sizePolicy)
        self.btn_backup.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btn_backup.setObjectName("btn_backup")
        self.horizontalLayout_4.addWidget(self.btn_backup)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(settings_dialog)
        self.frame_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.btn_acept = QtWidgets.QPushButton(self.frame_5)
        self.btn_acept.setObjectName("btn_acept")
        self.horizontalLayout_5.addWidget(self.btn_acept)
        spacerItem3 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.btn_Cancel = QtWidgets.QPushButton(self.frame_5)
        self.btn_Cancel.setObjectName("btn_Cancel")
        self.horizontalLayout_5.addWidget(self.btn_Cancel)
        self.verticalLayout.addWidget(self.frame_5)

        self.retranslateUi(settings_dialog)
        QtCore.QMetaObject.connectSlotsByName(settings_dialog)

    def retranslateUi(self, settings_dialog):
        settings_dialog.setWindowTitle(_translate("settings_dialog", "Dialog", None))
        self.lbl_tittleSettings.setText(_translate("settings_dialog", "      Backup settings", None))
        self.lbl_backupTime.setText(_translate("settings_dialog", "Backup time", None))
        self.label.setText(_translate("settings_dialog", "Frequency", None))
        self.lbl_origin.setText(_translate("settings_dialog", "Source", None))
        self.btn_source.setText(_translate("settings_dialog", "...", None))
        self.lbl_origin_2.setText(_translate("settings_dialog", "Backup", None))
        self.btn_backup.setText(_translate("settings_dialog", "...", None))
        self.btn_acept.setText(_translate("settings_dialog", "&Accept", None))
        self.btn_Cancel.setText(_translate("settings_dialog", "&Cancel", None))
