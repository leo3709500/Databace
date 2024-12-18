from PyQt5 import QtWidgets, QtCore

class MacButtons:
    def __init__(self, main_widget, main_window):
        self.main_widget = main_widget
        self.main_window = main_window
        self.is_dragging = False
        self.setup_mac_buttons()

    def setup_mac_buttons(self):
        # 添加 Mac OS 風格的紅橘綠按鈕
        self.button_close = QtWidgets.QPushButton(self.main_widget)
        self.button_close.setGeometry(QtCore.QRect(10, 10, 15, 15))
        self.button_close.setStyleSheet("""
            QPushButton {
                background-color: #FF605C;
                border: none;
                border-radius: 7px;
            }
            QPushButton:hover {
                background-color: #FF1F1F;
            }
        """)
        
        self.button_minimize = QtWidgets.QPushButton(self.main_widget)
        self.button_minimize.setGeometry(QtCore.QRect(30, 10, 15, 15))
        self.button_minimize.setStyleSheet("""
            QPushButton {
                background-color: #FFBD44;
                border: none;
                border-radius: 7px;
            }
            QPushButton:hover {
                background-color: #FFAA00;
            }
        """)
        
        self.button_maximize = QtWidgets.QPushButton(self.main_widget)
        self.button_maximize.setGeometry(QtCore.QRect(50, 10, 15, 15))
        self.button_maximize.setStyleSheet("""
            QPushButton {
                background-color: #00CA4E;
                border: none;
                border-radius: 7px;
            }
            QPushButton:hover {
                background-color: #00B324;
            }
        """)

        # 連接按鈕的點擊事件
        self.button_close.clicked.connect(self.main_window.close)
        self.button_minimize.clicked.connect(self.main_window.showMinimized)
        self.button_maximize.clicked.connect(self.main_window.showMaximized)

        self.main_window.setMouseTracking(True)
        self.main_window.mousePressEvent = self.mousePressEvent
        self.main_window.mouseMoveEvent = self.mouseMoveEvent
        self.main_window.mouseReleaseEvent = self.mouseReleaseEvent

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.is_dragging = True
            self.drag_position = event.globalPos() - self.main_window.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.is_dragging:
            self.main_window.move(event.globalPos() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.is_dragging = False
            event.accept() 