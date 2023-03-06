打算用 pyqt6 写GUI

参考：https://maicss.gitbook.io/pyqt-chinese-tutoral/pyqt6

~~先写脚本，实现扫描功能，再编辑GUI。~~
实际是先用了chatGPT写GUI，再用chatGPT写扫描器单线程脚本->多线程脚本->整合到GUI程序中

实验需求：
在 Windows 环境下利用 socket 的 connect 函数进行扫描器的设计，要求有界面，界面能够输入扫描的 ip 范围和端口范围，和需使用的线程数，显示结果。
界面由一个vbox组成，vbox里从上到下分别为：
1. 设置扫描参数，其中利用lineedit可以设置ip范围和端口范围、线程数。
2. 开始扫描与结束扫描的按钮。点击对应按钮可以开始、结束扫描。
3. 显示扫描结果的textedit子部件。在扫描结束后单独打印出开启的端口号，并且打印此次扫描花费的时间、扫描的总端口数以及开启的端口数。


扫描结果：socket连接超时时间设置为0.07s，设置为4线程时，有：
1. 扫描39.156.66.10(baidu.com)，Scanning completed in 19.21 seconds. Scanned 1090 ports. 2 ports are open.
2. 扫描127.0.0.1(localhost)，Scanning completed in 19.08 seconds. Scanned 1090 ports. 9 ports are open.

bug:
- stop scan按钮功能未完成。点击后仍会在完成扫描后结束扫描，不能实现在扫描中途停止扫描的功能。
