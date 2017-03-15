#!/usr/bin/env python3

import random
import sys
import math
import signal

from contextlib import ContextDecorator
from multiprocessing import Process, Lock, Array, set_start_method


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
        self.ip = Array('i', range(2))
        self._run = True

    def __call__(self):
        while self._run:
            x = random.random()
            y = random.random()
            with self.ip.get_lock():
                self.ip[0] += 1
                if in_circle(x, y):
                    self.ip[1] += 1

    def stop(self):
        """stop the worker"""
        self._run = False

    def print_results(self):
        with self.ip.get_lock():
            print
            print("iterations, hits: ", self.ip[0], self.ip[1])
            print(4 * self.ip[1] / self.ip[0])



if __name__ == '__main__':
    sim = Simulator()
    processes = []

    def worker_start():
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        signal.signal(signal.SIGQUIT, lambda *args: sim.stop())
        sim()

    def handle_int(*args):
        sim.print_results()

    def handle_quit(*args):
        # wait for workers to exit
        for p in processes:
            p.join()
        sim.print_results()

    max_workers = 1

    for i in range(max_workers):
        p = Process(target=worker_start)
        processes.append(p)
        p.start()

    signal.signal(signal.SIGINT, handle_int)
    signal.signal(signal.SIGQUIT, handle_quit)
