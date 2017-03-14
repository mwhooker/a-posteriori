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
    def __init__(self, locks):
        self.locks = locks
        self.inside = self.npoints = 0

    def __call__(self, lock):
        for _ in itertools.count(1):
            with lock():
                x = random.random()
                y = random.random()
                with lock:
                    self.npoints += 1
                    if in_circle(x, y):
                        self.inside += 1

    def print_results(self, exit):
        with self.locks:
            print
            print("iterations: ", self.npoints)
            print(4 * self.inside / self.npoints)
            if exit:
                sys.exit(0)
    
if __name__ == '__main__':


    max_workers = 1
    locks = Multilock()
    sim = Simulator(locks)

    for i in range(max_workers):
        Process(target=sim, args=(locks.lock(),)).start()

    signal.signal(signal.SIGINT, lambda *args: sim.print_results(False))
    signal.signal(signal.SIGQUIT, lambda *args: sim.print_results(True))
