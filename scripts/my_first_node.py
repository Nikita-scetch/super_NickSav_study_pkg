#!/usr/bin/env python3

from datetime import datetime
from time import sleep

delay = 5

while(True):
    current_time = datetime.now().time()
    print(f'Сейчас время: {current_time.hour}:{current_time.minute}:{current_time.second}')

    sleep(delay)