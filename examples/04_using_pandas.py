# -*- coding: utf-8 -*-

import logging

import numpy as np
import pandas as pd
from tqdm import tqdm
from tictoc import Timer


logging.basicConfig(format='[%(asctime)s:%(msecs)04d] - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
log = logging.getLogger('asyncio')

with Timer('NAME', to=log.info) as timer:
    tqdm.pandas(desc=timer.name)
    df = pd.DataFrame(np.random.randn(50, 2), columns=list('AB'))
    def func(row):
        return row['A'] * row['B']
    df['C'] = df.progress_apply(func, axis=1)

# [2018-10-21 14:43:58:0262] - asyncio - INFO - > NAME ...
# NAME: 100%|██████████| 50/50 [00:00<00:00, 16524.72it/s]
# [2018-10-21 14:43:58:0269] - asyncio - INFO - < NAME [WALL: 0.0068] [CPU: 0.0106]
