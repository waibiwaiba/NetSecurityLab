import sys
import socket
import time
import threading
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QHBoxLayout,
)
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import Qt


class IPAddressInput(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(50)
        self.setMaxLength(3)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        validator = QIntValidator(0, 255, self)
        self.setValidator(validator)


class IPInputBox(QHBoxLayout):
    def __init__(self, title, parent=None):
        super().__init__(parent)

        self.addWidget(QLabel(title))
        self.ip_address_1 = IPAddressInput()
        self.addWidget(self.ip_address_1)
        self.addWidget(QLabel("."))
        self.ip_address_2 = IPAddressInput()
        self.addWidget(self.ip_address_2)
        self.addWidget(QLabel("."))
        self.ip_address_3 = IPAddressInput()
        self.addWidget(self.ip_address_3)
        self.addWidget(QLabel("."))
        self.ip_address_4 = IPAddressInput()
        self.addWidget(self.ip_address_4)

    def get_ip_address(self):
        return ".".join(
            [
                self.ip_address_1.text(),
                self.ip_address_2.text(),
                self.ip_address_3.text(),
                self.ip_address_4.text(),
            ]
        )


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置IP范围和端口范围的输入框
        # 起始\结束IP地址输入框
        self.start_ip_box = IPInputBox("Start IP")
        self.end_ip_box = IPInputBox("End  IP")

        self.start_port = QLineEdit()
        self.start_port.setPlaceholderText("Start Port")
        self.start_port.setFixedWidth(100)

        self.end_port = QLineEdit()
        self.end_port.setPlaceholderText("End Port")
        self.end_port.setFixedWidth(100)

        port_validator = QIntValidator(1, 65535, self)
        self.start_port.setValidator(port_validator)
        self.end_port.setValidator(port_validator)

        # 设置线程数为1-9之间某个值
        self.threads = QLineEdit()
        self.threads.setPlaceholderText("Threads")
        self.threads.setFixedWidth(100)
        threads_validator = QIntValidator(1, 9, self)
        self.threads.setValidator(threads_validator)

        # 开始扫描和结束扫描按钮
        self.start_btn = QPushButton("Start Scan")
        self.stop_btn = QPushButton("Stop Scan")
        self.start_btn.clicked.connect(self.start_scan)
        self.stop_btn.clicked.connect(self.stop_scan)

        # 扫描结果显示框
        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)

        # 将所有部件添加到vbox中
        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("IP Address Range:"))
        vbox.addLayout(self.start_ip_box)
        vbox.addLayout(self.end_ip_box)
        vbox.addWidget(QLabel("Port Range:"))
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.start_port)
        hbox1.addWidget(QLabel("-"))
        hbox1.addWidget(self.end_port)
        vbox.addLayout(hbox1)
        vbox.addWidget(QLabel("Threads:"))
        vbox.addWidget(self.threads)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.start_btn)
        hbox2.addWidget(self.stop_btn)
        vbox.addLayout(hbox2)
        vbox.addWidget(QLabel("Scan Result:"))
        vbox.addWidget(self.result_box)

        self.setLayout(vbox)

        self.setWindowTitle("Port Scanner")
        self.show()

    def start_scan(self):
        pass

    def stop_scan(self):
        pass


def main():

    app = QApplication(sys.argv)
    myScanner = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
