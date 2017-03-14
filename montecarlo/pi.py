#/usr/bin/env python3
import random
import sys
import itertools
import math
import signal
import functools

from contextlib import ContextDecorator
from multiprocessing import Process, Lock


def in_circle(x, y):
    return math.sqrt(x**2 + y**2) <= 1

def signal_handler(signal, frame, f):
    f()
    sys.exit(0)


class Multilock(list, ContextDecorator):
    def __enter__(self):
        for lock in self:
            lock.acquire()

    def __exit__(self, *exc):
        for lock in self:
            lock.release()

    def lock(self, *args, **kwargs):
        lock = Lock(*args, **kwargs)
        self.append(lock)
        return lock


class Simulator(object):
    def __init__(self):
        self.ip = Array('long', [0, 0])

    def __call__(self, lock):
        for _ in itertools.count(1):
            x = random.random()
            y = random.random()
            with self.ip.get_lock():
                self.ip.value[0] += 1
                if in_circle(x, y):
                    self.ip.value[1] += 1

    def print_results(self, exit):
        with self.ip.get_lock():
            print
            print("iterations: ", self.ip.value[0])
            print(4 * self.ip.value[0] / self.ip.value[1])
            if exit:
                sys.exit(0)
    
if __name__ == '__main__':


    max_workers = 1
    locks = Multilock()
    sim = Simulator()

    for i in range(max_workers):
        Process(target=sim).start()

    signal.signal(signal.SIGINT, lambda *args: sim.print_results(False))
    signal.signal(signal.SIGQUIT, lambda *args: sim.print_results(True))
