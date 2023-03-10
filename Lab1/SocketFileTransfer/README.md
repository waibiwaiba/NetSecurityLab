使用方法：
- 用 `ifconfig` 命令得到 linux 虚拟机的 ip 地址，代替`server.py`文件中的 server ip 地址，并在 linux 虚拟机上运行 `server.py`
- 用户机上的`client.py`文件里的 server ip 地址也设置完毕后，运行 `client.py` 
- 输入 upload, download, close 可分别实现
  - 从用户端往服务器端上传文件
  - 从服务器端往用户端下载文件
  - 用户端退出连接

~~把实验要求输给chatGPT之后，得到的代码debug一下就可以用了。AI真是个好东西。。~~
### 一些bug
- 莫名其妙的无法连接错误，如：
  > Traceback (most recent call last):
  > File "D:\VSCODE\NetSecurityLab\Lab1\SocketFileTransfer\client.py", line 9, in <module>
  >   client_socket.connect(("192.168.94.133", 8888))
  > TimeoutError: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。

  报错：积极拒绝 可能是因为服务器端的代码并未运行。
  > Traceback (most recent call last):
  > File "D:\VSCODE\NetSecurityLab\Lab1\SocketFileTransfer\client.py", line 9, in <module>
  >  client_socket.connect(("192.168.94.133", 8888))
  > ConnectionRefusedError: [WinError 10061] 由于目标计算机积极拒绝，无法连接。

- 单次运行客户端时，只能执行upload或download一个功能。想使用两个功能的话，在输入第二种指令后会卡死。我也懒得修这个bug了。。。明明之前有一个版本可以连着upload和download的。😣