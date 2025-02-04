menu = """
1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair
"""

saldo = 0.0
limite = 500.0
extrato = ""
numero_saque = 0
limite_saque = 3

while True:
    print(menu)
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        deposito = float(input("Informe o valor de deposito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R${deposito: }\n"
            print(f"Seu saldo atual é de R${saldo: }")
        else:
            print("O valor do depósito deve ser maior que zero.")
        
    elif opcao == 2:
        saque = float(input("Informe o valor que deseja sacar: "))
        if saque > 0 and saque <= saldo and numero_saque < limite_saque and saque <= limite:
            saldo -= saque
            extrato += f"Saque: R${saque: }\n"
            numero_saque += 1
            print(f"Seu saldo atual é de R${saldo: }")
        else:
            if saque > saldo:
                print("Saldo insuficiente para sacar.")
            elif numero_saque >= limite_saque:
                print("Você atingiu o limite de saques diários.")
            elif saque > limite:
                print(f"O valor do saque não pode ultrapassar R${limite: }.")
            else:
                print("O valor do saque deve ser maior que zero.")
        
    elif opcao == 3:
        print("Extrato:")
        print(extrato)
        print(f"Seu saldo atual é de R${saldo: }")
        
    elif opcao == 4:
        print("Obrigado por utilizar nossos serviços!")
        break
        
    else:
        print("Opção inválida, tente novamente! Informe apenas números de 1 a 4.")