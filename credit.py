from math import floor
from sys import exit
import re

# Get credit card number from user
card_no = input("Number: ")

# Initialise sum variable to zero
sum = 0

# Calculate checksum
# Multiply every other digit by 2, starting from second-to-last, and add digits to sum
for i in range(len(card_no) - 2, -1, -2):
    result = int(card_no[i]) * 2
    if (result < 10):
        sum += result
    # If the multipled number is great 10 or greater, then add the two digits together
    else:
        sum += floor(result / 10) + result % 10

# Sum up the digits of every other digit starting from the end
for i in range(len(card_no) - 1, -1, -2):
    sum += int(card_no[i])

# Check if the sum modulo 10 is congruent to 0
if sum % 10 != 0:
    print("INVALID")
    exit()

# Validate if AMEX
if len(card_no) == 15:
    if card_no[0] == "3" and re.search("4|7", card_no[1]):
        print("AMEX")
        exit()
    else:
        print("INVALID")
        exit()

# Validate if MasterCard or 16-digit VISA
if len(card_no) == 16:
    if card_no[0] == "4":
        print("VISA")
        exit()
    elif card_no[0] == "5" and re.search("1|2|3|4|5", card_no[1]):
        print("MASTERCARD")
        exit()
    else:
        print("INVALID")
        exit()

# Validate if 13-digit VISA
if len(card_no) == 13 and card_no[0] == "4":
    print("VISA")
    exit()
else:
    print("INVALID")
    exit()
