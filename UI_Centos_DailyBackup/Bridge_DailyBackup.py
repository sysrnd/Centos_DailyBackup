# -*- coding: utf-8 -*-

#from Modules.Qt import QtCore, QtGui, QtWidgets
from PyQt4 import QtCore, QtGui

class Bridge_CentOs_DailyBackup(object):

    def __init__(self, mainWindow, configWindow, coreObj):
        """
        """
        self.coreActions = coreObj

        self.mainWindow = mainWindow
        self.configWindow = configWindow

        # MAIN WINDOW
        # Buttons
        self.main_btn_config = mainWindow.btn_config
        self.main_btn_backup = mainWindow.btn_backup
        self.main_btn_clean = mainWindow.btn_clean
        # Prograss bar
        self.main_proBar_progress = mainWindow.proBar_Progress

        # Config window
        self.set_tEdit_backupTime = configWindow.timeEdit_BackupTime
        self.set_sbBox_frequency = configWindow.snBox_frequency
        self.set_lEdit_source = configWindow.LEdit_source
        self.set_lEdit_backup = configWindow.LEdit_backup
        self.set_btn_sourcePath = configWindow.btn_source
        self.set_btn_backupPath = configWindow.btn_backup
        self.set_btn_accept = configWindow.btn_acept
        self.set_btn_cancel = configWindow.btn_Cancel

        # Connecting Main Window
        self.main_btn_config.clicked.connect(self.OpenConfig)

        # Connecting config window
        self.set_btn_sourcePath.clicked.connect(self.winSource)
        self.set_btn_backupPath.clicked.connect(self.winBack)
        self.set_btn_accept.clicked.connect(self.ConfigAccept)
        self.set_btn_cancel.clicked.connect(self.ConfigCancel)

    def winSource(self):
        tSource = "Source folder"
        nm = self.getFileP(title = tSource, el = self.set_lEdit_source)
        self.set_lEdit_source.setText(nm)


    def winBack(self):
        tBack = "Backup folder"
        nm = self.getFileP(title = tBack, el = self.set_lEdit_backup)
        self.set_lEdit_backup.setText(nm)

    def getFileP(self, title, el):
        name = unicode (QtGui.QFileDialog.getExistingDirectory(caption= title))
        return name

        

    def PopulateUI(self):
        """
        """

    def SaveConfig(self):
        dataP = self.set_lEdit_source.text()
        backupP = self.set_lEdit_backup.text()

        dataP = unicode(dataP).replace('\\', '/')
        backupP = unicode(backupP).replace('\\', '/')
        timeH = "Min Hours"
        timeH = self.set_tEdit_backupTime.dateTime().toString("dd MMM YYYY  hh:mm").split(" ")[-1]
        timeM = timeH.split(":")[0]
        timeH = timeH.split(":")[1]

        frecuency_Qt = str(self.set_sbBox_frequency.value())

        data = {
            self.coreActions.Frequency: frecuency_Qt,
            self.coreActions.DataPathKey: dataP,
            self.coreActions.BackupPathKey: backupP,
            self.coreActions.TimeHour: str(timeH),
            self.coreActions.TimeMin: str(timeM)
            }

        self.coreActions.SaveConfigFile(dataX = data)

    def OpenConfig(self):
        self.configWindow.show()
        self.mainWindow.hide()

    def ConfigAccept(self):
        self.SaveConfig()
        self.configWindow.hide()
        self.mainWindow.show()

    def ConfigCancel(self):
        self.configWindow.hide()
        self.mainWindow.show()
