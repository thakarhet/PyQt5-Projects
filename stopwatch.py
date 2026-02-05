import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel , QWidget , QVBoxLayout ,QHBoxLayout , QPushButton
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00.000", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_display)
        
        self.initUI()
    def start(self):
        self.timer.start(10)
    def stop(self):
        self.timer.stop()
    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))
    def format_time(self):
        hours = self.time.hour()
        minutes = self.time.minute()
        seconds = self.time.second()
        milliseconds = self.time.msec()
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"
    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
    
    def initUI(self):
        self.setWindowTitle("Watch")   

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        vbox = QVBoxLayout()
        central_widget.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.time_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)
        self.setStyleSheet("QPushButton {font-size: 20px;}"
                         "QLabel {font-size: 30px; font-weight: bold; color: hsl(211,100%,50%); background-color: black;}"
                         "QMainWindow {background-color: black;}")
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
    