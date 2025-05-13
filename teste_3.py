import random 
'''Crie um programa para gerenciar os fornecedores de uma empresa de construção. O programa deve permitir:
Funcionalidades:
Inserir os dados dos fornecedores com os seguintes campos:
NumFor (gerado automaticamente);
NomeFor (nome do fornecedor);
Endereço;
Telefone (validar se tem ao menos 9 dígitos);
NIF (validar se tem exatamente 9 dígitos);
ValorFornecido (valor total dos equipamentos fornecidos);
Desconto (calculado automaticamente);
ValorFinal = ValorFornecido - Desconto.
Regras de desconto:
Se o valor fornecido for entre 1.000 e 5.000 €, aplicar 8% de desconto;
Se entre 5.001 e 10.000 €, aplicar 12%;
Se superior a 10.000 €, aplicar 18%.
Listar os fornecedores um por um (parando entre cada um com um Enter);
Permitir busca direta por número do fornecedor (NumFor).
Observações:
Todas as entradas devem ser validadas.
O programa deve ser estruturado com funções.
Use uma lista para armazenar os dados dos fornecedores.'''

fornecedores=[]

def desc(valorfor):
        if 1000< valorfor <5000:
            valorfor

def Numfor():
    for i in range(1,10000):
        i += 1
        print(f"ID:{i}")
        

def ValorFor():
    valorfor = random.randint(1000, 10000)
    print(f"{valorfor}€")
    

class forn:
    def __init__(self,nfor,nome,endereco,telefone,nif,valor):
        self.nfor=Numfor()    
        self.nome=nome
        self.endereco=endereco
        self.tetelefone=telefone
        self.nif=nif
        self.valor=ValorFor()

    