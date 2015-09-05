import csv
import operator
from collections import defaultdict

def make_address(address):
    parts = address.split()
    if parts:
        parts[0] = parts[0][:1] + (len(parts[0][1:]) * "*")
    return " ".join(parts)

f = open('potholes.csv')

#potholes_by_address = defaultdict()
potholes_by_address = {}
d = csv.DictReader(f)
for row in d:
    street_address = row['STREET ADDRESS']
    street_address = make_address(street_address)
    potholes_by_address[street_address] = potholes_by_address.get(street_address, 0) + 1
f.close()
sorted_potholes_by_address = sorted(potholes_by_address.items(), key=operator.itemgetter(1), reverse=True)
print sorted_potholes_by_address[0][0], "***", sorted_potholes_by_address[0][1]