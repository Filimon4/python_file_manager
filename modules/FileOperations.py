import os
import shutil
import re

from modules.dialogs import FolderSelectorDialog
from modules.security.HashAlgo import Hash
from modules.FileIntegrityChecker import FileIntegrityChecker as FICheck

from PySide6.QtWidgets import QInputDialog, QMessageBox, QLineEdit, QDialog
from PySide6.QtCore import QDir, QFile

class FileOperations:

    def __init__(self, app):
        self.app = app
        self.cut_files = False

    def readBinaryFile(self, file):
        filePath = self.app.FileS.engine.filePath(file)
        ciphertext = ""
        with open(f"{filePath}", "rb") as file:
            ciphertext = file.read()
        return ciphertext

    def newFolder(self):
        folderName, ok = QInputDialog.getText(self.app, "Ввод", "Название папки: ", QLineEdit.Normal, text="Новая папка")
        if not folderName.strip():
            folderName = "Новая папка"
            
        clearName = ''
        invalidChars = '<>:"/\\|?*'
        for i in folderName:
            if not i in invalidChars:
                clearName += i
        folderName = clearName
        
        if ok and folderName:
            counter = self.getNumberOfSameName(self.app.currentDir, folderName)
            print(counter)
            if counter > 0:
                QDir(self.app.currentDir).mkdir(f"{folderName} ({counter})")
            else:
                QDir(self.app.currentDir).mkdir(f"{folderName}")

    def newFile(self):
        fileName, ok = QInputDialog.getText(self.app, "Ввод", "Название файла: ", QLineEdit.Normal, text="Новый файл.txt")
        if ok:
            file = f"{self.app.currentDir}/{fileName}"
            fileEntities = fileName.split('.')
            counter = self.getNumberOfSameName(self.app.currentDir, fileEntities[0])
            if counter > 0:
                if len(fileEntities) == 2:
                    file = f"{self.app.currentDir}/{fileEntities[0]} ({counter}).{fileEntities[1]}"
                else:
                    file = f"{self.app.currentDir}/{fileEntities[0]} ({counter}).txt"
            else:
                if len(fileEntities) == 2:
                    file = f"{self.app.currentDir}/{fileEntities[0]}.{fileEntities[1]}"
                else:
                    file = f"{self.app.currentDir}/{fileEntities[0]}.txt"
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

    def getNumberOfSameName(self, filePath, fileName):
        files = os.listdir(filePath)

        print(fileName)
        name_pattern_copy = re.compile(f"{fileName}" + r' (\(\d+\))?$')
        name_pattern = re.compile(f'{fileName}$')

        count = 0
        for item in files:
            if name_pattern.match(item) or name_pattern_copy.match(item):
                count += 1
        return count

    # Расчёт хэша
    def paste(self):
        willPaste = QMessageBox.question(self.app, "Вставка", "Вставить файлы в текущюю директорию", QMessageBox.Yes|QMessageBox.No)
        if not willPaste == QMessageBox.StandardButton.Yes: return

        for file in self.app.savedFiles:
            fromPath = self.app.FileS.engine.filePath(file)
            fromName = self.app.FileS.engine.fileName(file)
            toPath = f"{self.app.currentDir}/{fromName}"

            integrity = FICheck()
            if self.app.FileS.engine.fileInfo(file).isDir():

                filePath = self.app.FileS.engine.filePath(file)
                fileName = self.app.FileS.engine.fileName(file)

                counter = self.getNumberOfSameName(self.app.currentDir, fileName)
                if counter > 0:
                    shutil.copytree(filePath, f"{self.app.currentDir}/{fileName} ({counter})")
                else:
                    shutil.copytree(filePath, toPath)
            elif self.app.FileS.engine.fileInfo(file).isFile():
                filePath = self.app.FileS.engine.filePath(file)
                fileName = self.app.FileS.engine.fileName(file)

                fileEntities = fileName.split('.')
                counter = self.getNumberOfSameName(self.app.currentDir, fileEntities[0])
                if counter > 0:
                    if len(fileEntities) == 2:
                        toPath = f"{self.app.currentDir}/{fileEntities[0]} ({counter}).{fileEntities[1]}"
                        shutil.copy2(filePath, toPath)
                    else:
                        toPath = f"{self.app.currentDir}/{fileEntities[0]} ({counter})"
                        shutil.copy2(filePath, toPath)
                else:
                    shutil.copy2(filePath, toPath)


            checkIntegrity = integrity.compare_two(fromPath, toPath)
            print(checkIntegrity)
            if checkIntegrity:
                self.app.Notif.info("Соханность файла", "Файл успешно вставлен без потерь содержимого")
            else:
                self.app.Notif.info("Сохранность файла", "Целостность файла при перемещении была нарушено")
                # Notif.critical


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
            md5 = Hash()
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

    # Расчёт хэша
    def move(self):
        file = self.app.FileV.getSingleSelectedFile()
        if file:
            dia = FolderSelectorDialog(self.app.currentDir)
            result = dia.exec_()

            if result == QDialog.Accepted:
                selected_directory = self.app.FileS.engine.filePath(dia.tree_view.currentIndex())
                fileName = self.app.FileS.engine.fileName(file)
                fromPath = self.app.FileS.engine.filePath(file)

                integrity = FICheck()
                integrity.addFile(fromPath)
                # hash1 = self.getAutoHash(fromPath)

                toPath = f"{selected_directory}/{fileName}"

                willMove = QMessageBox.question(
                    self.app,
                    "Move item",
                    f"Переместить {fileName} из {fromPath} в {toPath}",
                    QMessageBox.Yes|QMessageBox.No
                )

                if willMove == QMessageBox.StandardButton.Yes:
                    self.move_file(fromPath, toPath)
                    integrityResuilt = integrity.compare_with(fromPath, toPath)
                    if integrityResuilt:
                        self.app.Notif.info("Соханность файла", "Файл успешно вставлен без потерь содержимого")
                    else:
                        self.app.Notif.info("Сохранность файла", "Целостность файла при перемещении была нарушено")

    def rename(self):
        file = self.app.FileV.getSingleSelectedFile()
        if file:
            itemPath = self.app.FileS.engine.filePath(file)
            itemName = self.app.FileS.engine.fileName(file)
            fileName, ok = QInputDialog.getText(self.app, "Ввод", "Новое имя: ", QLineEdit.Normal, text = itemName)
            filePath = f"{self.app.currentDir}/{fileName}"
            if QFile(itemPath).rename(itemPath, filePath):
                print("New file name")
            else:
                print("Cannot rename file")

