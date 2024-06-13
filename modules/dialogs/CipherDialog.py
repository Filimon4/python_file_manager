import json
import os
import random
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFileDialog,
    QCheckBox
)
from modules.dialogs.FolderSelectorDialog import FileSelectorDialog

class CipherDialog(QDialog):
    def __init__(self, app, selectedFile='', parentOfSelectedFile='', inputExtenstion=''):
        super().__init__()
        app_icon = QIcon('app_icon.png')
        self.setWindowIcon(app_icon)

        self.selectedFile = selectedFile
        self.parentOfSelected = parentOfSelectedFile
        self.inputExtenstion = inputExtenstion
        self.app = app

        self.fileSelected = self.selectedFile.split('/')[-1]

        self.file_to_cipher_edit = QLineEdit()

        if inputExtenstion:
            selectedFileEntyties = self.selectedFile.split('.')
            if len(selectedFileEntyties) >= 2:
                if selectedFileEntyties[-1] == inputExtenstion:
                    self.file_to_cipher_edit.setText(self.selectedFile)
                else:
                    self.file_to_cipher_edit.setText(f"{self.parentOfSelected}/")
            else:
                self.file_to_cipher_edit.setText(f"{self.parentOfSelected}/")
        else:
            self.file_to_cipher_edit.setText(self.selectedFile)

        self.output_file_edit = QLineEdit()
        if self.parentOfSelected:
            self.output_file_edit.setText(f"{self.parentOfSelected}/")
        self.b1_box = QLineEdit()
        self.b1_box.setInputMask("HHHHHHHH")
        self.b1_box.setMaxLength(8)
        self.b2_box = QLineEdit()
        self.b2_box.setInputMask("HHHHHHHH")
        self.b2_box.setMaxLength(8)
        self.b3_box = QLineEdit()
        self.b3_box.setInputMask("HHHHHHHH")
        self.b3_box.setMaxLength(8)
        self.b4_box = QLineEdit()
        self.b4_box.setInputMask("HHHHHHHH")
        self.b4_box.setMaxLength(8)

        self.rewriteKeys = QCheckBox('Перезаписать ключи')
        self.rewriteKeys.setChecked(False)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        file_to_cipher_layout = QVBoxLayout()
        file_to_cipher_input = QHBoxLayout()
        file_to_cipher_layout.addWidget(QLabel(self.InputTitle))
        file_to_cipher_input.addWidget(self.file_to_cipher_edit)
        file_to_cipher_layout.addLayout(file_to_cipher_input)
        browse_button = QPushButton("Выбрать") # change to created input file
        browse_button.clicked.connect(self.browse_file_to_cipher)
        file_to_cipher_input.addWidget(browse_button)
        layout.addLayout(file_to_cipher_layout)

        output_file_layout = QVBoxLayout()
        output_file_layout.addWidget(QLabel(self.OutputTitle))
        output_file_layout.addWidget(self.output_file_edit)
        layout.addLayout(output_file_layout)

        cipher_params_layout = QVBoxLayout()
        cipher_params_layout.addWidget(QLabel(self.keysTitle))
        generate_button = QPushButton('Сгенерировать новые ключи')
        generate_button.clicked.connect(self.set_generate_keys)
        use_prev_keys_button = QPushButton('Использовать предыдущие ключи')
        use_prev_keys_button.clicked.connect(self.set_prev_keys)
        cipher_params_layout.addWidget(generate_button)
        cipher_params_layout.addWidget(use_prev_keys_button)
        for label_text, spinbox in zip(["K1:", "K2:", "K3:", "K4:"], [self.b1_box, self.b2_box, self.b3_box, self.b4_box]):
            cipher_keys_layout = QHBoxLayout()
            cipher_keys_layout.addWidget(QLabel(label_text), 1)
            cipher_keys_layout.addWidget(spinbox, 100)
            cipher_params_layout.addLayout(cipher_keys_layout)
        cipher_params_layout.addWidget(self.rewriteKeys)
        layout.addLayout(cipher_params_layout)
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.ok_clicked)
        layout.addWidget(ok_button)
        self.setLayout(layout)

    def set_prev_keys(self):
        keys = []
        with open('./keys.json', 'r') as f:
            data = json.load(f)
            for i in data:
                keys.append(data[i])
        self.b1_box.setText(keys[0])
        self.b2_box.setText(keys[1])
        self.b3_box.setText(keys[2])
        self.b4_box.setText(keys[3])

    def set_generate_keys(self):
        keys = self.generate_hex_keys()
        self.b1_box.setText(keys[0])
        self.b2_box.setText(keys[1])
        self.b3_box.setText(keys[2])
        self.b4_box.setText(keys[3])

    def generate_hex_keys(self):
        keys = []
        def generate_random_hex():
            return '{:08x}'.format(random.randint(0, 2**32-1))

        for i in range(4):
            random_hex = generate_random_hex()
            if random_hex:
                keys.append(str(random_hex))
            else:
                keys.append('11111111')

        return keys


    def browse_file_to_cipher(self):
        # file_dialog = QFileDialog()
        # file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog = FileSelectorDialog(self.app.currentDir)
        result = file_dialog.exec_()
        if result == QDialog.Accepted:
            selected_files = file_dialog.selectedFile
            if selected_files:
                if self.inputExtenstion:
                    selectedFileEntyties = self.selectedFile.split('.')
                    if len(selectedFileEntyties) >= 2:
                        if selectedFileEntyties[-1] == self.inputExtenstion:
                            self.file_to_cipher_edit.setText(selected_files[0])
                        else:
                            self.file_to_cipher_edit.setText(f"{self.parentOfSelected}/")
                    else:
                        self.file_to_cipher_edit.setText(f"{self.parentOfSelected}/")
                else:
                    self.file_to_cipher_edit.setText(selected_files[0])


    def is_file_path_available(self, file_path):
        return not os.path.exists(file_path)

    def ok_clicked(self):
        self.file_to_cipher = self.file_to_cipher_edit.text().strip()
        self.output_file_path = self.output_file_edit.text().strip()
        self.k1 = self.b1_box.text()
        self.k2 = self.b2_box.text()
        self.k3 = self.b3_box.text()
        self.k4 = self.b4_box.text()

        if not self.file_to_cipher or not self.output_file_path:
            print("Please provide both input and output file paths.")
            return

        if not self.is_file_path_available(self.output_file_path):
            print("Output file path already exists. Choose a different one.")
            return
        self.accept()

class EncryptCipherDialog(CipherDialog):
    def __init__(self, app, selectedFile='', parentOfSelectedFile=''):
        self.OutputTitle = "Пеместить данные в:"
        self.InputTitle = "Зашифровать данные из: "
        self.keysTitle = "Ключ для шифрования"
        super().__init__(app, selectedFile, parentOfSelectedFile)
        self.setWindowTitle("Шифрование файла")

class DecryptCipherDialog(CipherDialog):
    def __init__(self, app, selectedFile='', parentOfSelectedFile='', inputExtenstion=''):
        self.InputTitle = "Дешифровать данне из"
        self.OutputTitle = "Пеместить данные в:"
        self.keysTitle = "Ключи для дешифрования"
        super().__init__(app, selectedFile, parentOfSelectedFile, inputExtenstion)
        self.setWindowTitle("Дешифровка файла")