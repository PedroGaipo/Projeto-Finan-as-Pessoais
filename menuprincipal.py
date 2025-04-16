from receitadespesas import adcreceitas, adcdespesas
from consultsaldo import saldoatual

def menu():
    while True:
        print("=============Menu Principal==============")
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Consultar saldo atual")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adcreceitas()
        elif opcao == "2":
            adcdespesas()
        elif opcao == "3":
            saldoatual()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
menu()