import sys

from Modules.Qt import QtCore, QtGui, QtWidgets

class MyApplication(QtWidgets.QMainWindow, Ui_window_bsNamer):

	def __init__(self, parent=None):
		super(MyApplication, self).__init__(parent)
		self.setupUi(self)

if __name__ != "__main__":
	try:
		app = QtWidgets.QApplication(sys.argv)
	except:
		app = QtCore.QCoreApplication.instance()
	window = MyApplication()
	window.setWindowFlags(
		window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
	
	interfaceMacho = bsNamesBridge(window=window)
	window.show()

	try:
		sys.exit(app.exec_())
	except:
		"error al intentar salir"

