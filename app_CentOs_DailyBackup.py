import sys

sys.path.append("Z:/RnD/Pipeline/Maya/Scripts")
sys.path.append("Z:/RnD/SystemTools/Centos_DailyBackup")

#from Modules.Qt import QtCore, QtGui, QtWidgets
from PyQt4 import QtCore, QtGui

from Core_Centos_DailyBackup.Core_DailyBackup import *
from UI_Centos_DailyBackup.Bridge_DailyBackup import *
from UI_Centos_DailyBackup.Resources.DailyBackup_SettingsUI_v003_PyQt4 import *
from UI_Centos_DailyBackup.Resources.DailyBackup_MainUI_v002_PyQt4 import *



class MyApplication(QtGui.QMainWindow, Ui_BackUp):

    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.setupUi(self)

class SettingsApp(QtGui.QDialog, Ui_settings_dialog):
    def __init__(self, parent = None):
        super(SettingsApp, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":

    if QtCore.QCoreApplication.instance() is not None:
        app = QtCore.QCoreApplication.instance()
    else:
        app = QtGui.QApplication(sys.argv)

    # instancia de objetos de ventanas
    window = MyApplication()
    window.setWindowFlags(
        window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

    settingsWin = SettingsApp()

    # instancia del objeto de funciones
    configPath = "/media/Storage/MASTER/"
    if sys.platform == "win32":
        configPath = "Z:/"
    configPath = configPath + "RnD/SystemTools/Centos_DailyBackup/sysconfig_Centos_DailyBackup/"
    configPath = configPath + "ConfigJsonFile.json"
    coreObject = DailyBackupFunctions(pathToConfigFile = configPath)

    bridgObject = Bridge_CentOs_DailyBackup(
        mainWindow=window, configWindow = settingsWin, coreObj = coreObject)
    
    window.show()
    
    try:
        sys.exit(app.exec_())
    except:
        "error al intentar salir"
    

