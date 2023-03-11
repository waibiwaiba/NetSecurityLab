要运行main.c代码，您需要进行以下步骤：

### 1.安装libpcap库：
在终端中运行以下命令：
`sudo apt-get install libpcap-dev`
### 2.编译代码：
按照以下步骤编译并运行这个main.c文件：
a.	在终端中进入main.c所在的目录。
b.	使用以下命令编译main.c文件：
`gcc -o main main.c -lpcap`
该命令将生成一个可执行文件main。
c.	运行可执行文件：
`sudo ./main`
注意：使用libpcap库需要管理员权限。
运行后，程序将捕获本机数据包，并将这些信息写入txt文件中。

### 注：
- PointerAndAddress.cpp 文件与本次实验无关。
- chatHistoryWithChatGPT.md 文件是为了完成这次实验，与chatGPT的聊天记录。