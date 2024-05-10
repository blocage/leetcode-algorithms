from threading import Lock

class Foo:
    def __init__(self):
        self.first_lock = Lock()
        self.second_lock = Lock()
        self.first_lock.acquire()
        self.second_lock.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first_lock.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.first_lock:
            printSecond()
            self.second_lock.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.second_lock:
            printThird()