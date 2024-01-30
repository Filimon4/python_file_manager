# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTreeView, QVBoxLayout, QWidget)
import rc_icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(975, 571)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setTabletTracking(False)
        MainWindow.setStyleSheet(u"#centralwidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#copy_btn {\n"
"	border: 1px solid black;\n"
"	border-radius: 7px;\n"
"	padding: 5px;\n"
"	\n"
"}\n"
"\n"
"#copy_btn:hover {\n"
"	background-color: rgb(0, 141, 197);\n"
"	border: 1px solid rgb(0, 172, 240);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: 2px solid #808080;\n"
"	padding: 5px;\n"
"	border-radius: 5px;\n"
"}\n"
"            \n"
"QPushButton:hover {\n"
"	background-color: #87CEFA; /* Light blue on hover */\n"
"}\n"
"            \n"
"QPushButton:pressed {\n"
"	border: 2px solid #0000FF; /* Blue border on press */\n"
"}\n"
"")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon = QIcon()
        icon.addFile(u":/imgs_file_manager/circle-xmark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon)
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        icon1 = QIcon()
        icon1.addFile(u":/imgs_file_manager/copy-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCopy.setIcon(icon1)
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        icon2 = QIcon()
        icon2.addFile(u":/imgs_file_manager/paste.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPaste.setIcon(icon2)
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        icon3 = QIcon()
        icon3.addFile(u":/imgs_file_manager/scissors.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCut.setIcon(icon3)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon4 = QIcon()
        icon4.addFile(u":/imgs_file_manager/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon4)
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.actionAbout_Qt.setIcon(icon4)
        self.actionRename = QAction(MainWindow)
        self.actionRename.setObjectName(u"actionRename")
        icon5 = QIcon()
        icon5.addFile(u":/imgs_file_manager/pen-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRename.setIcon(icon5)
        self.actionMake_folder = QAction(MainWindow)
        self.actionMake_folder.setObjectName(u"actionMake_folder")
        icon6 = QIcon()
        icon6.addFile(u":/imgs_file_manager/add-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMake_folder.setIcon(icon6)
        self.actionDelete_folder = QAction(MainWindow)
        self.actionDelete_folder.setObjectName(u"actionDelete_folder")
        icon7 = QIcon()
        icon7.addFile(u":/imgs_file_manager/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDelete_folder.setIcon(icon7)
        self.actionNew_File = QAction(MainWindow)
        self.actionNew_File.setObjectName(u"actionNew_File")
        icon8 = QIcon()
        icon8.addFile(u":/imgs_file_manager/add-document.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew_File.setIcon(icon8)
        self.actionMove = QAction(MainWindow)
        self.actionMove.setObjectName(u"actionMove")
        icon9 = QIcon()
        icon9.addFile(u":/imgs_file_manager/move-to-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMove.setIcon(icon9)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.copy_btn = QPushButton(self.centralwidget)
        self.copy_btn.setObjectName(u"copy_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.copy_btn.sizePolicy().hasHeightForWidth())
        self.copy_btn.setSizePolicy(sizePolicy1)
        self.copy_btn.setIcon(icon1)
        self.copy_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.copy_btn)

        self.cut_btn = QPushButton(self.centralwidget)
        self.cut_btn.setObjectName(u"cut_btn")
        sizePolicy1.setHeightForWidth(self.cut_btn.sizePolicy().hasHeightForWidth())
        self.cut_btn.setSizePolicy(sizePolicy1)
        self.cut_btn.setIcon(icon3)
        self.cut_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.cut_btn)

        self.paste_btn = QPushButton(self.centralwidget)
        self.paste_btn.setObjectName(u"paste_btn")
        sizePolicy1.setHeightForWidth(self.paste_btn.sizePolicy().hasHeightForWidth())
        self.paste_btn.setSizePolicy(sizePolicy1)
        self.paste_btn.setIcon(icon2)
        self.paste_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.paste_btn)

        self.newFile_btn = QPushButton(self.centralwidget)
        self.newFile_btn.setObjectName(u"newFile_btn")
        sizePolicy1.setHeightForWidth(self.newFile_btn.sizePolicy().hasHeightForWidth())
        self.newFile_btn.setSizePolicy(sizePolicy1)
        self.newFile_btn.setIcon(icon8)
        self.newFile_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.newFile_btn)

        self.newFolder_btn = QPushButton(self.centralwidget)
        self.newFolder_btn.setObjectName(u"newFolder_btn")
        sizePolicy1.setHeightForWidth(self.newFolder_btn.sizePolicy().hasHeightForWidth())
        self.newFolder_btn.setSizePolicy(sizePolicy1)
        self.newFolder_btn.setIcon(icon6)
        self.newFolder_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.newFolder_btn)

        self.delete_btn = QPushButton(self.centralwidget)
        self.delete_btn.setObjectName(u"delete_btn")
        sizePolicy1.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
        self.delete_btn.setSizePolicy(sizePolicy1)
        self.delete_btn.setIcon(icon7)
        self.delete_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.delete_btn)

        self.horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.undo_btn = QPushButton(self.centralwidget)
        self.undo_btn.setObjectName(u"undo_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.undo_btn.sizePolicy().hasHeightForWidth())
        self.undo_btn.setSizePolicy(sizePolicy2)
        icon10 = QIcon()
        icon10.addFile(u":/imgs_file_manager/undo-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.undo_btn.setIcon(icon10)
        self.undo_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.undo_btn)

        self.redo_btn = QPushButton(self.centralwidget)
        self.redo_btn.setObjectName(u"redo_btn")
        self.redo_btn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.redo_btn.sizePolicy().hasHeightForWidth())
        self.redo_btn.setSizePolicy(sizePolicy2)
        icon11 = QIcon()
        icon11.addFile(u":/imgs_file_manager/redo-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.redo_btn.setIcon(icon11)
        self.redo_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.redo_btn)

        self.up_btn = QPushButton(self.centralwidget)
        self.up_btn.setObjectName(u"up_btn")
        sizePolicy2.setHeightForWidth(self.up_btn.sizePolicy().hasHeightForWidth())
        self.up_btn.setSizePolicy(sizePolicy2)
        icon12 = QIcon()
        icon12.addFile(u":/imgs_file_manager/level-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.up_btn.setIcon(icon12)
        self.up_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.up_btn)

        self.directory = QLabel(self.centralwidget)
        self.directory.setObjectName(u"directory")

        self.horizontalLayout_2.addWidget(self.directory)

        self.find = QLabel(self.centralwidget)
        self.find.setObjectName(u"find")

        self.horizontalLayout_2.addWidget(self.find)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 8)
        self.horizontalLayout_2.setStretch(4, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setEnabled(True)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QSize(1, 0))
        self.treeView.setMaximumSize(QSize(1000000, 100000))

        self.verticalLayout.addWidget(self.treeView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 975, 26))
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuEdit.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionCopy)
        self.menuFile.addAction(self.actionPaste)
        self.menuFile.addAction(self.actionCut)
        self.menuFile.addAction(self.actionRename)
        self.menuFile.addAction(self.actionMove)
        self.menuFile.addAction(self.actionMake_folder)
        self.menuFile.addAction(self.actionNew_File)
        self.menuFile.addAction(self.actionDelete_folder)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.actionRename.setText(QCoreApplication.translate("MainWindow", u"Rename", None))
        self.actionMake_folder.setText(QCoreApplication.translate("MainWindow", u"New Folder", None))
        self.actionDelete_folder.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.actionNew_File.setText(QCoreApplication.translate("MainWindow", u"New File", None))
        self.actionMove.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.copy_btn.setText("")
        self.cut_btn.setText("")
        self.paste_btn.setText("")
        self.newFile_btn.setText("")
        self.newFolder_btn.setText("")
        self.delete_btn.setText("")
        self.undo_btn.setText("")
        self.redo_btn.setText("")
        self.directory.setText("")
        self.find.setText("")
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

