import os
import shutil
from FolderSelectorDialog import FolderSelectorDialog
from PySide6.QtWidgets import QInputDialog, QMessageBox, QLineEdit, QDialog
from PySide6.QtCore import QDir, QFile

class FileOperations:

    def __init__(self, app):
        self.app = app
        self.cut_files = False

    def readBinaryFile(self, file):
        filePath = self.app.FileS.engine.filePath(file)
        # fileName = self.app.FileS.engine.fileName(file)
        ciphertext = ""
        with open(f"{filePath}", "rb") as file:
            ciphertext = file.read()
        return ciphertext

    def newFolder(self):
        folderName, ok = QInputDialog.getText(self.app, "Ввод", "Название папки: ", QLineEdit.Normal)
        if ok and folderName:
            QDir(self.app.currentDir).mkdir(f"{folderName}")

    def newFile(self):
        fileName, ok = QInputDialog.getText(self.app, "Ввод", "Название файла: ", QLineEdit.Normal)
        file = f"{self.app.currentDir}/{fileName}"
        if ok and file:
            with open(file, "w") as file:
                pass

    def newFileBinarySilent(self, fileName, binaryText):
        file = f"{self.app.currentDir}/{fileName}"
        if file:
            with open(file, "wb") as file:
                file.write(binaryText)

    def delete(self, items = []):
        if not items:
            items = self.app.FileV.getSelectedFiles()
        if items:
            quest = f"Удалить {len(items)} элементов"
            willDelete = QMessageBox.question(self.app, "Удаление", quest, QMessageBox.Yes|QMessageBox.No)
            if willDelete == QMessageBox.StandardButton.Yes:
                for index in items:
                    self.app.FileS.engine.remove(index)

    def delete_no_sub(self, items = [], saved=False):
        if saved:
            items = self.app.savedFiles
        if items:
            for index in items:
                self.app.FileS.engine.remove(index)

    def copy(self):
        files = self.app.FileV.getSelectedFiles()
        if files:
            self.cut_files = False
            self.app.setSavedFiles_Signal.emit(files)

    def cut(self):
        files = self.app.FileV.getSelectedFiles()
        if files:
            self.cut_files = True
            self.app.setSavedFiles_Signal.emit(files)

    def paste(self):
        willPaste = QMessageBox.question(self.app, "Вставка", "Вставить файлы в текущюю директорию", QMessageBox.Yes|QMessageBox.No)
        if not willPaste == QMessageBox.StandardButton.Yes: return

        for file in self.app.savedFiles:
            if self.app.FileS.engine.fileInfo(file).isDir():
                filePath = self.app.FileS.engine.filePath(file)
                fileName = self.app.FileS.engine.fileName(file)

                files = os.listdir(self.app.currentDir)
                print(QDir(self.app.currentDir))

                if os.path.isdir(filePath):
                    counter = 0
                    for f in files:
                        if f.startswith(fileName):
                            counter += 1
                            print(f, counter)
                    shutil.copytree(filePath, f"{self.app.currentDir}/{fileName} ({counter})")
                else:
                    shutil.copytree(filePath, f"{self.app.currentDir}/{fileName}")
            elif self.app.FileS.engine.fileInfo(file).isFile():
                filePath = self.app.FileS.engine.filePath(file)
                fileName = self.app.FileS.engine.fileName(file)
                shutil.copy2(filePath, f"{self.app.currentDir}/{fileName}")

        if self.cut_files == True:
            self.delete_no_sub(saved=True)

    def move_file(self, fromPath, toPath):
        if fromPath and toPath:
            shutil.move(fromPath, toPath)

    def move(self):
        file = self.app.FileV.getSingleSelectedFile()
        if file:
            dia = FolderSelectorDialog()
            result = dia.exec_()

            if result == QDialog.Accepted:
                selected_directory = self.app.FileS.engine.filePath(dia.tree_view.currentIndex())
                fileName = self.app.FileS.engine.fileName(file)
                fromPath = self.app.FileS.engine.filePath(file)
                toPath = f"{selected_directory}/{fileName}"
                quest = f"Переместить {fileName} из {fromPath} в {toPath}"
                willMove = QMessageBox.question(self.app, "Move item", quest, QMessageBox.Yes|QMessageBox.No)
                if willMove == QMessageBox.StandardButton.Yes:
                    self.move_file(fromPath, toPath)

    def rename (self):
        file = self.getSingleSelectedFile()
        if file:
            itemPath = self.dialog.filePath(file)
            item = QFile(itemPath)
            fileName, ok = QInputDialog.getText(self, "Ввод", "Новое имя: ", QLineEdit.Normal)
            filePath = f"{self.app.currentDir}/{fileName}"
            if item.rename(filePath):
                print("New file name")
            else:
                print("Cannot rename file")

