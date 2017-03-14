#/usr/bin/env python3
import random
import sys
import itertools
import math
import signal
import functools


def in_circle(x, y):
    return math.sqrt(x**2 + y**2) <= 1

def signal_handler(signal, frame, f):
    f()
    sys.exit(0)


if __name__ == '__main__':
    inside = npoints = 0

    def print_results(exit):
        print
        print("iterations: ", npoints)
        print(4 * inside / npoints)
        if exit:
            sys.exit(0)

    signal.signal(signal.SIGINT, lambda *args: print_results(False))
    signal.signal(signal.SIGQUIT, lambda *args: print_results(True))

    for i in itertools.count(1):
        x = random.random()
        y = random.random()
        npoints = i
        if in_circle(x, y):
            inside += 1
