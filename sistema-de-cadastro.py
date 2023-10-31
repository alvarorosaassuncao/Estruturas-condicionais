

#dicionário vazio para armazenar os clientes
clientes = {}

# Função para cadastrar um novo cliente
def cadastrar_cliente():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    
    cliente = {
        'nome': nome,
        'sobrenome': sobrenome,
        'email': email,
        'telefone': telefone
    }
    
    clientes[email] = cliente
    print("Cliente cadastrado com sucesso.")

# Função para listar todos os clientes
def listar_clientes():
    print("Lista de Clientes:")
    for email, cliente in clientes.items():
        print(f"Nome: {cliente['nome']} {cliente['sobrenome']}")
        print(f"Email: {email}")
        print(f"Telefone: {cliente['telefone']}")
        print("-" * 30)

# Função para atualizar um cliente
def atualizar_cliente():
    email = input("Digite o email do cliente que deseja atualizar: ")
    if email in clientes:
        print("Atualize as informações do cliente:")
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        telefone = input("Telefone: ")
        
        clientes[email]['nome'] = nome
        clientes[email]['sobrenome']




cadastrar_cliente()
listar_clientes()
atualizar_cliente()
