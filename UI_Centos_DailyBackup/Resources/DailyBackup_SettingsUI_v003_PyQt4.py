# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DailyBackup_SettingsUI_v003.ui'
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

class Ui_settings_dialog(object):
    def setupUi(self, settings_dialog):
        settings_dialog.setObjectName(_fromUtf8("settings_dialog"))
        settings_dialog.resize(325, 372)
        settings_dialog.setWindowOpacity(0.965)
        settings_dialog.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 3, 14, 255), stop:1 rgba(7, 47, 55, 255));\n"
"\n"
"border-top-color: rgb(46, 255, 23);\n"
"\n"
"color: rgb(8, 255, 239);\n"
"\n"
"QMenuBar{\n"
"    background-color:transparent;\n"
"}\n"
"QMenuBar::item {\n"
"    background-color: transparent;\n"
"}"))
        self.verticalLayout = QtGui.QVBoxLayout(settings_dialog)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbl_tittleSettings = QtGui.QLabel(settings_dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_tittleSettings.sizePolicy().hasHeightForWidth())
        self.lbl_tittleSettings.setSizePolicy(sizePolicy)
        self.lbl_tittleSettings.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_tittleSettings.setFont(font)
        self.lbl_tittleSettings.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.lbl_tittleSettings.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_tittleSettings.setObjectName(_fromUtf8("lbl_tittleSettings"))
        self.verticalLayout.addWidget(self.lbl_tittleSettings)
        self.frame = QtGui.QFrame(settings_dialog)
        self.frame.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbl_backupTime = QtGui.QLabel(self.frame)
        self.lbl_backupTime.setObjectName(_fromUtf8("lbl_backupTime"))
        self.horizontalLayout.addWidget(self.lbl_backupTime)
        self.timeEdit_BackupTime = QtGui.QTimeEdit(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit_BackupTime.sizePolicy().hasHeightForWidth())
        self.timeEdit_BackupTime.setSizePolicy(sizePolicy)
        self.timeEdit_BackupTime.setMinimumSize(QtCore.QSize(80, 0))
        self.timeEdit_BackupTime.setAutoFillBackground(False)
        self.timeEdit_BackupTime.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0,);"))
        self.timeEdit_BackupTime.setTime(QtCore.QTime(2, 30, 0))
        self.timeEdit_BackupTime.setObjectName(_fromUtf8("timeEdit_BackupTime"))
        self.horizontalLayout.addWidget(self.timeEdit_BackupTime)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(settings_dialog)
        self.frame_2.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.snBox_frequency = QtGui.QSpinBox(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.snBox_frequency.sizePolicy().hasHeightForWidth())
        self.snBox_frequency.setSizePolicy(sizePolicy)
        self.snBox_frequency.setMinimumSize(QtCore.QSize(50, 0))
        self.snBox_frequency.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.snBox_frequency.setMinimum(1)
        self.snBox_frequency.setMaximum(30)
        self.snBox_frequency.setObjectName(_fromUtf8("snBox_frequency"))
        self.horizontalLayout_2.addWidget(self.snBox_frequency)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtGui.QFrame(settings_dialog)
        self.frame_3.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lbl_origin = QtGui.QLabel(self.frame_3)
        self.lbl_origin.setObjectName(_fromUtf8("lbl_origin"))
        self.horizontalLayout_3.addWidget(self.lbl_origin)
        self.LEdit_source = QtGui.QLineEdit(self.frame_3)
        self.LEdit_source.setObjectName(_fromUtf8("LEdit_source"))
        self.horizontalLayout_3.addWidget(self.LEdit_source)
        self.btn_source = QtGui.QPushButton(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_source.sizePolicy().hasHeightForWidth())
        self.btn_source.setSizePolicy(sizePolicy)
        self.btn_source.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btn_source.setObjectName(_fromUtf8("btn_source"))
        self.horizontalLayout_3.addWidget(self.btn_source)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtGui.QFrame(settings_dialog)
        self.frame_4.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lbl_origin_2 = QtGui.QLabel(self.frame_4)
        self.lbl_origin_2.setObjectName(_fromUtf8("lbl_origin_2"))
        self.horizontalLayout_4.addWidget(self.lbl_origin_2)
        self.LEdit_backup = QtGui.QLineEdit(self.frame_4)
        self.LEdit_backup.setObjectName(_fromUtf8("LEdit_backup"))
        self.horizontalLayout_4.addWidget(self.LEdit_backup)
        self.btn_backup = QtGui.QPushButton(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_backup.sizePolicy().hasHeightForWidth())
        self.btn_backup.setSizePolicy(sizePolicy)
        self.btn_backup.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btn_backup.setObjectName(_fromUtf8("btn_backup"))
        self.horizontalLayout_4.addWidget(self.btn_backup)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtGui.QFrame(settings_dialog)
        self.frame_5.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.btn_acept = QtGui.QPushButton(self.frame_5)
        self.btn_acept.setObjectName(_fromUtf8("btn_acept"))
        self.horizontalLayout_5.addWidget(self.btn_acept)
        spacerItem3 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.btn_Cancel = QtGui.QPushButton(self.frame_5)
        self.btn_Cancel.setObjectName(_fromUtf8("btn_Cancel"))
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

