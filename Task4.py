"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def check_telemarketer(call_list, text_list):
    call_senders = list()
    call_receivers = list()
    text_senders = list()
    text_receivers = list()
    possible_telemarketers = set()

    for line in call_list:
        call_senders.append(line[0])
        call_receivers.append(line[1])

    for tline in text_list:
        text_senders.append(tline[0])
        text_receivers.append(tline[1])

    for sender in call_senders:
        if sender not in call_receivers and sender not in text_senders and sender not in text_receivers:
            possible_telemarketers.add(sender)

    possible_telemarketers_list = list(possible_telemarketers)
    possible_telemarketers_list.sort()
    return possible_telemarketers_list

suspected_telemarketers = check_telemarketer(calls, texts)
print("These numbers could be telemarketers: ")
for num in suspected_telemarketers:
  print(num)