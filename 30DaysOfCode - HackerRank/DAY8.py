"""
Task
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for. 
For each  queried, 
print the associated entry from your phone book on a new line in the form name=phoneNumber; 
if an entry for  is not found, print Not found instead.
"""
N = int(input())
data = [input().strip().split() for i in range(N)]
phoneBook = dict(data)
while True:
    try:
        name = input()
        if name in phoneBook:
            print("%s=%s" % (name, phoneBook[name]))
        else:
            print("Not found")
    except:
        break