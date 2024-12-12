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








    

