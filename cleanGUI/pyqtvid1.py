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


		fontchoice = QtGui.QAction('Font', self)
		fontchoice.triggered.connect(self.fontchoice)

		#self.toolBar = self.addToolBar('Font')
		self.toolBar.addAction(fontchoice)


		color = QtGui.QColor(0, 0, 0)
		fontcolor = QtGui.QAction('Font bg Color', self)
		fontcolor.triggered.connect(self.color_picker)

		self.toolBar.addAction(fontcolor)



		# adding check box to window
		checkBox = QtGui.QCheckBox('Enlarge Window', self)
		checkBox.move(300, 25)
		#checkBox.toggle()
		checkBox.stateChanged.connect(self.enlarge_window)

		# adding progress bar
		self.progress = QtGui.QProgressBar(self)
		self.progress.setGeometry(200,80,250,20)

		# adding push button for progress bar
		self.btn = QtGui.QPushButton("Download", self)
		self.btn.move(200,120)
		self.btn.clicked.connect(self.download)


		# creating a lable for the dorp down menu
		print(self.style().objectName())
		self.styleChoice = QtGui.QLabel("Windows", self)

		# creating a drop down menu that contains the following text 
		comboBox = QtGui.QComboBox(self)
		comboBox.addItem("motif")
		comboBox.addItem("Windows")
		comboBox.addItem("cde")
		comboBox.addItem("Plastique")
		comboBox.addItem("Cleanlooks")
		comboBox.addItem("windowsvista")

		# moving the drop down menu and drop down menu label
		comboBox.move(50,250)
		self.styleChoice.move(50,210)
		# activates the item in the combobox by connecting it 
		comboBox.activated[str].connect(self.style_choice)

		cal = QtGui.QCalendarWidget(self)
		cal.move(500,200)
		cal.resize(300,300)

		self.show()

	def color_picker(self):
		color = QtGui.QColorDialog.getColor()
		self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

	def fontchoice(self):
		font, valid = QtGui.QFontDialog.getFont()
		if valid:
			self.styleChoice.setFont(font)

	# method that selects the gui style
	def style_choice(self,text):
		self.styleChoice.setText(text)
		QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))


	# method that updates progress bar 
	def download(self):
		self.completed = 0

		while self.completed < 100:
			self.completed += 0.0001
			self.progress.setValue(self.completed)

	# updates the checkbox state and enlarges window
	def enlarge_window(self, state):
		if state == QtCore.Qt.Checked:
			self.setGeometry(50, 50, 1000, 10000)
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