import sys
from PyQt4 import QtGui, QtCore

# creating a window object that inherit from QtGui
class Window(QtGui.QMainWindow):
	# the init is the initial set of methods that always run when window is called
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle("PyQt tuts!")
		self.setWindowIcon(QtGui.QIcon("pythonLogo.png"))

		# creates a action to be used in the file menu
		extractAction = QtGui.QAction("&Get out the CHOPPAH! ! ! ! !", self)
		extractAction.setShortcut("Ctrl+q")
		extractAction.setStatusTip("Leave The App")
		extractAction.triggered.connect(self.close_application)

		# created my own action that does nothing right now
		exAct = QtGui.QAction("what",self)


		#self.statusBar()

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)
		

		editMenu = mainMenu.addMenu('&Edit')
		editMenu.addAction(exAct)



		self.home()

	def home(self):
		btn = QtGui.QPushButton('quit', self)
		btn.clicked.connect(self.close_application)

		btn.resize(btn.minimumSizeHint())
		btn.move(100,100)

		self.show()

	def close_application(self):
		print("whooaa so custom")
		sys.exit()

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()

	sys.exit(app.exec_())

run()