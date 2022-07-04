def calculadora(num1, num2, operacao, resultado):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo numero: "))
    operacao = str(input("Digite a operação desejada:\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão"))
    if (operacao == 1):
        resultado = num1+num2
    elif (operacao == 2):
        resultado = num1-num2
    elif (operacao == 3):
        resultado = num1*num2
    elif (operacao == 4):
        resultado = num1/num2
    else:
        print("0")

        return resultado            

    



    



    
