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

while True:

    opcao = input(menu)

    if opcao == "d":
        print("deposito")
        valor_a_depositar = float(input('informe o valor para deposito:'))
        
        if valor_a_depositar >= 0:
            saldo += valor_a_depositar 
            extrato += f'Deposito de: {valor_a_depositar:.2f}\n'
       
        else: print("valor insuficiente para deposito")
        

    elif opcao == "s":
        quantidade_de_saques =  0
        print("saque")
        valor_a_retirar = float(input('informe o valor do saque:'))

        if valor_a_retirar >= 500:
            print('valor para saque nao permitido')

        if saldo >= limite:
            print('excedeu seu limite de saque do dia')
              
        if valor_a_retirar > saldo:
            print('vc nao tem saldo suficiente')

        if quantidade_de_saques >= LIMITE_SAQUES:
            print('excedeu numeros de saques')

        elif valor_a_retirar > 0:
            saldo - valor_a_retirar
            extrato += f'Saque: R$ {valor_a_retirar:.2f}\n'
            numero_saques += 1
    
    elif opcao == "e":
        print("extrato")
        print("nao foram realizadas movimentacoes")
        print("saldo {saldo}")

    elif opcao == "q":
        print("sair")
        break

    else:
        print("operacao invalida, por favor selecione outra opcao")
    

