import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_ellipse(self, qp):
        qp.setBrush(QColor(250, 221, 115))
        d = random.randint(10, 300)
        qp.drawEllipse(40, 40, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
