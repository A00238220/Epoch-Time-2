#importing modules
import time
import json
# import random

# investment = 0
#setting start time
start_time = time.time()

#opening file in read mode
filename = "time.txt"
with open(filename, 'r') as file_object:
  lines = file_object.readlines()

#setting empty dictionary
data = {}
#appending start time to dictionary
data["time"] = start_time


with open('data.json', 'w') as outfile:
  json.dump(data, outfile)

if time in lines:
  pass
else:
  filename = 'time.txt'
  with open(filename, 'w') as file_object2:
    file_object2.write(f"{start_time}")

filename = "time.txt"
with open(filename, 'r') as file_object:
  lines = file_object.readlines()
  previous_time = float(lines[0])
  # print(type(previous_time), type(time.time()))
  
elapsed_time = time.time() - previous_time
print(f"{elapsed_time} secs has elapsed since file creation")