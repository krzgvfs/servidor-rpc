import rpyc

req = rpyc.connect("localhost", 18812)

try:
    op = int(input("1 - Calcular IMC\n2 - Equação de Segundo Grau\n3 - Palíndromo\nOpção: "))

    # IMC
    if op == 1:
        idade = int(input("\nDigite a idade: "))
        altura = float(input("Digite a altura em metros: "))
        peso = float(input("Digite o peso: "))
        
        result = req.root.imc(idade,altura,peso)
        print(result)

    # Equação 2° Grau
    elif op == 2:
        print(" --- Calculo de Equação de 2° Grau ---")

        a = int(input("Coeficiente de x^2 (a): "))
        if (a != 0):
            b = int(input("Coeficiente de x (b): "))
            c = int(input("Termo constante (c): "))
            raizPositiva, raizNegativa = req.root.equacao2grau(a, b, c)
            print(f"\nEquação: {a}x²{b}x{c}=0\n\nx1 = {raizPositiva}\nx2 = {raizNegativa}\n\nResultado = ({raizPositiva}; {raizNegativa})\n")
        else:
            print("Os fatores informados são caracteristicos de uma equação linear! Por favor, Informe uma Equação de 2° Grau.")

    elif op == 3:
        pass
    else: 
        print("Opção invalida!")

except urllib.error.URLError:
    print('caught a URLError')
