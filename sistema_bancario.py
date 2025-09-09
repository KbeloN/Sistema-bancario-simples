saldo = 0
extrato = ""
saques_feitos = 0
LIMITE_SAQUE_DIARIO = 3
LIMITE_SAQUE_RS = 500.00

def verificar_de_letras_opcao (valor):
    if any(caractere.isalpha() for caractere in valor):
        return 401
    else:
        return valor
    
def verificar_de_letras_saque_deposito (valor):
    if any(caractere.isalpha() for caractere in valor):
        return 0.00
    else:
        return valor

def saque():
    global saldo, saques_feitos, extrato

    if saques_feitos == LIMITE_SAQUE_DIARIO:
        print("Não foi possível realizar porque chegou no limíte de saques diários.")
        return

    saque_input = input(f"Deseja fazer um saque de quantos reais (O Limite de saque é R$500.00)?\nR$")
        
    saque = float(verificar_de_letras_saque_deposito(saque_input))

    if saque > LIMITE_SAQUE_RS:
        print("Não foi possível realizar porque ultrapassou o limite de saque em reais.")
    elif saque > saldo:
        print("Não foi possível realizar porque a sua conta não tem saldos suficientes.")
    elif saque > 0.00:
        print("Saque feito com sucesso!")
        saldo -= saque
        saques_feitos += 1
        extrato += f"Saque - R${saque:.2f}\n"
    else:
        print("Não foi possível realizar o saque com o valor apresentado.")

def depositar():
    global saldo, extrato

    deposito_input = input("Deseja fazer um deposito de quantos reais?\nR$")

    deposito = float(verificar_de_letras_saque_deposito(deposito_input))
    if deposito > 0.00:
        print("Deposito feito com sucesso!")
        saldo += deposito
        extrato += f"Deposito - R${deposito:.2f}\n"
    else:
        print("Não foi possível realizar o depósito com o valor apresentado.")

# Sistema bancário

while True:
    menu = f'''
    {" Menu ".center(30, "=")}
        1 - Sacar
        2 - Depositar
        3 - Extrato
        0 - Sair do sistema
    {"".center(30, "=")}
'''

    print(menu)

    input_usuario = input("Sua escolha:")
    print()
    
    opcao = int(verificar_de_letras_opcao(input_usuario))

    if opcao == 1:
        saque()

    elif opcao == 2:
        depositar()   

    elif opcao == 3:
        print(f'''    {" Extrato ".center(30, "=")}
{"Nenhuma operação foi realizada" if not extrato else extrato}

Saldo atual - R${saldo:.2f}
    {"".center(30, "=")}''')   

    elif opcao == 0:
        print("Saindo do sistema...")
        break 
    else:
        print("O valor informado é inválido.")