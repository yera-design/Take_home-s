#!/usr/bin/env python3
import re

file = open(r"C:\Users\STS LTD\messages.xml", "r", encoding="utf-8")

total_transferred = 0
total_received = 0
total_paid = 0
total_payments = 0

for line in file:
    if "body=" in line:
        match = re.search(r"([\d]+(,[\d]+)?) RWF transferred", line)
        matching = re.search(r"received ([\d]+(,[\d]+)?) RWF", line)
        matched = re.search(r"payment of ([\d]+(,[\d]+)?) RWF", line)
        if match:
            total_transferred = total_transferred + int(match.group(1).replace(",", ""))
        if matching:
            total_received = total_received + int(matching.group(1).replace(",", ""))
        if matched:
            total_paid = total_paid + int(matched.group(1).replace(",", ""))
            
        total_payments = total_paid + total_transferred

print("Total transferred:", total_transferred)
print("Total received:", total_received)
print("Total paid:", total_paid)
print("Total payments:", total_payments)

file.close()
