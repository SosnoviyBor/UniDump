from threading import Lock

class Int:
    """Thread-safe integer"""
    
    i = 0
    lock = Lock()
    
    def inc(self):
        with self.lock:
            self.i += 1
    
    def dec(self):
        with self.lock:
            self.i -= 1
    
    def get(self):
        with self.lock:
            return self.i