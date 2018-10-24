# -*- coding: utf-8 -*-

import time
from tictoc import Timer


with Timer('NAME') as timer:
    print('Scope: ' + timer.name)
    print('...')
    time.sleep(1)

# > NAME ...
# Scope: NAME
# ...
# < NAME [WALL: 1.0034] [CPU: 0.0001]

timer = Timer('NAME')
timer.tic()  # or .start()
print('Scope: ' + timer.name)
print('...')
time.sleep(1)
timer.toc()  # or .end()

# > #647 ...
# Scope: #647
# ...
# < #647 [WALL: 1.0021] [CPU: 0.0001]
