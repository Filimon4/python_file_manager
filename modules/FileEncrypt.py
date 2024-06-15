import base64
from typing import List
from modules.dialogs.CipherDialog import DecryptCipherDialog, EncryptCipherDialog
from modules.security.CipherAlgo import CipherAlgo

class Encrypt(CipherAlgo):
    
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.actionCipher = self.app.ui.actionCipher
        self.actionCipher.triggered.connect(self.actionClicked)

    def actionClicked(self):
        selectedFile = self.app.FileV.getSingleSelectedFile()

        filePath = ''
        fileParentPath = ''
        if selectedFile:
            filePath = self.app.FileS.engine.filePath(selectedFile)
            fileParentPath = self.app.FileS.engine.filePath(selectedFile.parent())
        dialog = EncryptCipherDialog(self.app, filePath, fileParentPath)
        result = dialog.exec_()
        if result:
            self.app.updateDir_Signal.emit()
            k1 = int(dialog.k1, 16)
            k2 = int(dialog.k2, 16)
            k3 = int(dialog.k3, 16)
            k4 = int(dialog.k4, 16)
            file_to_cipher = self.app.FileS.engine.index(dialog.file_to_cipher)

            fileName = dialog.output_file_path.split('/')[-1]
            readBinary = self.app.FileO.readBinaryFile(file_to_cipher)
            plain_text = base64.b64encode(readBinary)

            ciphertext = super().feistel_cipher(plain_text, [k1,k2,k3,k4])
            self.app.FileO.newFileBinarySilent(f"{fileName.split('.')[0]}.b64", ciphertext)