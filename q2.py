romano_valores = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

s = input().strip()  
total = 0
valor_anterior = 0

for roman in reversed(s):
    valor = romano_valores[roman]
    if valor < valor_anterior: 
        total -= valor
    else:  
        total += valor
    valor_anterior = valor 

print(total)