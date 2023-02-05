from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGridLayout, QSystemTrayIcon, qApp, QAction, QMenu

from watch import Watch
from current import Current, History


class Weather(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(540, 240))
        self.setWindowTitle("Senex")
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
        self.setStyleSheet("QLabel { color: white }")
        
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QRect(3, 2, 535, 235))
        self.layoutWidget.setObjectName("layoutWidget")
        
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        tempfont = QFont()
        tempfont.setPointSize(40)
        cityfont = QFont()
        cityfont.setPointSize(18)
        midfont = QFont()
        midfont.setPointSize(12)
        smallfont = QFont()
        smallfont.setPointSize(10)
        
        self.datetime = QLabel(self.layoutWidget)
        self.datetime.setFont(midfont)
        self.datetime.setObjectName("datetime")
        self.gridLayout.addWidget(self.datetime, 0, 0, 1, 5)
        
        self.city = QLabel(self.layoutWidget)
        self.city.setFont(cityfont)
        self.city.setObjectName("city")
        self.gridLayout.addWidget(self.city, 1, 0, 1, 5)
        
        self.temp = QLabel(self.layoutWidget)
        self.temp.setFont(tempfont)
        self.temp.setAlignment(Qt.AlignCenter)
        self.temp.setObjectName("temp")
        self.gridLayout.addWidget(self.temp, 2, 0, 2, 1)
        
        self.icon = QLabel(self.layoutWidget)
        self.icon.setObjectName("icon")
        self.gridLayout.addWidget(self.icon, 2, 1, 2, 2)
        
        self.weather = QLabel(self.layoutWidget)
        self.weather.setFont(midfont)
        self.weather.setObjectName("weather")
        self.gridLayout.addWidget(self.weather, 2, 3, 1, 2)
        
        self.feels = QLabel(self.layoutWidget)
        self.feels.setFont(midfont)
        self.feels.setObjectName("feels")
        self.gridLayout.addWidget(self.feels, 3, 3, 1, 2)
        
        self.sunrise = QLabel(self.layoutWidget)
        self.sunrise.setFont(midfont)
        self.sunrise.setObjectName("sunrise")
        self.gridLayout.addWidget(self.sunrise, 4, 0, 1, 3)
        
        self.sunset = QLabel(self.layoutWidget)
        self.sunset.setFont(midfont)
        self.sunset.setObjectName("sunset")
        self.gridLayout.addWidget(self.sunset, 4, 3, 1, 2)
        
        self.wind = QLabel(self.layoutWidget)
        self.wind.setFont(midfont)
        self.wind.setObjectName("wind")
        self.gridLayout.addWidget(self.wind, 5, 0, 1, 2)
        
        self.humidity = QLabel(self.layoutWidget)
        self.humidity.setFont(midfont)
        self.humidity.setObjectName("humidity")
        self.gridLayout.addWidget(self.humidity, 5, 2, 1, 2)
        
        self.pressure = QLabel(self.layoutWidget)
        self.pressure.setFont(midfont)
        self.pressure.setObjectName("pressure")
        self.gridLayout.addWidget(self.pressure, 5, 4, 1, 1)
        
        self.yandex = QLabel(self.layoutWidget)
        self.yandex.setFont(smallfont)
        self.yandex.setObjectName("yandex")
        self.gridLayout.addWidget(self.yandex, 6, 0, 1, 5)
        
        self.today = QLabel(self.layoutWidget)
        self.today.setFont(smallfont)
        self.today.setObjectName("today")
        self.gridLayout.addWidget(self.today, 7, 0, 1, 5)
        
        self.tomorrow = QLabel(self.layoutWidget)
        self.tomorrow.setFont(smallfont)
        self.tomorrow.setObjectName("tomorrow")
        self.gridLayout.addWidget(self.tomorrow, 8, 0, 1, 5)
        
        self.setCentralWidget(self.centralwidget)

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('icons/01d.png'))
        
        quit_action = QAction("Закрыть Senex", self)
        quit_action.triggered.connect(qApp.quit)
        
        tray_menu = QMenu()
        tray_menu.addAction(quit_action)
        
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        
        self.history = History(mainwindow=self)
        
        self.watch = Watch(mainwindow=self)
        self.watch.run()

        self.current = Current(mainwindow=self)
        self.current.run()

    def seticon(self, path):
        self.icon.setPixmap(QPixmap(path))
        self.tray_icon.setIcon(QIcon(path))

    def update_history(self):
        self.history.run()


def move2RightBottomCorner(win):
    screen_geometry = QApplication.desktop().availableGeometry()
    screen_size = (screen_geometry.width(), screen_geometry.height())
    win_size = (win.frameSize().width(), win.frameSize().height())
    x = screen_size[0] - win_size[0]
    y = screen_size[1] - win_size[1]
    win.move(x, y)


if __name__ == "__main__":
    import sys
    
    from PyQt5.QtWidgets import QApplication


    app = QApplication(sys.argv)
    main = Weather()
    main.show()
    move2RightBottomCorner(main)
    sys.exit(app.exec())
