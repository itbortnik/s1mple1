import sys
import random
from PyQt6 import QtWidgets, QtGui, QtCore
from ui_mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(800, 600)

        self.ui.pushButton.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        diameter = random.randint(10, 100)
        w = self.ui.centralwidget.width()
        h = self.ui.centralwidget.height()
        x = random.randint(diameter // 2, w - diameter // 2)
        y = random.randint(diameter // 2, h - diameter // 2)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.setPen(QtCore.Qt.PenStyle.NoPen)
        painter.setBrush(QtGui.QColor('yellow'))
        for (x, y, d) in self.circles:
            painter.drawEllipse(QtCore.QPointF(x, y), d / 2.0, d / 2.0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())