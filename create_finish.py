import os
import time

file_name = "output/sim1"
file_size = 1024*1024

time.sleep(20)

with open(file_name, 'wb') as fout:
    fout.write(os.urandom(file_size))
