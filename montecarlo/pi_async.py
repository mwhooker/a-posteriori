#!/usr/bin/env python3

import random
import sys
import math
import concurrent.futures
import signal

import multiprocessing as mp

def in_circle(x, y):
    return math.sqrt(x**2 + y**2) <= 1

class Simulator(object):
    def __init__(self, runs):
        self.runs = runs

    def __call__(self):
        signal.signal(signal.SIGQUIT, signal.SIG_IGN)
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        hits = 0
        for _ in range(self.runs):
            x = random.random()
            y = random.random()
            if in_circle(x, y):
                hits += 1
        return hits


class Results(object):
    def __init__(self, run_step):
        self.run_step = run_step
        self.runs = 0
        self.hits = 0

    def future_cb(self, future):
        self.runs += self.run_step
        self.hits += future.result()

    def print_results(self):
        if self.runs == 0:
            print("still waiting for results to come in")
            return
        print
        print("iterations, hits: ", self.runs, self.hits)
        print(4 * self.hits / self.runs)

def main():
    runs = 1000000
    results = Results(runs)
    running = True

    def handle_quit():
        results.print_results()
        running = False
        sys.exit(0)

    signal.signal(signal.SIGQUIT, lambda *args: handle_quit())

    semaphore = mp.BoundedSemaphore(mp.cpu_count())

    def done(future):
        results.future_cb(future)
        semaphore.release()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        while running:
            try:
                semaphore.acquire()
            except KeyboardInterrupt:
                results.print_results()
                continue
            future = executor.submit(Simulator(runs))
            future.add_done_callback(done)

if __name__ == '__main__':
    main()
