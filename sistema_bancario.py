menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor_sacado_dia = 0.0

while True:
    
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Valor que deseja depositar: R$"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor}"
        else:
            print("O valor do depósito precisa ser maior que 0.")

    if opcao == "s":
        print("Saque")
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Valor que deseja sacar: R$"))
            valor_sacado_dia += valor

            if valor_sacado_dia <= limite:
                if valor <= saldo:
                    saldo -= valor
                    extrato += f"Saque: R${valor}"
                    numero_saques += 1
                    print(f"Valor sacado: R${valor_sacado_dia}")
                else:
                    print("Seu saldo é insuficiente. Tente sacar outro valor.")
            else:
                valor_sacado_dia -= valor
                print("Você atingiu o limite de valor sacado por dia.")                    
        else:
            print("Você atingiu o limite de saques diários.")        
      
    if opcao == "e":
        if extrato != "":
            print(f"Extrato: {extrato}")
            print(f"Saldo atual: R${saldo}")
        else:
            print("Não foram realizadas movimentações.")

    if opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")