def q1():
    numero = input('').strip()
    if numero.startswith('-') or not numero.isdigit():
        print("False")
        return
    numero = numero.lstrip('')
    if not numero:
        print("True")
        return
    print("True" if numero == numero[::-1] else "False")


def q2():
    romano_valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    s = input('_').strip() 
    total = 0
    valor_anterior = 0

    for romano in reversed(s):
        valor = romano_valores[romano]
        if valor < valor_anterior:
            total -= valor
        else:
            total += valor
        valor_anterior = valor 

    print(total)


def q3():
    d = int(input("Divisores: "))
    soma = 0
    
    for divisor in range(1, d + 1):
        if d % divisor == 0 and divisor % 3 == 0:
            soma+=1
        if soma > 0:
            print(soma)
        else:
            print('O número não possui divisores multiplos de 3')
        
        
def q4():       
    numero_1 = int(input("Digite o primeiro numero:"))
    numero_2 = int(input("Digite o segundo numero:"))

    soma = 0
    numero = 0

    if soma > 0:
        soma + numero
    