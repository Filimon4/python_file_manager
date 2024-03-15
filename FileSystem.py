from PySide6.QtWidgets import QFileSystemModel, QApplication, QMessageBox
from PySide6.QtCore import QDir

class FileSystem():
    def __init__(self, app):
        self.app = app

        self.savedFiles = []

        self.engine = QFileSystemModel()
        self.engine.setRootPath(self.app.currentDir)

    @property
    def Dir(self):
        return self.app.currentDir

    @Dir.setter
    def Dir(self, dir):
        self.app.setCurrentFolder_Signal.emit(dir)

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

