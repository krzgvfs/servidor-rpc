import rpyc

req = rpyc.connect("localhost", 18812)

try:
    opcao = int(input("1 - Calcular IMC\n2 - Equação de Segundo Grau\n3 - Palíndromo\nOpção: "))

    # IMC
    if opcao == 1:
        print("--- Calculo de IMC ---")
        idade = int(input("\nDigite a idade: "))
        altura = float(input("Digite a altura em metros: "))
        peso = float(input("Digite o peso: "))
        
        resultado = req.root.imc(idade,altura,peso)
        print(resultado)

    # Equação 2° Grau
    elif opcao == 2:
        raizEq = []
        print(" --- Calculo de Equação de 2° Grau ---")

        a = int(input("Coeficiente de x^2 (a): "))
        if (a != 0):
            b = int(input("Coeficiente de x (b): "))
            c = int(input("Termo constante (c): "))
            raizEq = req.root.equacao2grau(a, b, c)
            print(f"\nEquação: {a}x²{b}x{c}=0\n\nx1 = {raizEq[0]}\nx2 = {raizEq[1]}\n\nResultado = ({raizEq[0]}; {raizEq[1]})\n")
        else:
            print("Os fatores informados são caracteristicos de uma equação linear! Por favor, Informe uma Equação de 2° Grau.")

    elif opcao == 3:
        print(" --- Palíndromo  ---")
        palavra = str(input("Digite uma palavra: "))
        result = req.root.palindromo(palavra)
        print(f"Resultado: A palavra {palavra} {result}")

    else: 
        print("Opção invalida!")

except urllib.error.URLError:
    print('caught a URLError')
