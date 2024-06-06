from PySide6.QtWidgets import QPushButton, QSizePolicy

class DiskButton(QPushButton):
    def __init__(self, disks, path):
        super().__init__()
        self.disks = disks
        self.path = path
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setMaximumHeight(25)
        self.setMaximumWidth(35)
        self.setText(self.path)
        self.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.disks.navigateToDisk(self.path)