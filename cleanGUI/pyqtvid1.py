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

		# reserves a horizontal bar at the bottom as the status bar
		self.statusBar()

		# display horizontal menubar with specified dropdown menus for action
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

		# Adding the action for a tools bar that belongs to the Home window
		extractAction = QtGui.QAction(QtGui.QIcon('pokeBall.png'), 'Flee the seen', self)
		extractAction.triggered.connect(self.close_application)

		# displaying the tools menu that belongs to the homes window
		self.toolBar = self.addToolBar('Extraction')
		self.toolBar.addAction(extractAction)

		self.show()

	def close_application(self):
		print("whooaa so custom")
		sys.exit()

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()

	sys.exit(app.exec_())

run()