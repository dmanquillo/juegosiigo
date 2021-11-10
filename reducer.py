import sys

salesTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", salesTotal)
        salesTotal = 0
    
    oldKey = thisKey
    salesTotal += float(thisSale)

if not oldKey:
    print(oldKey, "\t", salesTotal)
