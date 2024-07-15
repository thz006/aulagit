def calculadora():
    operacao=(str(input("Escolha a operação digitando o sinal da operação\n+\n-\n*\n/\nescolha: ")))
    if operacao == "+":
        n1=float(input("numero: "))
        n2=float(input("nuemro: "))
        result=n1+n2
        print("O resultado é: ",result)
    elif operacao == "-":
        n1=float(input("numero: "))
        n2=float(input("nuemro: "))
        result=n1-n2
        print("O resultado é: ",result)
    elif operacao == "*":
        n1=float(input("numero: "))
        n2=float(input("nuemro: "))
        result=n1*n2
        print("O resultado é: ",result)
    elif operacao == "/":
        n1=float(input("numero: "))
        n2=float(input("nuemro: "))
        result=n1/n2
        print("O resultado é: ",result)
    else:
        print("Operação Inválida!")
calculadora()