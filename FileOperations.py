import os
import shutil
from FolderSelectorDialog import FolderSelectorDialog
from PySide6.QtWidgets import QInputDialog, QMessageBox, QLineEdit, QDialog
from PySide6.QtCore import QDir, QFile

class FileOperations:

    @staticmethod
    def newFolder(self):
        folderName, ok = QInputDialog.getText(self, "Ввод", "Название папки: ", QLineEdit.Normal)
        if ok:
            QDir(self.currentDir).mkdir(f"{folderName}")

    @staticmethod
    def newFile(self):
        fileName, ok = QInputDialog.getText(self, "Ввод", "Название файла: ", QLineEdit.Normal)
        file = f"{self.currentDir}/{fileName}"
        if ok:
            with open(file, "w") as file:
                pass

    @staticmethod
    def delete(self, items = []):
        indexes = self.getSelectedFiles()
        if items:
            indexes = items
        print(indexes)
        if len(indexes) > 0:
            quest = f"Удалить {len(indexes)} элементов"
            willDelete = QMessageBox.question(self, "Удаление", quest, QMessageBox.Yes|QMessageBox.No)
            if willDelete == QMessageBox.StandardButton.Yes:
                for index in indexes:
                    self.dialog.remove(index)

    @staticmethod
    def delete_cut_items(self, items = []):
        print(items)
        for index in items:
            self.dialog.remove(index)

    @staticmethod
    def cut(self):
        # get selected files
        files = self.savedFiles
        if files:
            quest = f"Вырезать {len(files)} элементов"
            willDelete = QMessageBox.question(self, "Вырезание", quest, QMessageBox.Yes|QMessageBox.No)
            if willDelete == QMessageBox.StandardButton.Yes:
                self.paste()
                self.delete_cut_items(files)

    @staticmethod
    def paste(self):
        willPaste = QMessageBox.question(self, "Вставка", "Вставить файлы в настоящую директорию", QMessageBox.Yes|QMessageBox.No)
        if not willPaste == QMessageBox.StandardButton.Yes:
            return
        for file in self.savedFiles:
            if self.dialog.fileInfo(file).isDir():
                filePath = self.dialog.filePath(file)
                fileName = self.dialog.fileName(file)


                files = os.listdir(self.currentDir)

                if os.path.isdir(filePath):
                    counter = 0
                    for f in files:
                        if f.startswith(fileName):
                            counter += 1
                            print(f, counter)
                    if counter == 0 or counter == 1:
                        shutil.copytree(filePath, f"{self.currentDir}/{fileName} - copy")
                    else:
                        shutil.copytree(filePath, f"{self.currentDir}/{fileName} - copy ({counter})")
                else:
                    shutil.copytree(filePath, f"{self.currentDir}/{fileName}")
            elif self.dialog.fileInfo(file).isFile():
                filePath = self.dialog.filePath(file)
                fileName = self.dialog.fileName(file)
                shutil.copy2(filePath, f"{self.currentDir}/{fileName}")

    @staticmethod
    def copy(self):
        files = self.getSelectedFiles()
        self.savedFiles = files

    @staticmethod
    def move_file(self, fromPath, toPath):
        if fromPath and toPath:
            shutil.move(fromPath, toPath)

    @staticmethod
    def move (self):
        file = self.getSingleSelectedFile()
        if file:
            dia = FolderSelectorDialog()
            result = dia.exec_()

            if result == QDialog.Accepted:
                selected_directory = self.dialog.filePath(dia.tree_view.currentIndex())
                fileName = self.dialog.fileName(file)
                fromPath = self.dialog.filePath(file)
                toPath = f"{selected_directory}/{fileName}"
                quest = f"Переместить {fileName} из {fromPath} в {toPath}"
                willMove = QMessageBox.question(self, "Move item", quest, QMessageBox.Yes|QMessageBox.No)
                if willMove == QMessageBox.StandardButton.Yes:
                    self.move_file(fromPath, toPath)

    @staticmethod
    def rename (self):
        file = self.getSingleSelectedFile()
        if file:
            itemPath = self.dialog.filePath(file)
            item = QFile(itemPath)
            fileName, ok = QInputDialog.getText(self, "Ввод", "Новое имя: ", QLineEdit.Normal)
            filePath = f"{self.currentDir}/{fileName}"
            if item.rename(filePath):
                print("New file name")
            else:
                print("Cannot rename file")

