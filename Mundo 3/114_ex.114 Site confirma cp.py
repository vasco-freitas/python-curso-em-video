import requests

try:
    site = requests.get('https://www.cp.pt', timeout=10)
    #site = requests.get('https://www.pudim.com.br', timeout=10)
    tempo = site.elapsed.total_seconds()
    site.raise_for_status()
    print(f'Site found. Code: {site.status_code}  Time: {tempo:.2f} seconds')
    #print(f'Code: {site.text}')
except requests.RequestException as erro:
    print("Classe:", type(erro).__name__)
    print(f'Site not found. {erro} :(')

