'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP = R$67.836,43
• RJ = R$36.678,66
• MG = R$29.229,88
• ES = R$27.165,48
• Outros = R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que 
cada estado teve dentro do valor total mensal da distribuidora. 
'''


faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_estados.values())

percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estados.items()}

#Preferi formatar os percentuais para melhor observação
percentuais_formatados = {estado: f"{valor:.2f}%" for estado, valor in percentuais.items()}

print(f'Faturamento total mensal: {faturamento_total}, seu percentual de representação por '
       f'estado foi de: {percentuais_formatados}')

#Resposta: 
#Faturamento total: 180759.98
#Percentuais: 
"""
{
    'SP': 37.53%,
    'RJ': 20.29%,
    'MG': 16.17%,
    'ES': 15.03%,
    'Outros': 10.98%
}
"""