def fibonacci():
    n = int(input("Digite um numero para gerar os n primeiros números da sequência de Fibonacci: "))
    
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return print(f"Os {n} primeiros números da sequência de Fibonacci são: {fib_sequence}")

fibonacci()
