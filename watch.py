from PyQt5.QtCore import QThread, QTimer

from dt import dt


class Watch(QThread):

    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow
        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)
        self.showTime()

    def run(self):
        self.timer.start(1000)
    
    def showTime(self):
        self.mainwindow.datetime.setText(dt())
