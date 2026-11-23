name = str(input("Enter your full name: ")).strip().title()
dividido = name.split()
print(f'You are very welcome, Sir.{dividido[0]} {dividido[-1]}.')
print(f'Yor first name is {dividido[0]} and your last name is {dividido[-1]}.')