# -*- coding: utf-8 -*-

import time
import logging

from tqdm import tqdm
from tictoc import Timer


logging.basicConfig(format='[%(asctime)s:%(msecs)04d] - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
log = logging.getLogger('asyncio')

with Timer('NAME', to=log.info) as timer:
    for i in tqdm(range(1000), desc=timer.name):
        time.sleep(.01)

# [2018-10-21 14:31:01:0871] - asyncio - INFO - > NAME ...
# NAME: 100%|██████████| 1000/1000 [00:11<00:00, 87.07it/s]
# [2018-10-21 14:31:13:0359] - asyncio - INFO - < NAME [WALL: 11.4881] [CPU: 0.0943]
