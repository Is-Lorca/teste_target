'''
3) Dado um vetor que guarda o valor de faturamento diário 
de uma distribuidora, faça um programa, na linguagem que 
desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento 
diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. 
Estes dias devem ser ignorados no cálculo da média;

'''

import json
import os

file_path = os.path.join(os.path.dirname(__file__), 'dados.json')
with open(file_path, 'r') as file:
    data = json.load(file)

faturamento_valido = [dia['valor'] for dia in data if dia['valor'] > 0]

menor_valor = min(faturamento_valido)
maior_valor = max(faturamento_valido)

media_mensal = sum(faturamento_valido) / len(faturamento_valido)

dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

print(f'Menor Valor de Faturamento: {menor_valor:.2f}, Maior Valor de Faturamento: {maior_valor:.2f}, ' 
      f'Dias acima da média: {dias_acima_da_media}')

#Resposta: Menor Valor de Faturamento: 373.78, Maior Valor de Faturamento: 48924.24, 
#Dias acima da média: 10