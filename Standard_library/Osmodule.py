import os 

curDir = os.getcwd()

print(curDir)

import time

time.sleep(5)

os.mkdir('newDir')
time.sleep(5)
os.rename("newDir", 'newDir2')
time.sleep(5)
os.rmdir("newDir2")

