# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DailyBackup_MainUI_v002.ui'
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

class Ui_BackUp(object):
    def setupUi(self, BackUp):
        BackUp.setObjectName(_fromUtf8("BackUp"))
        BackUp.resize(247, 248)
        BackUp.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 3, 14, 255), stop:1 rgba(7, 47, 55, 255));\n"
"border-top-color: rgb(46, 255, 23);\n"
"color: rgb(8, 255, 239);"))
        self.centralwidget = QtGui.QWidget(BackUp)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.lbl_title = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_title.setFont(font)
        self.lbl_title.setAutoFillBackground(False)
        self.lbl_title.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.lbl_title.setTextFormat(QtCore.Qt.PlainText)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName(_fromUtf8("lbl_title"))
        self.verticalLayout.addWidget(self.lbl_title)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_backup = QtGui.QPushButton(self.centralwidget)
        self.btn_backup.setObjectName(_fromUtf8("btn_backup"))
        self.horizontalLayout.addWidget(self.btn_backup)
        self.btn_clean = QtGui.QPushButton(self.centralwidget)
        self.btn_clean.setObjectName(_fromUtf8("btn_clean"))
        self.horizontalLayout.addWidget(self.btn_clean)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.lbl_feedback = QtGui.QLabel(self.centralwidget)
        self.lbl_feedback.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.lbl_feedback.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_feedback.setObjectName(_fromUtf8("lbl_feedback"))
        self.verticalLayout.addWidget(self.lbl_feedback)
        spacerItem3 = QtGui.QSpacerItem(20, 11, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.proBar_Progress = QtGui.QProgressBar(self.centralwidget)
        self.proBar_Progress.setEnabled(False)
        self.proBar_Progress.setProperty("value", 0)
        self.proBar_Progress.setTextVisible(True)
        self.proBar_Progress.setInvertedAppearance(False)
        self.proBar_Progress.setObjectName(_fromUtf8("proBar_Progress"))
        self.verticalLayout.addWidget(self.proBar_Progress)
        spacerItem4 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        BackUp.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(BackUp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 247, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOpciones = QtGui.QMenu(self.menubar)
        self.menuOpciones.setObjectName(_fromUtf8("menuOpciones"))
        BackUp.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(BackUp)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BackUp.setStatusBar(self.statusbar)
        self.actionAuto_backup_settings = QtGui.QAction(BackUp)
        self.actionAuto_backup_settings.setObjectName(_fromUtf8("actionAuto_backup_settings"))
        self.actionLog = QtGui.QAction(BackUp)
        self.actionLog.setObjectName(_fromUtf8("actionLog"))
        self.menuOpciones.addAction(self.actionAuto_backup_settings)
        self.menuOpciones.addSeparator()
        self.menuOpciones.addAction(self.actionLog)
        self.menubar.addAction(self.menuOpciones.menuAction())

        self.retranslateUi(BackUp)
        QtCore.QMetaObject.connectSlotsByName(BackUp)

    def retranslateUi(self, BackUp):
        BackUp.setWindowTitle(_translate("BackUp", "MainWindow", None))
        self.lbl_title.setText(_translate("BackUp", "Server Options", None))
        self.btn_backup.setText(_translate("BackUp", "Backup", None))
        self.btn_clean.setText(_translate("BackUp", "Clean", None))
        self.lbl_feedback.setText(_translate("BackUp", "---------------------------------------------------", None))
        self.menuOpciones.setTitle(_translate("BackUp", "Opciones", None))
        self.actionAuto_backup_settings.setText(_translate("BackUp", "Auto_backup settings", None))
        self.actionLog.setText(_translate("BackUp", "Log", None))

