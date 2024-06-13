import base64
from typing import List
from modules.dialogs.CipherDialog import DecryptCipherDialog, EncryptCipherDialog
from modules.security.CipherAlgo import CipherAlgo

class Decrypt(CipherAlgo):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.actionDecipher = self.app.ui.actionDecipher
        self.actionDecipher.triggered.connect(self.actionClicked)

    def actionClicked(self):
        selectedFile = self.app.FileV.getSingleSelectedFile()

        filePath = ''
        fileParentPath = ''
        if selectedFile:
            filePath = self.app.FileS.engine.filePath(selectedFile)
            fileParentPath = self.app.FileS.engine.filePath(selectedFile.parent())
        dialog = DecryptCipherDialog(self.app, filePath, fileParentPath, 'b64')
        result = dialog.exec_()
        if result:
            self.app.updateDir_Signal.emit()
            k1 = int(dialog.k1, 16)
            k2 = int(dialog.k2, 16)
            k3 = int(dialog.k3, 16)
            k4 = int(dialog.k4, 16)
            file_to_decipher = self.app.FileS.engine.index(dialog.file_to_cipher)

            fileName = dialog.output_file_path.split('/')
            fileEntyties = fileName[-1].split('.')

            selectedFile = self.app.FileV.getSingleSelectedFile()
            readBinary = self.app.FileO.readBinaryFile(file_to_decipher)

            deciphertext = super().feistel_decipher(readBinary, keys=[k1,k2,k3,k4])
            print(deciphertext)
            print(base64.b64decode(deciphertext))
            if len(fileEntyties) >= 2:
                self.app.FileO.newFileBinarySilent(f"{'.'.join(fileEntyties[0:-1])}.{fileEntyties[-1]}", base64.b64decode(deciphertext))
            else:
                self.app.FileO.newFileBinarySilent(f"{fileEntyties[0]}.txt", base64.b64decode(deciphertext))

