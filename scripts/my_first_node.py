#!/usr/bin/env python3

from datetime import datetime
from time import sleep

delay = 5

while(True):
    print(f'Сейчас время: {datetime.now().strftime("%H:%M:%S")}')
    
    sleep(delay)