from PySide6.QtWidgets import QSizePolicy, QSpacerItem
from PySide6.QtCore import QDir
from modules.ui import DiskButton

class Disks:
    def __init__(self, app):
        self.app = app
        self.logicDisks = QDir.drives()
        self.driverView = self.app.ui.driverView

        for disk in self.logicDisks:
            button = DiskButton(self, disk.absolutePath())
            self.driverView.addWidget(button)
        self.driverView.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

    def navigateToDisk(self, path):
        self.app.rendeRoot_Signal.emit(path)