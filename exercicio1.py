def calculate_Fibonacci(numero):
    a = 0
    b = 1
    while a < numero:
        a, b = b, a + b
    return a == numero

numero = int(input("Digite um número: "))

print(f"O número {numero} {'está' if calculate_Fibonacci(numero) else 'não está'} na sequência Fibonacci")