salve = []

while True:
    data  = {'Name': input('Name: ').title().strip() ,
         'Average': (m := float(input('Average: '))) ,
         'Situation': 'Approved!' if m >= 7 else('Recovery!' if m >= 5 else 'Failed!')}
    salve.append(data)
    
    sn = input('Want to continued? ').title().strip()
    if sn == 'N':
        break
    
for n, aluno in enumerate(salve,start=1):
    print('===---=='*7)
    print(f'Student {n}!')
    for i, t in aluno.items():
        print(f'The {i} is {t}!')
    