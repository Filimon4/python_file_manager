from PySide6.QtWidgets import QFileSystemModel, QApplication, QMessageBox
from PySide6.QtCore import QDir

class FileSystem():
    def __init__(self, app):
        self.app = app
        print(self.app)

        self.currentDir = ''
        self.savedFiles = []

        self.engine = QFileSystemModel()
        self.engine.setRootPath(QDir.currentPath())

    @property
    def Dir(self):
        return self.currentDir

    @Dir.setter
    def Dir(self, dir):
        self.currentDir = dir

    @property
    def _engine(self):
        return self.engine

    @staticmethod
    def quit(self):
        QApplication.quit()

    @staticmethod
    def about_qt(self):
        QApplication.aboutQt()

    @staticmethod
    def about(self):
        dialog = QMessageBox()
        dialog.setText('''О Программе\n\nНастоящий проекта был разработан по заказу предодователей ВятГу\nПроект: Файловый Менеджер''')
        dialog.setWindowTitle("О программе")
        dialog.setIcon(QMessageBox.Icon.Information)
        dialog.exec()

