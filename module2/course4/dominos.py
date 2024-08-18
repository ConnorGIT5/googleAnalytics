# create dominos

domin = []
for left in range(7):
    for right in range(left, 7):
        domin.append((left, right))

print(domin)
print('\n\n')

pips_in_dominos = []
    
for domino in domin:
        pips_in_dominos.append(domino[0] + domino[1])

print(pips_in_dominos)
print('\n\n')

# using 'list comprehension' instead

pips_in_dominos2 = [domino[0] + domino[1] for domino in domin]
print(pips_in_dominos2)
