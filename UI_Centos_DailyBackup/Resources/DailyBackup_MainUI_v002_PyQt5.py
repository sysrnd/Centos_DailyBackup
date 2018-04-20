# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DailyBackup_MainUI_v002.ui'
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


class Ui_BackUp(object):
    def setupUi(self, BackUp):
        BackUp.setObjectName("BackUp")
        BackUp.setWindowModality(QtCore.Qt.NonModal)
        BackUp.resize(238, 270)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
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

        BackUp.setStyleSheet(textAux)
        BackUp.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(BackUp)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_title.setFont(font)
        self.lbl_title.setAutoFillBackground(False)
        self.lbl_title.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.lbl_title.setTextFormat(QtCore.Qt.PlainText)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.verticalLayout.addWidget(self.lbl_title)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_config = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_config.sizePolicy().hasHeightForWidth())
        self.btn_config.setSizePolicy(sizePolicy)
        self.btn_config.setMaximumSize(QtCore.QSize(45, 16777215))
        self.btn_config.setObjectName("btn_config")
        self.horizontalLayout.addWidget(self.btn_config)
        self.btn_backup = QtWidgets.QPushButton(self.centralwidget)
        self.btn_backup.setObjectName("btn_backup")
        self.horizontalLayout.addWidget(self.btn_backup)
        self.btn_clean = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clean.setObjectName("btn_clean")
        self.horizontalLayout.addWidget(self.btn_clean)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.lbl_feedback = QtWidgets.QLabel(self.centralwidget)
        self.lbl_feedback.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.lbl_feedback.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_feedback.setObjectName("lbl_feedback")
        self.verticalLayout.addWidget(self.lbl_feedback)
        spacerItem3 = QtWidgets.QSpacerItem(20, 11, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.proBar_Progress = QtWidgets.QProgressBar(self.frame)
        self.proBar_Progress.setEnabled(False)
        self.proBar_Progress.setProperty("value", 0)
        self.proBar_Progress.setTextVisible(True)
        self.proBar_Progress.setInvertedAppearance(False)
        self.proBar_Progress.setObjectName("proBar_Progress")
        self.horizontalLayout_2.addWidget(self.proBar_Progress)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addWidget(self.frame)
        BackUp.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BackUp)
        self.statusbar.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.statusbar.setObjectName("statusbar")
        BackUp.setStatusBar(self.statusbar)
        self.actionAuto_backup_settings = QtWidgets.QAction(BackUp)
        self.actionAuto_backup_settings.setObjectName("actionAuto_backup_settings")
        self.actionLog = QtWidgets.QAction(BackUp)
        self.actionLog.setObjectName("actionLog")

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

