from receitadespesas import adcreceitas, adcdespesas
from consultsaldo import saldoatual
from listartransacao import todastransacoes

def menu():
    while True:
        print("=============Menu Principal==============")
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Consultar saldo atual")
        print("4. Listar todas as transações")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adcreceitas()
        elif opcao == "2":
            adcdespesas()
        elif opcao == "3":
            saldoatual()
        elif opcao == "4":
            todastransacoes()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":  
    menu()