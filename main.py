import sys
from PySide6.QtWidgets import QApplication
from rockWidget import RockWidget
from messageBox import MessageBox
from lineEditor import LineEditor
from textEdit import TextEdit
from imageBox import ImageBox
from sizePolicies import SizePolicies
from gridLayout import GridLayout
from buttonLayout import ButtonLayout
from listWidget import ListWidget
from tabWidget import TabWidget
from comboBox import ComboBox

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # w = RockWidget(app)
    # w.show()
    # m = MessageBox()
    # m.show()
    # l = LineEditor()
    # l.show()
    # t = TextEdit()
    # t.show()
    # i = ImageBox()
    # i.show()
    # s = SizePolicies()
    # s.show()
    # g = GridLayout()
    # g.show()
    # b = ButtonLayout()
    # b.show()
    # lw = ListWidget()
    # lw.show()
    # tw = TabWidget()
    # tw.show()
    cb = ComboBox()
    cb.show()
    app.exec()

# import os
# from PySide6.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QTreeView, QListView, QVBoxLayout, QLabel, \
#     QWidget, QLineEdit, QPushButton, QFileDialog, QHBoxLayout, QInputDialog, QMessageBox, QMenu
# from PySide6.QtCore import Qt


# class ComplexFileManager(QMainWindow):
#     def __init__(self):
#         super(ComplexFileManager, self).__init__()

#         self.setWindowTitle("Complex File Manager")
#         self.setGeometry(100, 100, 800, 600)

#         self.central_widget = QWidget(self)
#         self.setCentralWidget(self.central_widget)

#         self.layout = QVBoxLayout(self.central_widget)

#         # File Tree
#         self.model = QFileSystemModel()
#         self.model.setRootPath('')
#         self.tree_view = QTreeView(self.central_widget)
#         self.tree_view.setModel(self.model)
#         self.tree_view.setRootIndex(self.model.index(''))
#         self.tree_view.setContextMenuPolicy(Qt.CustomContextMenu)
#         self.tree_view.customContextMenuRequested.connect(self.show_context_menu)

#         self.layout.addWidget(self.tree_view)

#         # File List
#         self.file_list_view = QListView(self.central_widget)
#         self.file_list_view.setModel(self.model)
#         self.file_list_view.setRootIndex(self.model.index(''))
#         self.file_list_view.clicked.connect(self.on_file_list_clicked)

#         self.layout.addWidget(self.file_list_view)

#         # Labels
#         self.label_current_directory = QLabel(self.central_widget)
#         self.layout.addWidget(self.label_current_directory)

#         self.label_selected_file = QLabel(self.central_widget)
#         self.layout.addWidget(self.label_selected_file)

#         # Search
#         self.search_line_edit = QLineEdit(self.central_widget)
#         self.search_line_edit.setPlaceholderText("Search files")
#         self.layout.addWidget(self.search_line_edit)

#         search_button = QPushButton("Search", self.central_widget)
#         search_button.clicked.connect(self.search_files)
#         self.layout.addWidget(search_button)

#         # Buttons for additional features
#         button_layout = QHBoxLayout()

#         add_button = QPushButton("Add File", self.central_widget)
#         add_button.clicked.connect(self.add_file)
#         button_layout.addWidget(add_button)

#         delete_button = QPushButton("Delete File", self.central_widget)
#         delete_button.clicked.connect(self.delete_file)
#         button_layout.addWidget(delete_button)

#         rename_button = QPushButton("Rename File", self.central_widget)
#         rename_button.clicked.connect(self.rename_file)
#         button_layout.addWidget(rename_button)

#         self.layout.addLayout(button_layout)

#         # Initialize UI
#         self.update_current_directory()

#     def on_tree_view_clicked(self, index):
#         self.file_list_view.setRootIndex(index)
#         self.update_current_directory()

#     def on_file_list_clicked(self, index):
#         file_path = self.model.filePath(index)
#         self.label_selected_file.setText(f"Selected file: {file_path}")

#     def update_current_directory(self):
#         current_index = self.tree_view.currentIndex()
#         current_directory = self.model.filePath(current_index)
#         self.label_current_directory.setText(f"Current directory: {current_directory}")

#     def search_files(self):
#         search_text = self.search_line_edit.text()
#         root_path = self.model.rootPath()
#         search_results = []

#         for root, dirs, files in os.walk(root_path):
#             for file in files:
#                 if search_text.lower() in file.lower():
#                     search_results.append(os.path.join(root, file))

#         # Update the file list view with search results
#         search_model = QFileSystemModel()
#         search_model.setRootPath('')
#         search_model.setFilter(QDir.AllEntries | QDir.NoDotAndDotDot)
#         search_model.setNameFilters(["*." + ext for ext in ["txt", "pdf", "docx"]])  # Add desired file extensions
#         search_model.setNameFilterDisables(False)

#         search_model.setRootPath('')  # Display all drives/directories
#         search_model.setRootPath(root_path)

#         self.file_list_view.setModel(search_model)

#     def show_context_menu(self, pos):
#         index = self.tree_view.indexAt(pos)
#         if index.isValid():
#             menu = QMenu(self)

#             open_action = menu.addAction("Open")
#             open_action.triggered.connect(self.open_file)

#             delete_action = menu.addAction("Delete")
#             delete_action.triggered.connect(self.delete_file)

#             rename_action = menu.addAction("Rename")
#             rename_action.triggered.connect(self.rename_file)

#             menu.exec_(self.tree_view.mapToGlobal(pos))

#     def add_file(self):
#         current_index = self.tree_view.currentIndex()
#         current_directory = self.model.filePath(current_index)

#         file_name, _ = QFileDialog.getSaveFileName(self, "Add File", current_directory)

#         if file_name:
#             # Create an empty file
#             with open(file_name, 'w'):
#                 pass

#             # Update the file view
#             self.model.setRootPath('')
#             self.tree_view.setRootIndex(self.model.index(''))

#     def delete_file(self):
#         current_index = self.file_list_view.currentIndex()
#         file_path = self.model.filePath(current_index)

#         confirm_dialog = QMessageBox.question(self, 'Delete File', f'Delete {file_path}?', QMessageBox.Yes | QMessageBox.No)

#         if confirm_dialog == QMessageBox.Yes:
#             os.remove(file_path)
#             self.model.setRootPath('')
#             self.tree_view.setRootIndex(self.model.index(''))

#     def rename_file(self):
#         current_index = self.file_list_view.currentIndex()
#         file_path = self.model.filePath(current_index)

#         new_name, ok = QInputDialog.getText(self, 'Rename File', f'Enter new name for {file_path}:', QLineEdit.Normal, '')

#         if ok and new_name:
#             new_path = os.path.join(os.path.dirname(file_path), new_name)
#             os.rename(file_path, new_path)
#             self.model.setRootPath('')
#             self.tree_view.setRootIndex(self.model.index(''))

#     def open_file(self):
#         current_index = self.file_list_view.currentIndex()
#         file_path = self.model.filePath(current_index)

#         os.system(f"start {file_path}")  # Open the file using the default system program


# if __name__ == "__main__":
#     app = QApplication([])
#     file_manager = ComplexFileManager()
#     file_manager.show()
#     app.exec()



