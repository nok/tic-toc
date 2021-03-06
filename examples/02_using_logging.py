# -*- coding: utf-8 -*-

import time
import logging

from tic_toc import Timer


log_fmt = '[%(asctime)s:%(msecs)04d] - %(name)s - %(levelname)s - %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(format=log_fmt, datefmt=datefmt, level=logging.INFO)
log = logging.getLogger('asyncio')

with Timer('NAME', to=log.info) as timer:
    log.info('Scope: ' + timer.name)
    log.info('...')
    time.sleep(1)

# [2018-10-21 14:30:31:0332] - asyncio - INFO - > NAME ...
# [2018-10-21 14:30:31:0333] - asyncio - INFO - Scope: NAME
# [2018-10-21 14:30:31:0333] - asyncio - INFO - ...
# [2018-10-21 14:30:32:0337] - asyncio - INFO - < NAME [WALL: 1.0042s] [CPU: 0.0003s]
