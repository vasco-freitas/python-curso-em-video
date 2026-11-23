SUM = 0
NUMBER_TOTAL = 0

for c in range(1,501):
    if c % 2 == 1 and c % 3 == 0:
        SUM += c
        NUMBER_TOTAL += 1
print(f'The sum of all {NUMBER_TOTAL} requested values is {SUM}!')
        
    #print(c, end=" ")