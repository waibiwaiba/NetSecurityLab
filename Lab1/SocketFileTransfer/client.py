import socket
import os

# 创建TCP socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务端 192.168.94.133
# TODO// server ip
client_socket.connect(("192.168.94.133", 8888))

while True:
    # 提示用户输入命令
    command = input("Please enter the command (upload or download or close): ")

    # 处理上传文件请求
    if command == "upload":
        client_socket.send(f"upload".encode())
        # str1 = "/Lab1/SocketFileTransfer/"
        # str2 = (os.getcwd() + str1).replace("\\", "/")
        # 奇怪的事发生了，之前都是好的，不知道为什么到验收的时候就突然路径重复了
        # 就变成下面这个鬼东西了。
        # D:/VSCODE/NetSecurityLab/Lab1/SocketFileTransfer/Lab1/SocketFileTransfer/
        str2 = os.getcwd()
        print("Your current filepath is:")
        print(str2)
        print("You can upload those files:")
        for files in os.listdir(str2):  # 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
            print(files)
        # 提示用户输入文件名
        filename = input("Please enter the filename you want to upload: ")
        abspath = os.path.join(str2, filename)
        # 如果文件存在，计算文件大小并发送文件名和大小给服务端
        if os.path.exists(abspath):
            filesize = os.path.getsize(abspath)
            client_socket.send(f"{filename}|{filesize}".encode())

            # 等待接受服务器发回的确认文件大小和名称的信息
            ACK = False
            ACK_File = client_socket.recv(1024).decode()
            if ACK_File == "file name and size have been received.":
                print("Server has received file name and size.")
                ACK = True
            # 打开文件并发送给服务端
            with open(abspath, "rb") as f:
                data = f.read(1024)
                while data and ACK:
                    print("Sending data to server.")
                    client_socket.send(data)
                    data = f.read(1024)
            if ACK:
                print(f"{filename} has been uploaded to the server.")
            else:
                print("Server didn't receive file name and size.")
        else:
            print(f"{filename} does not exist in the current directory.")
    # 处理下载文件请求
    elif command == "download":
        # 获取服务端当前目录下的文件列表
        client_socket.send("download".encode())
        file_list = client_socket.recv(1024).decode()

        # 显示服务端当前目录下的文件列表
        print("The files in the current directory are:")
        print(file_list)

        # 提示用户输入需要下载的文件名
        filename = input("Please enter the filename you want to download: ")

        # 发送需要下载的文件名给服务端
        client_socket.send(filename.encode())

        # 接收服务端发送的文件名和大小
        response = client_socket.recv(1024).decode()
        if response.startswith("File"):
            # 如果文件不存在，显示错误信息
            print(response)
        else:
            filename, filesize = response.split("|")
            filesize = int(filesize)

            # 打开文件，准备写入
            with open(filename, "wb") as f:
                # 从服务端接收数据并写入文件
                data = client_socket.recv(1024)
                total_recv_size = len(data)
                f.write(data)
                while total_recv_size < filesize:
                    data = client_socket.recv(1024)
                    total_recv_size += len(data)
                    f.write(data)
            print(f"{filename} has been downloaded from the server.")
    # 断开连接
    elif command == "close":
        client_socket.send("close".encode())
        client_socket.close()
        exit(0)

    else:
        print("Invalid command. Please enter upload or download.")
