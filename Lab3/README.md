### 文件列表

```css
PS D:\VSCODE\NetSecurityLab\Lab3> tree /f
卷 Data 的文件夹 PATH 列表
卷序列号为 D62E-479E
D:.
│  README.md
│  第3次实验_实验报告模板.docx
│
├─Recevier
│      recvUDP.c	# 接收发送进PORT端口的数据包
│
└─Sender
        config.txt	# 源、目的ip地址和端口号的设置
        createPac.c	# 发送数据包
        payload.txt	# 欲发送的数据内容
```

### 如何运行

#### recvUDP.c

编译：`gcc recvUDP.c -o recvUDP` 

运行：`sudo ./recvUDP`

#### createPac.c

##### 安装libnet库

**不要**直接`sudo apt-get install libnet-dev`，这会安装`libnet1-dev`包，旧，手动编译更新的包。

去：https://github.com/libnet/libnet 的 `release` 页面下最新的`.tar.tz` 包。然后按照仓库主页的md文件的指令手动编译即可。

```bash
tar xf libnet-x.y.z.tar.gz
cd libnet-x.y.z/
./configure && make
sudo make install
```

##### 编译、运行

编译： `gcc -o createPac createPac.c -lnet`  其中 `-lnet` 参数是编译时链接 `libnet` 库。

运行：`sudo ./createPac`

若出现链接库时路径有问题，用报错信息问chatGPT可解决相关问题。