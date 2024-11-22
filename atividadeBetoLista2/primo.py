from os import system

def showPrime():
    verification = 0
    while verification == 0:
            try:
                n1 = int(input("Digite o primeiro número da sequencia: "))
                n2 = int(input("Digite o ultimo numero da sequencia: "))
            except:
                system('cls')
                print('erro, digite uma numero valido')
                continue
            else:
                def primeNumbers(n1, n2):
                            def prime(n):
                                if n < 2:
                                    return False
                                for i in range(2, int(n**0.5) + 1):
                                    if n % i == 0:
                                        return False
                                return True
                            
                            primos = [num for num in range(n1, n2 + 1) if prime(num)]
                            return primos
                verification +=1
            return print(f"Numeros primos no intervalo de {n1} a {n2}: {primeNumbers(n1, n2)}") 

showPrime()