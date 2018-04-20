from PyQt5 import QtCore, QtGui

class Bridge_CentOs_DailyBackup(object):

	def __init__(self, mainWindow, configWindow, coreObj):
		"""
		"""
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
		self.lEdit_source = configWindow.LEdit_source
		self.lEdit_backup = configWindow.LEdit_backup
		self.btn_sourcePath = configWindow.btn_source
		self.btn_backupPath = configWindow.btn_backup

		# Connecting Main Window
	
		# Connecting config window
		tSource = "Select source folder path"
		self.btn_sourcePath.clicked.connect(
			self.getFileP(title = tSource, el = self.lEdit_source))

		tBack = "Select back folder path"
		self.btn_backupPath.clicked.connect(
			self.getFileP(title = tBack, el = self.lEdit_backup))



	def getFileP(self, title, el):
		name = QtGui.QfileDialog.getOpenFileName(self, title)[0]


	def PopulateUI(self):
		"""
		"""

	def SaveConfig(self):
		"""
		"""
