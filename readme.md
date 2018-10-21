# tic-toc

Measure and track the wall and CPU time of defined scopes in Python.

## Usage

The following examples demonstrate the most simple usage: 

Here you see the implicit variant with the `with` construct:

```python
with Timer('NAME') as timer:
    print('Scope: ' + timer.name)
    print('...')
    time.sleep(1)
```

Here you see the explicit variant without the `with` construct:

```python
timer = Timer('NAME')
timer.tic()  # or timer.start()
print('Scope: ' + timer.name)
print('...')
time.sleep(1)
timer.toc()  # or timer.end()
```

The output is the same:

```python
# > NAME ...
# Scope: NAME
# ...
# < NAME [WALL: 1.0034] [CPU: 0.0001]
```

You can find more extended examples (e.g. with `logging`, `tqdm` or `pandas`) in the [examples](examples) directory.


## Sources

- [Answer](https://stackoverflow.com/a/5849861/1293700) by Eli Bendersky to the question '[tic, toc functions analog in Python](https://stackoverflow.com/questions/5849800/tic-toc-functions-analog-in-python)'
- [Python Clocks Explained](https://www.webucator.com/blog/2015/08/python-clocks-explained/) by Nat Dunn
- [Python 3.7 perf_counter() nanoseconds](https://vstinner.github.io/python37-perf-counter-nanoseconds.html) by Victor Stinner
- [PEP 564: New Time Functions With Nanosecond Resolution](https://docs.python.org/3.7/whatsnew/3.7.html#pep-564-new-time-functions-with-nanosecond-resolution)
- [PEP 560: Core Support for typing module and Generic Types](https://docs.python.org/3.7/whatsnew/3.7.html#pep-560-core-support-for-typing-module-and-generic-types)
- [Slow and fast methods for generating random integers in Python](https://eli.thegreenplace.net/2018/slow-and-fast-methods-for-generating-random-integers-in-python/) by  Eli Bendersky


## License

The module is Open Source Software released under the [MIT](license.txt) license.
