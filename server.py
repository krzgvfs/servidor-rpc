import cmath
import math
import rpyc
from rpyc.utils.server import ThreadedServer


class MyApps(rpyc.Service):
    @staticmethod
    def exposed_imc(idade, altura, peso):
        print("Requisição: IMC")
        imc = peso / (pow(altura, 2))

        if imc < 18.5:
            msg = "Magreza"
        elif 18.5 <= imc < 25:
            msg = "Normal"
        elif 25 <= imc < 30:
            msg = "Sobrepeso"
        elif 30 <= imc < 35:
            msg = "Obesidade grau I"
        elif 35 <= imc < 40:
            msg = "Obesidade grau II"
        else:
            msg = "Obesidade grau III"

        return msg

    @staticmethod
    def exposed_eq2grau(a, b, c):
        # ax² + bx + c
        print("Requisição: Equação de 2° Grau")
        if a != 0:
            # Equação Completa.
            if a != 0 and b != 0 and c != 0:
                # Identificando o delta.
                delta = pow(b, 2) - (4 * a * c)

                # Possui duas soluções reais distintas para x1 e x2.
                if delta > 0:
                    print("Delta > 0")
                    # Identificando as raiz
                    x1 = (-b + math.sqrt(delta)) / (2 * a)
                    x2 = (-b - math.sqrt(delta)) / (2 * a)
                    msg = f"\nEquação: {a}x²{b}x{c}=0\nResultado: \nx1 = {x1:.2f}  \nx2 = {x2:.2f}"
                    return msg
                # Possui uma única solução real igual para x1 e x2.
                elif delta == 0:
                    print("Delta == 0")
                    x1 = (-b + math.sqrt(delta)) / (2 * a)
                    msg = f"\nEquação: {a}x²{b}x{c}=0 \nResultado: \nx1 e x2 = {x1:.2f}"
                    return msg
                # Não possui soluções reais, mas duas soluções complexas conjugadas, uma para x1 e x2.
                elif delta < 0:
                    print("Delta < 0")
                    # A lib cmath trabalha com números complexos.
                    x1 = (-b + cmath.sqrt(delta)) / (2 * a)
                    x2 = (-b - cmath.sqrt(delta)) / (2 * a)
                    msg = f"\nEquação: {a}x²{b}x{c}=0\nResultado: \nx1 = {x1:.2f}  \nx2 = {x2:.2f}"
                    return msg
        else:
            msg = ("Os fatores informados são característicos de uma equação linear. "
                   "Informe uma Equação de 2° Grau valida.")
            return msg

    @staticmethod
    def exposed_palindromo(palavra):
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
