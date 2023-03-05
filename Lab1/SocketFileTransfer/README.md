使用方法：
- 用 `ifconfig` 命令得到 linux 虚拟机的 ip 地址，代替`server.py`文件中的 server ip 地址，并在 linux 虚拟机上运行 `server.py`
- 用户机上的`client.py`文件里的 server ip 地址也设置完毕后，运行 `client.py` 
- 输入 upload, download, close 可分别实现
  - 从用户端往服务器端上传文件
  - 从服务器端往用户端下载文件
  - 用户端退出连接
