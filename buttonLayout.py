# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtWidgets import QCheckBox, QVBoxLayout, QHBoxLayout, QWidget, QGroupBox, QButtonGroup, QRadioButton


class ButtonLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QCheckBox and QRadioButtn")
        # os
        os = QGroupBox("Choose os")
        windows = QCheckBox("Windows")
        linux = QCheckBox("Linux")
        mac = QCheckBox("Mac")

        #drinks
        drinks = QGroupBox("Choose drink")
        beer = QCheckBox("Beer")
        coffe = QCheckBox("Coffe")
        juice = QCheckBox("Juice")
        beer.setChecked(True)

        #radio buttons
        answers = QGroupBox("Choose Answer")
        answer_a = QRadioButton("A")
        answer_b = QRadioButton("B")
        answer_c = QRadioButton("C")
        answer_a.setChecked(True)

        #Make the checkboxes exclusive
        exclusive_button_group = QButtonGroup(self)
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(juice)
        exclusive_button_group.addButton(coffe)
        exclusive_button_group.setExclusive(True)

        # set events
        windows.toggled.connect(self.window_box_toggled)
        linux.toggled.connect(self.linux_box_toggled)
        mac.toggled.connect(self.mac_box_toggled)

        # add layout

        answers_layout = QVBoxLayout()
        answers_layout.addWidget(answer_a)
        answers_layout.addWidget(answer_b)
        answers_layout.addWidget(answer_c)
        answers.setLayout(answers_layout)

        drink_layout = QVBoxLayout()
        drink_layout.addWidget(beer)
        drink_layout.addWidget(juice)
        drink_layout.addWidget(coffe)
        drinks.setLayout(drink_layout)

        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)

        os.setLayout(os_layout)

        layout = QVBoxLayout()
        layout.addWidget(os)
        layout.addWidget(drinks)
        layout.addWidget(answers)

        h_layout = QHBoxLayout()
        h_layout.addWidget(os)
        h_layout.addWidget(drinks)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(answers)

        self.setLayout(v_layout)

    def window_box_toggled(self, checked):
        if (checked):
            print("Winodows box checked")
        else:
            print("Winodows box unchecked")

    def linux_box_toggled(self, checked):
        if (checked):
            print("Linux box checked")
        else:
            print("Linux box unchecked")

    def mac_box_toggled(self, checked):
        if (checked):
            print("Mac box checked")
        else:
            print("Mac box unchecked")
