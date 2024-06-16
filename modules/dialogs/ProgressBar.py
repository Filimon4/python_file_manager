from PySide6.QtWidgets import QProgressDialog
from PySide6.QtCore import QTimer

class ProgressBar(QProgressDialog):

    def __init__(self, title="Прогресс", btn="Отмена", min=0, max=100, step=1):
        super().__init__(title, btn, min, max)
        self.min = min
        self.max = max
        self.currentValue = min
        self.step = step
        super().setValue(self.min)
        super().setMinimumDuration(2000)

    def progres(self):
        nextStep = self.currentValue + self.step
        super().setValue(nextStep)

    def cancel(self):
        pass
