from collections import deque
class BufferFullException(Exception):
    pass
class BufferEmptyException(Exception):
    pass
class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.__deque = deque([], capacity)
    def read(self):
        try:
            return self.__deque.pop()
        except Exception:
            raise BufferEmptyException("read while buffer is empty")
    def write(self, d):
        if len(self.__deque) < self.capacity:
            self.__deque.appendleft(d)
        else:
            raise BufferFullException("write while buffer is full")
    def clear(self):
        self.__deque.clear()
    def overwrite(self, d):
        try:
            self.write(d)
        except Exception:
            self.__deque.pop()
            self.__deque.appendleft(d)