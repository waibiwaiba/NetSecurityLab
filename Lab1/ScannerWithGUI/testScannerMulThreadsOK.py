import threading
import socket
import time

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.07)   # 超时时间设置太大会导致扫描过程很慢，0.07都可以扫百度了。
    # print("Scanning:    {}:{}".format(ip, port))
    result = sock.connect_ex((ip, port))
    sock.close()
    if result == 0:
        print(f"Port {port} is open")

def scan_thread(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

def scan_ip(ip, start_port, end_port, num_threads):
    start_time = time.time()
    ports_per_thread = (end_port - start_port + 1) // num_threads
    threads = []

    for i in range(num_threads):
        if i == num_threads - 1:
            # last thread takes remaining ports
            end = end_port
        else:
            end = start_port + ports_per_thread - 1
        thread = threading.Thread(target=scan_thread, args=(ip, start_port, end))
        threads.append(thread)
        start_port = end + 1

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Scanning completed in {time.time()-start_time:.2f} seconds.")

scan_ip('127.0.0.1', 1, 1090, 4)
# ip address of baidu.com: 39.156.66.10