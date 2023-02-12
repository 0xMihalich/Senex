from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QListWidget, QDialogButtonBox

from get_city import city_dict


class Search(QWidget):
    city_dict = city_dict()

    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow
        self.setWindowTitle("Поиск города")
        self.setWindowIcon(self.mainwindow.tray_icon.icon())
        self.resize(481, 500)
        
        self.all_city = QListWidget()
        self.all_city.addItems(self.city_dict)
        
        self.widget = QWidget(self)
        self.widget.setGeometry(QRect(5, 10, 471, 481))
        self.widget.setObjectName("widget")
        self.gridLayout = QGridLayout(self.widget)
        
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QLabel(self.widget)
        
        font = QFont()
        font.setPointSize(10)
        
        self.label.setFont(font)
        self.label.setText("Поиск:")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        self.search = QLineEdit(self.widget)
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 0, 1, 1, 1)
        
        self.cityes = QListWidget(self.widget)
        self.cityes.itemDoubleClicked.connect(self.accept)
        self.cityes.setObjectName("cityes")
        self.gridLayout.addWidget(self.cityes, 1, 0, 1, 2)
        
        self.select = QDialogButtonBox(self.widget)
        self.select.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.select.accepted.connect(self.accept)
        self.select.rejected.connect(self.reject)
        self.select.setObjectName("select")
        self.gridLayout.addWidget(self.select, 2, 1, 1, 1)
        
        self.find('')
        self.search.textChanged.connect(self.find)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
    
    def selection(self, item):
        self.search.setText(item.text())
        
    def find(self, item):
        self.cityes.clear()
        self.cityes.addItems(result.text().title() for result in self.all_city.findItems(item.lower(), Qt.MatchContains))
    
    def accept(self):
        result = self.cityes.currentItem()
        if result:
            self.hide()
            lat, lon = self.city_dict[result.text().lower()]
            self.mainwindow.current.new_values((lat, lon))
    
    def reject(self):
        self.hide()
