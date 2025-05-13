'''Elabore um programa que leia um valor de entrada e mostre para cada valor até ao 1 (se é número Primo, Quantos divisores e números perfeitos) 
o Programa deve validar entradas entre 1 e 30.000, e parar de 10 em 10 valores com instrução para parar ou continuar. 
No mesmo programa use um menu e Elabore uma calculadora simples (+,-,*,/) com a função extra tabuada. 
Validar entradas de 1 a 1000 (nota a tabuada deve apresentar todas as multiplicações de 1 ate ao máximo introduzido) deve parar de 20 em 20 valores.'''


def primo(num):
    if num < 2:
        return False
    return all(num % i != 0 for i in range(2, int(num**0.5) + 1))

def divisores(num):
    return len([i for i in range(1, num + 1) if num % i == 0])

def perfeito(num):
    return sum(i for i in range(1, num) if num % i == 0) == num

def analisar():
    while True:
        try:
            n = int(input("Digite um número (1 a 30000): "))
            if 1 <= n <= 30000:
                break
            print("Valor inválido!")
        except ValueError:
            print("Digite um número inteiro!")

    for num in range(n, 0, -1):
        print(f"N: {num}, Primo: {primo(num)}, Divisores: {divisores(num)}, Perfeito: {perfeito(num)}")
        if num % 10 == 0 and input("Continuar? (s/n): ").lower() != 's':
            break

def calculadora():
    while True:
        print("\n1 - Soma | 2 - Sub | 3 - Mult | 4 - Div | 5 - Tabuada | 6 - Sair")
        opcao = input("Escolha: ")
        if opcao == "6":
            break
        if opcao == "5":
            tabuada()
            continue

        try:
            n1, n2 = map(int, input("Digite dois números (1 a 1000): ").split())
            if not (1 <= n1 <= 1000 and 1 <= n2 <= 1000):
                print("Valores inválidos!")
                continue
        except ValueError:
            print("Entrada inválida!")
            continue

        ops = {"1": n1 + n2, "2": n1 - n2, "3": n1 * n2, "4": n1 / n2 if n2 != 0 else "Erro!"}
        print(f"Resultado: {ops.get(opcao, 'Opção inválida!')}")

def tabuada():
    while True:
        try:
            num = int(input("Digite um número (1 a 1000): "))
            if 1 <= num <= 1000:
                break
            print("Valor inválido!")
        except ValueError:
            print("Digite um número inteiro!")

    for i in range(1, num + 1):
        print(f"{num} x {i} = {num * i}")
        if i % 20 == 0 and input("Continuar? (s/n): ").lower() != 's':
            break

def menu():
    while True:
        print("\n1 - Analisar | 2 - Calculadora | 3 - Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            analisar()
        elif opcao == "2":
            calculadora()
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")

menu()
