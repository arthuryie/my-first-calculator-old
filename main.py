# Definir operações
def calcular(operacao, numero1, numero2):
    if operacao == 'soma':
        return numero1 + numero2
    elif operacao == 'subtracao':
        return numero1 - numero2
    elif operacao == 'multiplicacao':
        return numero1 * numero2
    elif operacao == 'divisao':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "0"

# Entrada do user
operacao = input("Digite a operação desejada: ") 

#Verificar se a operação é válida
while operacao not in ['soma', 'subtracao', 'multiplicacao', 'divisao']:
    print("Por favor, escolha uma operação válida.")
    operacao = input("Digite a operação desejada: ").strip().lower()



numero1 = float(input("Digite o primeiro número da operação: "))
numero2 = float(input("Digite o segundo número da operação: "))

# Calcular
resultado = calcular(operacao, numero1, numero2)

# Mostrar resultado
print("Resultado: ", resultado)