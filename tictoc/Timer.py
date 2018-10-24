# -*- coding: utf-8 -*-

import time
import random

from typing import Callable
from typing import Any


class Timer(object):

    def __init__(self, name: str = None,
                 format_start: str = '> {name} ...',
                 format_end: str = '< {name} [WALL: {time_wall:.4f}] [CPU: {time_cpu:.4f}]',
                 to: Callable[[Any], None] = lambda msg: print(msg)):

        if not name:
            name = '#' + str(int(1000 * abs(random.random() - 0.001))).zfill(3)
        self.name: str = name

        self.format_start: str = format_start
        self.format_end: str = format_end
        self.time_wall: float = 0
        self.time_cpu: float = 0
        self._output_fn: Callable[[Any], None] = to

    def start(self) -> 'Timer':
        msg = self.format_start.format(**self.__dict__)
        self._output_fn(msg)
        self.time_wall = time.perf_counter()
        self.time_cpu = time.process_time()
        return self

    def end(self):
        msg = self.format_end.format(**{
            'name': self.name,
            'time_wall': time.perf_counter() - self.time_wall,
            'time_cpu': time.process_time() - self.time_cpu
        })
        self._output_fn(msg)

    def tic(self) -> 'Timer':
        return self.start()

    def toc(self):
        self.end()

    def __enter__(self) -> 'Timer':
        return self.start()

    def __exit__(self, type, value, traceback):
        self.end()
