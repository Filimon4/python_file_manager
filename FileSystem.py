from PySide6.QtWidgets import QFileSystemModel
from PySide6.QtCore import QDir

class FileSystem:
    def __init__(self):
        # logic

        self.currentDir = ''
        self.savedFiles = []

        self.engine = QFileSystemModel(self)
        self.engine.setRootPath(QDir.currentPath())

    @property
    def currentDir(self):
        return self.currentDir

    @currentDir.setter
    def currentDir(self, dir):
        self.currentDir = dir

    @property
    def engine(self):
        return self.engine
