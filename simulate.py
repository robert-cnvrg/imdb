import os
import time

file_prefix = "output/sim"
file_index = 1

file_size = 1024*1024*1024

while(True):
  file_name = file_prefix + str(file_index)
  with open(file_name, 'wb') as fout:
    fout.write(os.urandom(file_size))
    
  print("Wrote file: " + file_name)
  time.sleep(60*10)
  
