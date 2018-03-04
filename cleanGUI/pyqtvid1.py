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
		img = QtGui.QIcon('pokeBall.png')
		# Adding the action for a tools bar that belongs to the Home window
		extractAction = QtGui.QAction(img, 'Flee the seen', self)
		extractAction.triggered.connect(self.close_application)


		# displaying the tools menu that belongs to the homes window
		self.toolBar = self.addToolBar('Extraction')
		self.toolBar.addAction(extractAction)

		checkBox = QtGui.QCheckBox('Enlarge Window', self)
		checkBox.move(100, 25)
		checkBox.toggle()
		checkBox.stateChanged.connect(self.enlarge_window)


		self.show()


	def enlarge_window(self, state):
		if state == QtCore.Qt.Checked:
			self.setGeometry(50, 50, 1000, 600)
		else:
			self.setGeometry(50, 50, 500, 300)

	def close_application(self):

		choice = QtGui.QMessageBox.question(self,'Extract!', 
			"Get into the Chopper",
			QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			print("Extracting Now !!!")
			sys.exit()
		else:
			pass


def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()

	sys.exit(app.exec_())

run()