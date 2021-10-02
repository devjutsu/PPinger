import os
import time
hostname = "192.168.1.109" #example

while(True):
  f = open("/home/garuda/results.txt", "a")
  response = os.system("ping -c 1 " + hostname)

  if response == 0:
    f.write(time.ctime() + ' ___ UP!\n')
  else:
    f.write(time.ctime() + ' ___ \n')
  f.close()
  time.sleep(300);