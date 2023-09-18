import rpyc

req = rpyc.connect("localhost", 18812)

try:
    op = int(input("1 - Calcular IMC\n2 - Equação de Segundo Grau\n3 - Palíndromo\nOpção: "))

    if op == 1:
        idade = int(input("\nDigite a idade: "))
        altura = float(input("Digite a altura em metros: "))
        peso = int(input("Digite o peso: "))
        
        result = req.root.imc(idade,altura,peso)
        print(result)

    elif op == 2:
        pass
    elif op == 3:
        pass
    else: 
        print("Opção invalida!")

except urllib.error.URLError:
    print('caught a URLError')
