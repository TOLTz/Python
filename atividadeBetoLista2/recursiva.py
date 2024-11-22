

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

validation = True

while validation:
    try:
        n = int(input("Digite um numero: "))
    except:
        print("Erro, digite um numero inteiro.")
    else:
        print(f"O fatorial de {n} e {fatorial(n)}")
        validation = False

fatorial()