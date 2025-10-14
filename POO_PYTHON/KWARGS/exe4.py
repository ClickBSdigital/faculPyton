def calculate_tax(value, **kwargs):
    total = 0
    print("Parâmetros recebidos:", kwargs)  # mostra o dicionário completo
    
    # Verifica se o parâmetro 'iss' foi passado
    if 'iss' in kwargs:
        total += value * kwargs['iss']  # calcula ISS
    
    # Verifica se o parâmetro 'pis' foi passado
    if 'pis' in kwargs:
        total += value * kwargs['pis']  # calcula PIS
    
    return total
