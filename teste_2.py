'''Elabore uma base de dados de clientes de uma fábrica de materiais. O programa deverá possibilitar inserção e listagem dos clientes bem como as 
compras por eles efetuadas( Númcli(Automático), NomCli, morada, tel, nif, compra, Divfin ). Divida final=compra – desconto, valor do desconto se 
compra for entre 100 e 200 é 5%, se for superior a 200 e inferior a 500 é 10% se superior a 500 é 15%. O programa deve validar todas as entradas e na 
listagem deve parar cliente a cliente e ser possível busca direta por número de cliente. 5v. 
O programa deve conter (Estruturas 3v, funções .5v, Vetores .4v, apontadores .3v). 2 H '''

def eh_primo(numero):
    if numero < 2:
        return False
    return all(numero % divisor != 0 for divisor in range(2, int(numero**0.5) + 1))

def contar_divisores(numero):
    return len([divisor for divisor in range(1, numero + 1) if numero % divisor == 0])

def eh_perfeito(numero):
    return sum(divisor for divisor in range(1, numero) if numero % divisor == 0) == numero

def analisar_numeros():
    while True:
        try:
            limite = int(input("Digite um número (1 a 30000): "))
            if 1 <= limite <= 30000:
                break
            print("Valor inválido!")
        except ValueError:
            print("Digite um número inteiro!")

    for atual in range(limite, 0, -1):
        print(f"N: {atual}, Primo: {eh_primo(atual)}, Divisores: {contar_divisores(atual)}, Perfeito: {eh_perfeito(atual)}")
        if atual % 10 == 0 and input("Continuar? (s/n): ").lower() != 's':
            break

def calculadora():
    while True:
        print("\n1 - Soma | 2 - Subtração | 3 - Multiplicação | 4 - Divisão | 5 - Tabuada | 6 - Sair")
        escolha = input("Escolha: ")
        if escolha == "6":
            break
        if escolha == "5":
            mostrar_tabuada()
            continue

        try:
            numero1, numero2 = map(int, input("Digite dois números (1 a 1000): ").split())
            if not (1 <= numero1 <= 1000 and 1 <= numero2 <= 1000):
                print("Valores inválidos!")
                continue
        except ValueError:
            print("Entrada inválida!")
            continue

        operacoes = {
            "1": numero1 + numero2,
            "2": numero1 - numero2,
            "3": numero1 * numero2,
            "4": numero1 / numero2 if numero2 != 0 else "Erro! Divisão por zero."
        }
        print(f"Resultado: {operacoes.get(escolha, 'Opção inválida!')}")

def mostrar_tabuada():
    while True:
        try:
            numero = int(input("Digite um número (1 a 1000): "))
            if 1 <= numero <= 1000:
                break
            print("Valor inválido!")
        except ValueError:
            print("Digite um número inteiro!")

    for i in range(1, numero + 1):
        print(f"{numero} x {i} = {numero * i}")
        if i % 20 == 0 and input("Continuar? (s/n): ").lower() != 's':
            break

def menu_principal():
    while True:
        print("\n1 - Analisar | 2 - Calculadora | 3 - Sair")
        escolha_menu = input("Escolha: ")
        if escolha_menu == "1":
            analisar_numeros()
        elif escolha_menu == "2":
            calculadora()
        elif escolha_menu == "3":
            break
        else:
            print("Opção inválida!")

menu_principal()
