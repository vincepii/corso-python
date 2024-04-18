from datetime import datetime
import time

while True:
    now = datetime.now()
    print(f'{now.hour}:{now.minute}:{now.second}')
    time.sleep(1)
