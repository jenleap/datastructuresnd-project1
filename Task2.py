"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

from collections import defaultdict

def calculate_longest_call(call_list):
    call_dict = defaultdict(int)

    for line in call_list:
        if line[2][3:10] == '09-2016':
            for i in range(2):
                call_dict[line[i]] += int(line[3])
        
    longest_call = max(call_dict.values())

    for key, value in call_dict.items():
        if value == longest_call:
            print(f"{key} spent the longest time, {value} seconds, on the phone during September 2016.")

calculate_longest_call(calls)





