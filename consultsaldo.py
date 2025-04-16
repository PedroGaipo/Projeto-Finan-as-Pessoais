from receitadespesas import calculartotalreceitas, calculartotaldespesas

def saldoatual():  
    while True:
        print("=============Consultar Saldo============")
        
        totalreceitas = calculartotalreceitas()
        totaldespesas = calculartotaldespesas()
        saldo = totalreceitas - totaldespesas
        
        print("Seu saldo atual é: R$",saldo)
        opcao = input("\nGostaria de voltar ao Menu Principal? (s/n): ")

        
        if opcao == "s":
            break
        elif opcao == "n":
            print("Saindo do sistema...\n")
            exit()
        else:
            print("Opção inválida. Tente novamente.\n")