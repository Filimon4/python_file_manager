# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(535, 141)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fullNameLabel = QLabel(Widget)
        self.fullNameLabel.setObjectName(u"fullNameLabel")

        self.horizontalLayout.addWidget(self.fullNameLabel)

        self.fullNameLineEdit = QLineEdit(Widget)
        self.fullNameLineEdit.setObjectName(u"fullNameLineEdit")

        self.horizontalLayout.addWidget(self.fullNameLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.OccupationLabel = QLabel(Widget)
        self.OccupationLabel.setObjectName(u"OccupationLabel")

        self.horizontalLayout_2.addWidget(self.OccupationLabel)

        self.OccupationLineEdit = QLineEdit(Widget)
        self.OccupationLineEdit.setObjectName(u"OccupationLineEdit")

        self.horizontalLayout_2.addWidget(self.OccupationLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.fullNameLabel.setText(QCoreApplication.translate("Widget", u"FullName", None))
        self.OccupationLabel.setText(QCoreApplication.translate("Widget", u"Occupation", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"PushButton", None))
    # retranslateUi

