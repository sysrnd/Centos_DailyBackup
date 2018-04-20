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
        BackUp.setWindowModality(QtCore.Qt.NonModal)
        BackUp.resize(238, 270)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BackUp.sizePolicy().hasHeightForWidth())
        BackUp.setSizePolicy(sizePolicy)
        BackUp.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        BackUp.setAcceptDrops(False)
        BackUp.setWindowOpacity(0.965)
        textAux = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 3, 14, 255), stop:1 rgba(7, 47, 55, 255));\n"
        textAux = textAux + "\nborder-top-color: rgb(46, 255, 23);\n"
        textAux = textAux + "\ncolor: rgb(8, 255, 239);\n\n"
        textAux = textAux + "QMenuBar{\n    background-color:transparent;\n"
        textAux = textAux + "}\nQMenuBar::item {\n"
        textAux = textAux + "    background-color: transparent;\n}\n"

        BackUp.setStyleSheet(_fromUtf8(textAux))
        BackUp.setDocumentMode(False)
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
        self.btn_config = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_config.sizePolicy().hasHeightForWidth())
        self.btn_config.setSizePolicy(sizePolicy)
        self.btn_config.setMaximumSize(QtCore.QSize(45, 16777215))
        self.btn_config.setObjectName(_fromUtf8("btn_config"))
        self.horizontalLayout.addWidget(self.btn_config)
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
        spacerItem4 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.proBar_Progress = QtGui.QProgressBar(self.frame)
        self.proBar_Progress.setEnabled(False)
        self.proBar_Progress.setProperty("value", 0)
        self.proBar_Progress.setTextVisible(True)
        self.proBar_Progress.setInvertedAppearance(False)
        self.proBar_Progress.setObjectName(_fromUtf8("proBar_Progress"))
        self.horizontalLayout_2.addWidget(self.proBar_Progress)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addWidget(self.frame)
        BackUp.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(BackUp)
        self.statusbar.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BackUp.setStatusBar(self.statusbar)
        self.actionAuto_backup_settings = QtGui.QAction(BackUp)
        self.actionAuto_backup_settings.setObjectName(_fromUtf8("actionAuto_backup_settings"))
        self.actionLog = QtGui.QAction(BackUp)
        self.actionLog.setObjectName(_fromUtf8("actionLog"))

        self.retranslateUi(BackUp)
        QtCore.QMetaObject.connectSlotsByName(BackUp)

    def retranslateUi(self, BackUp):
        BackUp.setWindowTitle(_translate("BackUp", "CentOs Backup", None))
        self.lbl_title.setText(_translate("BackUp", "Server Options", None))
        self.btn_config.setText(_translate("BackUp", "Config", None))
        self.btn_backup.setText(_translate("BackUp", "Backup", None))
        self.btn_clean.setText(_translate("BackUp", "Clean", None))
        self.lbl_feedback.setText(_translate("BackUp", "---------------------------------------------------", None))
        self.actionAuto_backup_settings.setText(_translate("BackUp", "Auto_backup settings", None))
        self.actionLog.setText(_translate("BackUp", "Log", None))

