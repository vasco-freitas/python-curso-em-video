def vote():
    """_summary_
Calcula a idade com base no ano de nascimento 
e retorna o status de obrigatoriedade de voto.
    """
    from datetime import date
    year = int(input('What year were you borne? ')) 
    current_year = date.today().year - year
    if current_year < 18:
        state = "Don't vote!"
    elif current_year > 64:
        state = "Optional voting!"    
    else:
        state = "Mandatory voting!"
    
    
    print(f'With {current_year} years: {state}')
    return f'With {current_year} years: {state}'
print(vote())
help(vote)

