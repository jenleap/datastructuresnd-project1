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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def find_area_codes(call_list):
  area_codes = set()

  for line in call_list:
    if line[0][:5] == '(080)':
      area_codes.add(get_area_code(line[1]))

  area_codes_list = list(area_codes)
  area_codes_list.sort()
  return area_codes_list

def get_area_code(number):
  if number[:3] == '140':
    return '140'
  elif number.startswith('('):
    return number.split(')')[0] + ')'
  else: 
    return number.split(' ')[0][:4]

def calculate_percent_local_calls(call_list):
  total_calls = 0
  local_calls = 0 

  for line in call_list:
    if line[0][:5] == '(080)':
      total_calls += 1
      if line[1][:5] == '(080)':
        local_calls += 1

  return (local_calls / total_calls) * 100

#Part A
codes_called = find_area_codes(calls)
print("The numbers called by people in Bangalore have codes:")
for code in codes_called:
  print(code)

#Part B
percent_local_calls = calculate_percent_local_calls(calls)
print(f"{round(percent_local_calls, 2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")