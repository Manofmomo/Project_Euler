items = {'yo'}
for a in range(2,101):
    for b in range(2,101):
        items.add(a**b)

print(len(items))
