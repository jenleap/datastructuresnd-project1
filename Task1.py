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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def count_phone_numbers(records):
    number_count = set()

    for line in records:
        number_count.add(line[0])
        number_count.add(line[1])

    return len(number_count)

texts.extend(calls)
unique_phone_nums = count_phone_numbers(texts)
print(f"There are {unique_phone_nums} different telephone numbers in the records.")

