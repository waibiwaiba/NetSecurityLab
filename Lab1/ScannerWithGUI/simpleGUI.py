import sys
from PyQt6.QtWidgets import (QApplication,  QToolTip, QPushButton,
                              QMessageBox, QMainWindow, QMenu, QTextEdit, QLabel,
                              QHBoxLayout, QVBoxLayout, QWidget)
# from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QFont, QAction, QIcon

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # quit按钮
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(0, 0)

        # 气泡窗口
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 普通按钮
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        # 退出弹窗确定
        # exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        # exitAct.setShortcut('Ctrl+Q')
        # exitAct.setStatusTip('Exit application')
        # exitAct.triggered.connect(QApplication.instance().quit)

        # 状态栏
        # self.statusBar()
        # self.statusBar().showMessage('Ready')

        # 菜单栏
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(exitAct)

        # 子菜单
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('File')
        # impMenu = QMenu('Import', self)
        # impAct = QAction('Import mail', self)
        # impMenu.addAction(impAct)
        # newAct = QAction('New', self)
        # fileMenu.addAction(newAct)
        # fileMenu.addMenu(impMenu)
        
        # 勾选菜单栏
        # self.statusbar = self.statusBar()
        # self.statusbar.showMessage('Ready')
        # menubar = self.menuBar()
        # viewMenu = menubar.addMenu('View')
        # viewStatAct = QAction('View statusbar', self, checkable=True)
        # viewStatAct.setStatusTip('View statusbar')
        # viewStatAct.triggered.connect(self.toggleMenu)
        # viewMenu.addAction(viewStatAct)
        
        # 工具栏
        # exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        # exitAct.setShortcut('Ctrl+Q')
        # exitAct.triggered.connect(QApplication.instance().quit)
        # self.toolbar = self.addToolBar('Exit')
        # self.toolbar.addAction(exitAct)

        # 文本编辑窗口
        # textEdit = QTextEdit()
        # self.setCentralWidget(textEdit)

        # 绝对布局
        lbl1 = QLabel('ZetCode', self)
        lbl1.move(15, 10)

        # 水平、竖直布局
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        # self.setGeometry(300, 300, 300, 200)
        self.resize(350, 250)
        self.center()
        self.setWindowTitle('Tooltips')
        self.show()

    def closeEvent(self, event):
        '''退出事件'''
        reply = QMessageBox.question(self, 'Message',
                    "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                    QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
    
    
    def center(self):
        '''窗口居中'''
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def toggleMenu(self, state):
        '''勾选菜单栏'''
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def contextMenuEvent(self, event):
        '''上下文菜单'''
        cmenu = QMenu(self)
        newAct = cmenu.addAction("New")
        openAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec(self.mapToGlobal(event.pos()))

        if action == quitAct:
            QApplication.instance().quit()
def main():
    app = QApplication(sys.argv)
    ex = Example()


    sys.exit(app.exec())

if __name__ == '__main__':
    main()