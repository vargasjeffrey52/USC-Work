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
		self.home()

	def home(self):
		btn = QtGui.QPushButton('quit', self)
		btn.clicked.connect(self.close_application)

		btn.resize(btn.minimumSizeHint())
		btn.move(0,0)

		self.show()

	def close_application(self):
		print("whooaa so custom")
		sys.exit()

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()

	sys.exit(app.exec_())

run()