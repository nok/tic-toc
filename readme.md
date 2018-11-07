# tic-toc

[![PyPI](https://img.shields.io/pypi/v/tic-toc.svg)](https://pypi.python.org/pypi/tic-toc)
[![PyPI](https://img.shields.io/pypi/pyversions/tic-toc.svg)](https://pypi.python.org/pypi/tic-toc)
[![GitHub license](https://img.shields.io/pypi/l/tic-toc.svg)](https://raw.githubusercontent.com/nok/tic-toc/master/license.txt)

Measure and track the wall and CPU time of defined scopes in Python.<br>It's suitable for long-running applications which should be monitored.


## Installation

```bash
$ pip install tic-toc
```


## Usage

The following examples demonstrate the most simple usage: 

Here you see the implicit variant with the `with` construct:

```python
from tictoc import Timer

with Timer('NAME') as timer:
    print('Scope: ' + timer.name)
    time.sleep(1)
```

Here you see the explicit variant without the `with` construct:

```python
from tictoc import Timer

timer = Timer('NAME')
timer.tic()  # or .start()
print('Scope: ' + timer.name)
time.sleep(1)
timer.toc()  # or .end()
```

The outputs are similar to each other:

```python
# > NAME ...
# Scope: NAME
# < NAME [WALL: 1.0034s] [CPU: 0.0001s]
```

You can find more extended examples (e.g. with `logging`, `tqdm` or `pandas`) in the [examples](examples) directory.


## Parameters

```python
class Timer(object):
    def __init__(self, name: str = None,
                 format_start: str = '> {name} ...',
                 format_end: str = '< {name} [WALL: {time_wall:.4f}s] [CPU: {time_cpu:.4f}s]',
                 to: Callable[[Any], None] = lambda msg: print(msg)):
```

- `name`: str, optional, default: leading hash with four random digits, eg. `#0512`
- `format_start`: str, optional, default: `'> {name} ...'`
- `format_end`: str, optional, default: `'< {name} [WALL: {time_wall:.4f}s] [CPU: {time_cpu:.4f}s]'`
- `to`: `Callable[[Any], None]`, optional, default: `lambda msg: print(msg)`

You can change the visual string formats and the output method.


## Sources

- [Answer](https://stackoverflow.com/a/5849861/1293700) by Eli Bendersky to the question '[tic, toc functions analog in Python](https://stackoverflow.com/questions/5849800/tic-toc-functions-analog-in-python)'
- [Python Clocks Explained](https://www.webucator.com/blog/2015/08/python-clocks-explained/) by Nat Dunn
- [Python 3.7 perf_counter() nanoseconds](https://vstinner.github.io/python37-perf-counter-nanoseconds.html) by Victor Stinner
- [PEP 564: New Time Functions With Nanosecond Resolution](https://docs.python.org/3.7/whatsnew/3.7.html#pep-564-new-time-functions-with-nanosecond-resolution)
- [PEP 560: Core Support for typing module and Generic Types](https://docs.python.org/3.7/whatsnew/3.7.html#pep-560-core-support-for-typing-module-and-generic-types)
- [Slow and fast methods for generating random integers in Python](https://eli.thegreenplace.net/2018/slow-and-fast-methods-for-generating-random-integers-in-python/) by  Eli Bendersky


## License

The module is Open Source Software released under the [MIT](license.txt) license.
