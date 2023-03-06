class PortScanner(threading.Thread):
    def __init__(self, ip_range, port_range, thread_num, result_box):
        super().__init__()
        self.ip_range = ip_range
        self.port_range = port_range
        self.thread_num = thread_num
        self.result_box = result_box
        self.daemon = True
        self._stop_event = threading.Event()
        self._lock = threading.Lock()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        start_time = time.time()
        total_ports = len(self.ip_range) * len(self.port_range)
        open_ports = []

        def scan(ip_address, port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            try:
                sock.connect((ip_address, port))
                with self._lock:
                    open_ports.append(port)
            except:
                pass
            finally:
                sock.close()

        threads = []
        for i in range(self.thread_num):
            thread = threading.Thread(target=self._scan_worker)
            thread.start()
            threads.append(thread)

        for ip in self.ip_range:
            for port in self.port_range:
                if self.stopped():
                    return
                while threading.active_count() > self.thread_num:
                    time.sleep(0.1)
                if self.stopped():
                    return
                threading.Thread(target=scan, args=(ip, port)).start()

        for thread in threads:
            thread.join()

        elapsed_time = time.time() - start_time
        result = f"Scan finished in {elapsed_time:.2f} seconds. Scanned {total_ports} ports, {len(open_ports)} open ports.\nOpen ports: {', '.join(map(str, open_ports))}"
        self.result_box.append(result)

    def _scan_worker(self):
        while True:
            if self.stopped():
                break
            time.sleep(0.1)