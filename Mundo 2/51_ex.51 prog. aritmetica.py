term = int(input("First term: "))
reason = int(input("Reason: "))
num = reason * 10

for PA in range (term, num, reason):
    print(PA, end=" -> ")
print("End")