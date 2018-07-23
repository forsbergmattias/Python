import time
import datetime

t = datetime.datetime.now().timestamp()
time.sleep(0)
print(t-datetime.datetime.now().timestamp())
