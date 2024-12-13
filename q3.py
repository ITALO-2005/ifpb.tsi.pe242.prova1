d = int(input("Divisores: "))
soma = 0

for divisor in range(1, d + 1):
    if d % divisor == 0 and divisor % 3 == 0:
        soma+=1
    elif soma > 0:
        print(soma)
    else:
        print("O numero não possui divisores multiplos de 3")