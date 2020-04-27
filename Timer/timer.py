#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 06 16:15:42 2020

@author: AkashTyagi
"""

import sys
import time
import datetime as dt


def play_sound():
    import os
    duration = 1  # seconds
    freq = 330  # Hz
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))


input_time = sys.argv[1]
print("Timer Note: ",end='')
note = input()
time_array = [int(t) for t in input_time.split(":")]

total_sec = 00
input_hours = 00
input_minutes = 00
input_seconds = 00
for i in range(len(time_array)-1, -1, -1):
    if i == len(time_array)-1:
        # Seconds
        if time_array[i]>59:
            mins = time_array[i]//60
            input_seconds = input_seconds - mins*60
            if mins>59:
                hours = mins//60
                mins = mins - hours*60
                input_hours += hours
            input_minutes += mins
        total_sec += time_array[i]
        input_seconds += time_array[i]

    elif i == len(time_array)-2:
        # Minutes
        if time_array[i]>59:
            hours = time_array[i]//60
            input_minutes = input_minutes - hours*60
            input_hours += hours        
        total_sec += time_array[i]*60
        input_minutes += time_array[i]
    elif i == len(time_array)-3:
        # Hours
        total_sec += time_array[i]*60*60
        input_hours += time_array[i]

print("\n")
print("="*40)
print(
    f"Timer set for: {input_hours}H:{input_minutes}M:{input_seconds}S")
if len(note)>0:
    print("Note: ",note)

total_hours = 00
total_minutes = 00
total_seconds = 00

current_time = 0
g = 99
start_time = dt.datetime.today()

while current_time < total_sec:
    time.sleep(0.1)
    # print(total_hours,total_minutes,total_seconds)
    curr_diff = round(dt.datetime.today().timestamp() - start_time.timestamp(), 0)
    if curr_diff != g:
        g = curr_diff
        if total_seconds < 59:
            total_seconds += 1
        elif total_minutes < 59:
            total_seconds = 0
            total_minutes += 1
        else:
            total_seconds = 0
            total_minutes = 0
            total_hours += 1
        print(f" Time: {total_hours}:{total_minutes}:{total_seconds}", end="\r")
        current_time += 1

print("="*40)
print("Timer Finished !!!")

print("\nDetails")
print("-------")
print(f"Started At: {start_time.hour}:{start_time.minute}")
print(f"Finished At: {dt.datetime.today().hour}:{dt.datetime.today().minute}")
print(f"Total Time spent:  {input_hours}H:{input_minutes}M:{input_seconds}S")
play_sound()


# import time
# import datetime as dt
# s = dt.datetime.today().timestamp()
# d = 99
# for x in range(600):
#     time.sleep(0.1)
#     z = round(dt.datetime.today().timestamp() - s,0)
#     # print(z)
#     if  z != d:
#         d = z
#         print(f'THis is {d}',end='\r')
