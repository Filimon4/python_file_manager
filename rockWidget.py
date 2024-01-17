from PySide6.QtWidgets import QMainWindow, QPushButton, QStatusBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6 import QtWidgets

class RockWidget(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("RockWidget")
        self.app = app # declare an app member
        self.setWindowTitle("Custom MainWindow")

        # add menu action
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.button_quit)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")


        # init toolbar
        toolbar = QtWidgets.QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        #add action in toolbar
        toolbar.addAction(quit_action)

        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message from some action")
        action1.triggered.connect(self.toolbar_button_click)

        # add second action in toolbar
        toolbar.addAction(action1)

        action2 = QAction(QIcon('simple_icon.png'), "Some other action", self)
        action2.setStatusTip("Status message for some other action")
        action2.triggered.connect(self.toolbar_button_click)
        # action2.setCheckable(True)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click here"))

        self.setStatusBar(QStatusBar(self))

        button1 = QPushButton("Button1")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)




    def button1_clicked(self):
        print("Now ith main")

    def button_quit(self):
       self.app.quit()

    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from my app")
