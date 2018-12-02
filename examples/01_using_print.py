# -*- coding: utf-8 -*-

import time
from tic_toc import Timer


with Timer('NAME') as timer:
    print('Scope: ' + timer.name)
    print('...')
    time.sleep(1)

# > NAME ...
# Scope: NAME
# ...
# < NAME [WALL: 1.0034s] [CPU: 0.0001s]

timer = Timer('NAME')
timer.tic()  # or .start()
print('Scope: ' + timer.name)
print('...')
time.sleep(1)
timer.toc()  # or .end()

# > #647 ...
# Scope: #647
# ...
# < #647 [WALL: 1.0021s] [CPU: 0.0001s]
