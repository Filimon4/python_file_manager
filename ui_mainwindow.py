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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QToolBar,
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
        MainWindow.setAutoFillBackground(False)
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
"\n"
"QMainWindow {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"           \n"
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
        self.actionCipher = QAction(MainWindow)
        self.actionCipher.setObjectName(u"actionCipher")
        icon10 = QIcon()
        icon10.addFile(u"imgs_file_manager/cipher.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCipher.setIcon(icon10)
        self.actionDecipher = QAction(MainWindow)
        self.actionDecipher.setObjectName(u"actionDecipher")
        icon11 = QIcon()
        icon11.addFile(u"imgs_file_manager/decipher.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDecipher.setIcon(icon11)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.undo_btn = QPushButton(self.centralwidget)
        self.undo_btn.setObjectName(u"undo_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.undo_btn.sizePolicy().hasHeightForWidth())
        self.undo_btn.setSizePolicy(sizePolicy1)
        self.undo_btn.setMaximumSize(QSize(30, 30))
        icon12 = QIcon()
        icon12.addFile(u":/imgs_file_manager/undo-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.undo_btn.setIcon(icon12)
        self.undo_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.undo_btn)

        self.redo_btn = QPushButton(self.centralwidget)
        self.redo_btn.setObjectName(u"redo_btn")
        self.redo_btn.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.redo_btn.sizePolicy().hasHeightForWidth())
        self.redo_btn.setSizePolicy(sizePolicy1)
        self.redo_btn.setMaximumSize(QSize(30, 30))
        icon13 = QIcon()
        icon13.addFile(u":/imgs_file_manager/redo-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.redo_btn.setIcon(icon13)
        self.redo_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.redo_btn)

        self.up_btn = QPushButton(self.centralwidget)
        self.up_btn.setObjectName(u"up_btn")
        sizePolicy1.setHeightForWidth(self.up_btn.sizePolicy().hasHeightForWidth())
        self.up_btn.setSizePolicy(sizePolicy1)
        self.up_btn.setMaximumSize(QSize(30, 30))
        icon14 = QIcon()
        icon14.addFile(u":/imgs_file_manager/level-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.up_btn.setIcon(icon14)
        self.up_btn.setIconSize(QSize(15, 15))

        self.horizontalLayout_2.addWidget(self.up_btn)

        self.directory = QLabel(self.centralwidget)
        self.directory.setObjectName(u"directory")
        self.directory.setAutoFillBackground(False)
        self.directory.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 5px;\n"
"\n"
"\n"
"")
        self.directory.setLineWidth(2)

        self.horizontalLayout_2.addWidget(self.directory)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 8)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.driverView = QHBoxLayout()
        self.driverView.setSpacing(5)
        self.driverView.setObjectName(u"driverView")

        self.verticalLayout_2.addLayout(self.driverView)

        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setEnabled(True)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QSize(1, 0))
        self.treeView.setMaximumSize(QSize(1000000, 100000))

        self.verticalLayout_2.addWidget(self.treeView)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 20)

        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 975, 25))
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
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
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCipher)
        self.menuFile.addAction(self.actionDecipher)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionNew_File)
        self.toolBar.addAction(self.actionMake_folder)
        self.toolBar.addAction(self.actionMove)
        self.toolBar.addAction(self.actionRename)
        self.toolBar.addAction(self.actionDelete_folder)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u043a\u0430", None))
#if QT_CONFIG(shortcut)
        self.actionPaste.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0440\u0435\u0437\u0430\u043d\u0438\u0435", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"\u041e Qt", None))
        self.actionRename.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u0442\u044c", None))
        self.actionMake_folder.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u043f\u0430\u043f\u043a\u0430", None))
        self.actionDelete_folder.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435", None))
        self.actionNew_File.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0444\u0430\u0439\u043b", None))
        self.actionMove.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435", None))
        self.actionCipher.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.actionDecipher.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.undo_btn.setText("")
        self.redo_btn.setText("")
        self.directory.setText("")
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043a\u0430", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

