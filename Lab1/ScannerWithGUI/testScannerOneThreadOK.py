import socket
import time

# 输入要扫描的IP地址和端口范围
# ip = input("请输入要扫描的IP地址：")
# start_port = int(input("请输入要扫描的起始端口号："))
# end_port = int(input("请输入要扫描的结束端口号："))

# ip = '127.0.0.1'
ip = '192.168.94.133'
start_port = 1
end_port = 1090


# 初始化计数器
open_ports = 0
total_ports = 0

# 记录开始扫描的时间
start_time = time.time()

# 循环扫描指定端口
for port in range(start_port, end_port + 1):
    # 创建 socket 对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置连接超时时间为1秒
    client_socket.settimeout(0.001)
    # 尝试连接指定端口
    try:
        # print("正在扫描：{}:{}".format(ip, port))
        client_socket.connect((ip, port))
        print("端口 " + str(port) + " 开放")
        open_ports += 1
    except:
        pass
    # 关闭 socket 连接
    client_socket.close()
    total_ports += 1

# 计算扫描的时间
scan_time = time.time() - start_time

# 输出结果
print("扫描完成！")
print("扫描花费时间：" + str(scan_time) + "秒")
print("扫描的总端口数：" + str(total_ports))
print("开放的端口数：" + str(open_ports))
