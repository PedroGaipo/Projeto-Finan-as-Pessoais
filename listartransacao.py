from receitadespesas import armazenarreceitas
from receitadespesas import armazenardespesas

transacoesreceitas = armazenarreceitas()
transacoesdespesas = armazenardespesas()

def todastransacoes():
    print("===========Todas as trnasações===========\n")
        
    if not transacoesreceitas and not transacoesdespesas:
        print("Nenhuma transação encontrada.")
    else:
        if transacoesreceitas:
            print("Últimas transações de receitas:")
            for i, linha in enumerate(transacoesreceitas, start=1):
                print(f"{i}. {linha}")  
            print()
                
        if transacoesdespesas:
            print("Últimas transações de despesas:")
            for u, linha in enumerate(transacoesdespesas, start=1):
                print(f"{u}. {linha}")
            print()
            
    while True:        
        opcao = input("\nGostaria de voltar ao Menu Principal? (s/n): ")
        if opcao == "s":
            break
        elif opcao == "n":
            print("Saindo do sistema...\n")
            exit()
        else:
            print("Opção inválida. Tente novamente.\n")