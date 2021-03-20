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

def calculate_longest_call(call_list):
    call_dict = dict()

    for line in call_list:
        for i in range(2):
            if call_dict.get(line[i]):
                call_dict[line[i]] += int(line[3])
            else:
                call_dict[line[i]] = int(line[3])
        
    longest_call = max(call_dict.values())

    for key, value in call_dict.items():
        if value == longest_call:
            print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(key, value))

calculate_longest_call(calls)





