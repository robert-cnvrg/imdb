import time
import random

key = "epoch 1"
while(True):
    val = random.randint(0,9)    
    print(f"cnvrg_linechart_Option1 value: {val}")
    
    print(f"cnvrg_linechart_Option2 key: {key} value: {val}")

    print(f"cnvrg_linechart_Option3 group: '1' value: {val}")
    print(f"cnvrg_linechart_Option3 x: 'TX' y: 'TY' group: '2' value: {val + 1}")
    
    print(f"cnvrg_linechart_Option4 group: '1' key: '{key}' value: {val}")
    print(f"cnvrg_linechart_Option4 group: '2' key: '{key}' value: {val + 1}")
    
    time.sleep(10)
