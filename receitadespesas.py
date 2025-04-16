#função que irá adicionar receitas
def adcreceitas():
    print("=============Adicionar Receitas============")
    receita = input("Digite o nome da receita: ")
    valorreceita = input("Digite o valor da receita: ")
    datareceita = input("Digite a data da receita (dd/mm/aaaa): ")
    
    with open("receitas.txt", "a") as arquivo: 
        #O arquivo irá armazenar a receita e o valor separados por vírgula
        arquivo.write(f"{receita},{valorreceita},{datareceita}\n")
        print("Receita cadastrada com sucesso!")
        
def calculartotalreceitas():
    total = 0
    try:
        with open("receitas.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(",")
                if len(partes)>=2:
                    try:
                        total += float(partes[1])
                    except ValueError:
                        pass
    except ValueError:
        pass
    return total
        

#função que adiciona despesas
def adcdespesas():
    print("=============Adicionar Despesas============")
    despesa = input("Digite o nome da despesa: ")
    valordespesa = input("Digite o valor da despesa: ")
    datadespesa = input("Digite a data da despesa (dd/mm/aaaa): ")
    
    with open("despesas.txt", "a") as arquivo: 
        #O arquivo irá armazenar a receita e o valor separados por vírgula
        arquivo.write(f"{despesa},{valordespesa},{datadespesa}\n")
        print("Despesa cadastrada com sucesso!")
        

def calculartotaldespesas():
    total = 0
    try:
        with open("despesas.txt", "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(",")
                if len(partes)>=2:
                    try:
                        total += float(partes[1])
                    except ValueError:
                        pass
    except ValueError:
        pass
    return total

