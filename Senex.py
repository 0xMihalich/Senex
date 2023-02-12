from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QGridLayout, QSystemTrayIcon, qApp, QAction, QMenu, QDesktopWidget

from current import Current, History
from lat_lon import lat_lon
from search import Search
from sqlbase import conn
from watch import Watch


class Weather(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(540, 240))
        self.setWindowTitle("Senex")
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
        with conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM settings;')
            (color, position) = cur.fetchone()
            cur.execute('SELECT timezone, lat, lon FROM info;')
            info = cur.fetchone()
        self.change_color(color)
        self.position(position)
        del color, position
        
        self.timezone = info[0] if info else 0
        self.geo = (info[1], info[2]) if info else None
        
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QRect(3, 2, 515, 235))
        self.layoutWidget.setObjectName("layoutWidget")
        
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setAlignment(Qt.AlignLeft)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        tempfont = QFont()
        tempfont.setPointSize(40)
        cityfont = QFont()
        cityfont.setPointSize(16)
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
        
        position_action = QMenu("Положение виджета", self)
        color_action = QMenu("Цвет текста", self)
        city_action = QAction("Выбрать город", self)
        update_action = QAction("Обновить местоположение", self)
        quit_action = QAction("Закрыть Senex", self)
        
        tray_menu = QMenu()
        tray_menu.addMenu(position_action)
        tray_menu.addMenu(color_action)
        tray_menu.addAction(city_action)
        tray_menu.addAction(update_action)
        tray_menu.addAction(quit_action)
        
        center_action = QAction("По центру", self)
        upleft_action = QAction("Слева вверху", self)
        downleft_action = QAction("Слева внизу", self)
        upright_action = QAction("Справа вверху", self)
        downright_action = QAction("Справа внизу", self)
        
        position_action.addAction(center_action)
        position_action.addAction(upleft_action)
        position_action.addAction(downleft_action)
        position_action.addAction(upright_action)
        position_action.addAction(downright_action)
        
        white_action = QAction("Белый", self)
        black_action = QAction("Черный", self)
        gray_action = QAction("Серый", self)
        red_action = QAction("Красный", self)
        orange_action = QAction("Оранжевый", self)
        yellow_action = QAction("Желтый", self)
        green_action = QAction("Зеленый", self)
        blue_action = QAction("Синий", self)
        indigo_action = QAction("Индиго", self)
        violet_action = QAction("Фиолетовый", self)
        
        color_action.addAction(white_action)
        color_action.addAction(black_action)
        color_action.addAction(gray_action)
        color_action.addAction(red_action)
        color_action.addAction(orange_action)
        color_action.addAction(yellow_action)
        color_action.addAction(green_action)
        color_action.addAction(blue_action)
        color_action.addAction(indigo_action)
        color_action.addAction(violet_action)
        
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        
        self.history = History(mainwindow=self)
        self.watch = Watch(mainwindow=self)
        self.current = Current(mainwindow=self)
        self.search = Search(mainwindow=self)
        
        self.watch.run()
        self.history.run()
        self.current.run()
        
        center_action.triggered.connect(lambda: self.position('center'))
        upleft_action.triggered.connect(lambda: self.position('upleft'))
        downleft_action.triggered.connect(lambda: self.position('downleft'))
        upright_action.triggered.connect(lambda: self.position('upright'))
        downright_action.triggered.connect(lambda: self.position('downright'))
        
        white_action.triggered.connect(lambda: self.change_color('white'))
        black_action.triggered.connect(lambda: self.change_color('black'))
        gray_action.triggered.connect(lambda: self.change_color('gray'))
        red_action.triggered.connect(lambda: self.change_color('red'))
        orange_action.triggered.connect(lambda: self.change_color('orange'))
        yellow_action.triggered.connect(lambda: self.change_color('yellow'))
        green_action.triggered.connect(lambda: self.change_color('green'))
        blue_action.triggered.connect(lambda: self.change_color('blue'))
        indigo_action.triggered.connect(lambda: self.change_color('indigo'))
        violet_action.triggered.connect(lambda: self.change_color('violet'))
        
        city_action.triggered.connect(lambda: self.search.show())
        
        update_action.triggered.connect(lambda: self.current.new_values())
        
        quit_action.triggered.connect(qApp.quit)
        
        self.show()

    def seticon(self, path):
        self.icon.setPixmap(QPixmap(path))
        self.tray_icon.setIcon(QIcon(path))
    
    def change_color(self, color):
        self.setStyleSheet("QLabel { color: " + color + " }")
        with conn:
            cur = conn.cursor()
            cur.execute(f'UPDATE settings SET color = "{color}";')
            conn.commit()
    
    def position(self, pos):
        """ 'center'    - по центру
            'upleft'    - левый верхний угол
            'downleft'  - левый нижний угол
            'upright'   - правый верхний угол
            'downright' - правый нижний угол (стандартная позиция)"""
        
        _screen = QDesktopWidget().availableGeometry()
        width, height = (_screen.width(), _screen.height())
        x = width - 540
        y = height - 240
        if pos == 'center':
            x, y = x // 2, y // 2
        elif pos == 'upleft':
            x, y = 0, 0
        elif pos == 'downleft':
            x, y = 0, y
        elif pos == 'upright':
            x, y = x, 0
        self.move(x, y)
        with conn:
            cur = conn.cursor()
            cur.execute(f'UPDATE settings SET position = "{pos}";')
            conn.commit()
        del _screen, width, height, x, y, pos


if __name__ == "__main__":
    import sys
    
    from PyQt5.QtWidgets import QApplication


    app = QApplication(sys.argv)
    main = Weather()
    sys.exit(app.exec())
