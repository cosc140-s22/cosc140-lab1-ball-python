#
# Name: Kyle Shaw
# Collaborator(s): None
#
second = input("How many seconds? ")
day = int(second)//86400
second = int(second)%86400
hour = int(second)//3600
second = int(second)%3600
minute = int(second)//60
second = int(second)%60
print(f"{second} seconds is equivalent to {day} days, {hour} hours, {minute} minutes, and {second} seconds")
