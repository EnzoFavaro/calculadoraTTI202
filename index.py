num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input('''
 
+ (adição)
- (subtração)
* (multiplicação)
/ (divisão) 

Por favor, insira o operador que será usado:
''')

match operacao:
    case '+':
        resultado = num1 + num2
        print("A soma de ",num1, "+",num2," é:" , resultado)
    case '-':
        resultado = num1 - num2
        print("A subtração de ",num1, "-",num2," é:" , resultado)
    case '*':
        resultado = num1 * num2
        print("A multiplicação de ",num1, "*",num2," é:" , resultado)
    case '/':
        resultado = num1 / num2
        print("A divisão de ",num1, "/",num2," é:" , resultado)
    case _:
        print("Insira um operador válido!")


