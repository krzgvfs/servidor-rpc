import urllib
import rpyc

req = rpyc.connect("localhost", 18812)
try:
    opc = int(input("1 - Calcular IMC\n2 - Equação de Segundo Grau\n3 - Palíndromo\nOpção: "))
    # IMC
    if opc == 1:
        print("--- Calculo de IMC ---")
        idade = int(input("\nDigite a idade: "))
        altura = float(input("Digite a altura em metros: "))
        peso = float(input("Digite o peso: "))
        
        resultado = req.root.imc(idade, altura, peso)
        print(resultado)

    # Equação 2° Grau
    elif opc == 2:
        print(" --- Calculo de Equação de 2° Grau ---")
        a = int(input("Coeficiente de x^2 (a): "))
        b = int(input("Coeficiente de x (b): "))
        c = int(input("Termo constante (c): "))
        x = req.root.eq2grau(a, b, c)
        print(x)
    # Palíndromo
    elif opc == 3:
        print(" --- Palíndromo  ---")
        palavra = str(input("Digite uma palavra: "))
        result = req.root.palindromo(palavra)
        print(f"Resultado: A palavra {palavra}, {result}")
    else: 
        print("Opção invalida!")

except urllib.error.URLError:
    print('caught a URLError')
