import os
import shutil
import hashlib
from FolderSelectorDialog import FolderSelectorDialog
from PySide6.QtWidgets import QInputDialog, QMessageBox, QLineEdit, QDialog
from PySide6.QtCore import QDir, QFile
from hashAlgo import MD5

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

    # add hash
    def paste(self):
        willPaste = QMessageBox.question(self.app, "Вставка", "Вставить файлы в текущюю директорию", QMessageBox.Yes|QMessageBox.No)
        if not willPaste == QMessageBox.StandardButton.Yes: return

        for file in self.app.savedFiles:
            filePath = self.app.FileS.engine.filePath(file)
            fileName = self.app.FileS.engine.fileName(file)

            hash1 = self.getAutoHash(filePath)
            toPath = f"{self.app.currentDir}/{fileName} Copy"
            if self.app.FileS.engine.fileInfo(file).isDir():
                filePath = self.app.FileS.engine.filePath(file)
                fileName = self.app.FileS.engine.fileName(file)

                files = os.listdir(self.app.currentDir)

                if os.path.isdir(filePath):
                    counter = 0
                    for f in files:
                        if fileName in f:
                            counter += 1
                    shutil.copytree(filePath, f"{self.app.currentDir}/{fileName} Copy({counter})")
                else:
                    shutil.copytree(filePath, toPath)
            elif self.app.FileS.engine.fileInfo(file).isFile():
                filePath = self.app.FileS.engine.filePath(file)
                fileName = self.app.FileS.engine.fileName(file)

                files = os.listdir(self.app.currentDir)
                print(files)

                if os.path.isfile(filePath):
                    counter = 0
                    for i in files:
                        if fileName in i:
                            counter += 1;
                    shutil.copy2(filePath, f"{self.app.currentDir}/{fileName} Copy({counter})")
                else:
                    shutil.copy2(filePath, toPath)

            hash2 = self.getAutoHash(toPath)

            if hash1 and hash2 and hash1 == hash2:
                print("The files are the save")
            else:
                print("Error file itegrity is in dunger")


        if self.cut_files == True:
            self.delete_no_sub(saved=True)

    def move_file(self, fromPath, toPath):
        if fromPath and toPath:
            shutil.move(fromPath, toPath)

    def getAutoHash(self, path):
        if not (path and os.path.exists(path)): return None
        if os.path.isfile(path):
            return self.getHashOfFile(path)
        elif os.path.isdir(path):
            return self.getHashOfFolder(path)

    def getHashOfFile(self, path):
        hash = None
        if path and os.path.exists(path) and os.path.isfile(path):
            md5 = MD5()
            with open(path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    md5.update(chunk)
            hash = md5.hexdigest()
        return hash

    def getHashOfFolder(self, path):
        file_integrity = ''
        if path and os.path.exists(path) and os.path.isdir(path):
            for root, dirs, files in os.walk(path):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    file_hash = self.getHashOfFile(file_path)
                    file_integrity += file_hash
        return file_integrity

    # add hash
    def move(self):
        file = self.app.FileV.getSingleSelectedFile()
        if file:
            dia = FolderSelectorDialog()
            result = dia.exec_()

            if result == QDialog.Accepted:
                selected_directory = self.app.FileS.engine.filePath(dia.tree_view.currentIndex())
                fileName = self.app.FileS.engine.fileName(file)
                fromPath = self.app.FileS.engine.filePath(file)

                hash1 = self.getAutoHash(fromPath)

                toPath = f"{selected_directory}/{fileName}"

                willMove = QMessageBox.question(
                    self.app,
                    "Move item",
                    f"Переместить {fileName} из {fromPath} в {toPath}",
                    QMessageBox.Yes|QMessageBox.No
                )

                if willMove == QMessageBox.StandardButton.Yes:
                    self.move_file(fromPath, toPath)

                    hash2 = self.getAutoHash(toPath)
                    if hash1 and hash2 and hash1 == hash2:
                        print("The files are the save")
                    else:
                        print("Error file itegrity is in dunger")

    def rename (self):
        file = self.app.FileV.getSingleSelectedFile()
        if file:
            itemPath = self.app.FileS.engine.filePath(file)
            item = QFile(itemPath)
            fileName, ok = QInputDialog.getText(self.app, "Ввод", "Новое имя: ", QLineEdit.Normal)
            filePath = f"{self.app.currentDir}/{fileName}"
            if item.rename(filePath):
                print("New file name")
            else:
                print("Cannot rename file")

