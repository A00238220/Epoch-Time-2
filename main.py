#importing modules
import time
import json
# import random

###############
#Question a
###################

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

#dumping dictionary data in json
with open('data.json', 'w') as outfile:
  json.dump(data, outfile)

#setting conditional statement for time validation 
if time in lines:
  pass
else:
  filename = 'time.txt'
  with open(filename, 'w') as file_object2:
    file_object2.write(f"{start_time}")

#checking content of file
filename = "time.txt"
with open(filename, 'r') as file_object:
  lines = file_object.readlines()

##############
#Question B
###############
#converting time data type from string to float
previous_time = float(lines[0])

#calculating elapsed seconds since file creation
elapsed_time = time.time() - previous_time

#printing elapsed time to terminal
print(f"{elapsed_time} secs has elapsed since file creation")

###############
#Question C
#################
print()

# investment = 0
#setting interest rate per annum
interest = 0.023

#calculating accumulations for different periods
accumulation_per_sec = interest * elapsed_time
accumulation_per_min = accumulation_per_sec * 60
accumulation_per_hour = accumulation_per_min * 60
accumulation_per_day = accumulation_per_hour * 24
accumulation_per_week = accumulation_per_day * 7
accumulation_per_month = accumulation_per_week * 4
accumulation_per_year = accumulation_per_month * 12

#printing accumulated interest to terminal
print(f"The accumulated interest per second is {accumulation_per_sec}\nThe accumulated interest per minute is {accumulation_per_min}\nThe accumulated interest per hour is {accumulation_per_hour}\nThe accumulated interest per day is {accumulation_per_day}\nThe accumulated interest per week is {accumulation_per_week}\nThe accumulated interest per month is {accumulation_per_month}\nThe accumulated interest per year is {accumulation_per_year}")

###############
#Question D
#################
print()

#setting while loop
while True:
  print(f"The accumulated interest per second is {accumulation_per_sec}")
  time.sleep(2)
  print(f"The accumulated interest per minute is {accumulation_per_min}")
  time.sleep(2)
  print(f"The accumulated interest per hour is {accumulation_per_hour}")
  time.sleep(2)
  print(f"The accumulated interest per day is {accumulation_per_day}")
  time.sleep(2)
  print(f"The accumulated interest per week is {accumulation_per_week}")
  time.sleep(2)
  print(f"The accumulated interest per month is {accumulation_per_month}")
  time.sleep(2)
  print(f"The accumulated interest per year is {accumulation_per_year}")
  time.sleep(2)

  break

###############
#Question E
#################
print()

#setting starting amount and current amount
starting_amount = 1000000

#calculating accumulations for different periods
accumulation_per_sec = starting_amount + (interest * elapsed_time)
accumulation_per_min = accumulation_per_sec * 60
accumulation_per_hour = accumulation_per_min * 60
accumulation_per_day = accumulation_per_hour * 24
accumulation_per_week = accumulation_per_day * 7
accumulation_per_month = accumulation_per_week * 4
accumulation_per_year = accumulation_per_month * 12

while True:
  print(f"The starting amount is ${starting_amount}")
  time.sleep(2)
  print(f"The current amount plus interest per second is {accumulation_per_sec}")
  time.sleep(2)
  print(f"The current amount plus interest per minute is {accumulation_per_min}")
  time.sleep(2)
  print(f"The current amount plus interest per hour is {accumulation_per_hour}")
  time.sleep(2)
  print(f"The current amount plus interest per day is {accumulation_per_day}")
  time.sleep(2)
  print(f"The current amount plus interest per week is {accumulation_per_week}")
  time.sleep(2)
  print(f"The current amount plus interest per month is {accumulation_per_month}")
  time.sleep(2)
  print(f"The current amount plus interest per year is {accumulation_per_year}")
  time.sleep(2)

  break
