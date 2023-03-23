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
│       recvUDP.c	# 接收发送进PORT端口的数据包
|		Mylibpcap.c # Lab2抓包程序
│
└─Sender
        config.txt	# 源、目的ip地址和端口号的设置
        createPac.c	# 发送数据包
        payload.txt	# 欲发送的数据内容
```

### 如何运行

#### Mylibpcap.c

##### 安装libpcap库

```bash
sudo apt update
sudo apt install libpcap-dev
```

##### 编译、运行

先用 `ifconfig` 指令查看 ubuntu 里用的是哪个网络适配器。

```bash
(base) lx120l020121@ubuntu:~/CODE/Mylibnet$ ifconfig
docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        ether 02:42:6e:46:e6:4b  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

ens38: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.126.128  netmask 255.255.255.0  broadcast 192.168.126.255
        inet6 fe80::290e:efc7:b2e8:fdc3  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:15:c5:aa  txqueuelen 1000  (Ethernet)
        RX packets 10378  bytes 4474588 (4.4 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 8016  bytes 2738442 (2.7 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 12413  bytes 2973256 (2.9 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 12413  bytes 2973256 (2.9 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

在虚拟机采用NAT模式时，分配了子网地址的正在`RUNNING` 的 `ens38` 就是应该设置为`DEVICE_NAME`的网络适配器。

编译：`gcc Mylibpcap.c -o Mylibpcap`

运行：`sudo ./Mylibpcap`

#### recvUDP.c

编译：`gcc recvUDP.c -o recvUDP` 

运行：`sudo ./recvUDP`

#### createPac.c

先设置config.txt和payload.txt。

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