import cmath
import math
import rpyc
import sympy
from rpyc.utils.server import ThreadedServer

# By Marcos André Santos Junior, 24 September 2023.
# https://github.com/krzgvfs/servidor-rpc

"""
Guia de uso:

1 - Criando ambiente virtual.
Windows: py -m venv servrpc-env 
Linux: python3 -m venv servrpc-env 

2 - Instalando dependências:
Windows: py -m pip install  -r requirements.txt
Linux: python3 pip install -r requirements.txt

Client: 
3 - Estabelecer conexão: 
requisição = rpyc.connect("localhost", 18812)

4 - Funções do Servidor: 
imc(int idade=23, float altura=1.78, float peso=108)                       
eq2grau(int a=2, int b=-4, int c= 2) Representação: a = ax², b = x, c = c  
palindromo(palavra=Arara)                                                  

5 - Acessando métodos remotos: 
Exemplo: 
calcularImc = req.root.imc()

"""


class MyApps(rpyc.Service):
    @staticmethod
    def exposed_imc(idade=23, altura=1.78, peso=87):
        """
        Está função realiza o cálculo de IMC.
        :param idade: Idade do brother.
        :type idade: Int
        :param altura: Valor da altura em metros.
        :type altura: Float
        :param peso: Valor do peso em kg.
        :type altura: Float

        :return: A função irá retornar uma string informando a classificação resultante do cálculo IMC.
        :rtype: String

        """
        print("Requisição: IMC")
        imc = peso / (pow(altura, 2))

        if imc < 18.5:
            msg = f"\nIdade:{idade}, Altura:{altura:.2f}m, Peso:{peso:.2f}kg\nClassificação: Magreza"
        elif 18.5 <= imc < 25:
            msg = f"\nIdade:{idade}, Altura:{altura:.2f}m, Peso:{peso:.2f}kg\nClassificação: Normal"
        elif 25 <= imc < 30:
            msg = f"\nIdade:{idade}, Altura:{altura:.2f}m, Peso:{peso:.2f}kg\nClassificação: Sobrepeso"
        elif 30 <= imc < 35:
            msg = f"\nIdade:{idade}, Altura:{altura:.2f}m, Peso:{peso:.2f}kg\nClassificação: Obesidade grau I"
        elif 35 <= imc < 40:
            msg = f"\nIdade:{idade}, Altura:{altura:.2f}m, Peso:{peso:.2f}kg\nClassificação: Obesidade grau II"
        else:
            msg = f"\nIdade:{idade}, Altura:{altura:.2f}m, Peso:{peso:.2f}kg\nClassificação: Obesidade grau III"

        return msg

    @staticmethod
    def exposed_eq2grau(a=2, b=-4, c=2):
        """
        Está função realiza o cálculo de equações de segundo grau completas e incompletas, abrangendo variações
        de resolução com base na variável delta.
        :param a: Representa o Coeficiente "ax²" da função
        :type a: Int
        :param b: Representa o Coeficiente "x" da função
        :type b: Int
        :param c: Representa o termo Constante "c" da função
        type c: Int

        :return: Os retornos da função podem variar com base na estrutura da equação informada, mas no geral
        será uma String informativa com os resultados encontrados para a função.
        """

        # ax² + bx - c
        print("Requisição: Equação de 2° Grau")
        if a != 0:
            # Equação Completa ax²+bx+c=0
            if a != 0 and b != 0 and c != 0:
                # Identificando o delta.
                delta = pow(b, 2) - (4 * a * c)

                # Possui duas soluções reais distintas para x1 e x2.
                if delta > 0:
                    # Identificando as raiz
                    x1 = (-b + math.sqrt(delta)) / (2 * a)
                    x2 = (-b - math.sqrt(delta)) / (2 * a)
                    msg = f"\nEquação: {a}x²{b}x{c}=0\nDelta > 0\nResultado: \nx1 = {x1:.2f}  \nx2 = {x2:.2f}"
                    return msg
                # Possui uma única solução real igual para x1 e x2.
                elif delta == 0:
                    x1 = (-b + math.sqrt(delta)) / (2 * a)
                    msg = f"\nEquação: {a}x²{b}x{c}=0\nDelta = 0\nResultado: \nx1 e x2 = {x1:.2f}"
                    return msg
                # Não possui soluções reais, mas duas soluções complexas conjugadas, uma para x1 e x2.
                elif delta < 0:
                    # A lib cmath trabalha com números complexos.
                    x1 = (-b + cmath.sqrt(delta)) / (2 * a)
                    x2 = (-b - cmath.sqrt(delta)) / (2 * a)
                    msg = f"\nEquação: {a}x²{b}x{c}=0\nDelta < 0\nResultado: \nx1 = {x1:.2f}  \nx2 = {x2:.2f}"
                    return msg
            # Equação Incompleta ax²+bx=0
            elif a != 0 and b == 0 and c != 0:
                x = sympy.symbols('x')
                eq = a * pow(x, 2) + c
                result = sympy.solve(eq, x)

                if len(result) == 2:
                    msg = f"Resultado:\nx = {result[0]}\nx = {result[1]}"
                elif len(result) == 1:
                    msg = f"Resultado:\nx = {result[0]}"
                else:
                    msg = "Sem soluções reais."
                return msg
            # Equação Incompleta ax²+c=0
            elif a != 0 and b != 0 and c == 0:
                rg = []
                count = 0
                x = sympy.symbols('x')  # Variável simbólica para representar o valor desconhecido.
                eq = a * pow(x, 2) + b * x
                result = sympy.solve(eq, x)
                for naruto in result:
                    rg.append(naruto)
                    count += 1
                    # print(count)

                if len(result) == 2:
                    msg = f"Resultado:\nx = {result[0]}\nx = {result[1]}"
                elif len(result) == 1:
                    msg = f"Resultado:\nx = {result[0]}"
                else:
                    msg = "Sem soluções reais."
                return msg
        else:
            msg = ("Os fatores informados são característicos de uma equação linear. "
                   "Informe uma Equação de 2° Grau valida.")
            return msg

    @staticmethod
    def exposed_palindromo(palavra="arara"):
        """
        Está função realiza a verificação em uma palavra para verificar se a mesma é um palíndromo, ou seja,
        se sua estrutura se mantém a mesma quando invertida.
        :param palavra: Palavra submetida a verificação de Palindromo.
        :type palavra: String
        :return: O retorno da função é uma string resultante da verificação.
        """
        print("Requisição: Palíndromo")
        if palavra.lower() == palavra.lower()[::-1]:
            msg = "é um Palíndromo!\n"
        else:
            msg = "não é um Palíndromo!\n"
        return msg


if __name__ == "__main__":
    server = ThreadedServer(MyApps, port=18812)
    print('Servidor online')
    server.start()
