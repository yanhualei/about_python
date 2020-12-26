from multiprocessing.dummy import Pool
import queue
import threading

class Foo:
    def __init__(self):
        self.q=queue.Queue()
        self.pool = Pool()

    def first(self):
        print("1")
        self.q.put(2)

    def second(self):
        res = self.q.get()
        print(res)
        self.q.put(3)

    def third(self):
        res = self.q.get()
        print(res)

    def run(self):
        self.third()
        self.first()
        self.second()


    def main(self):
        self.pool.apply_async(self.run)
if __name__ == '__main__':
    Foo().run()
