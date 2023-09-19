import math
import urllib
import rpyc
from fraction import Fraction
from rpyc.utils.server import ThreadedServer 

class MyApps(rpyc.Service):
    def exposed_imc(self, idade, altura, peso):
        print("Requisição: IMC")
        imc = peso / (pow(altura, 2))

        if imc < 18.5:
            result = "Magreza"
        elif 18.5 <= imc < 25:
            result = "Normal"
        elif 25 <= imc < 30:
            result = "Sobrepeso"
        elif 30 <= imc < 35:
            result = "Obesidade grau I"
        elif 35 <= imc < 40:
            result = "Obesidade grau II"
        else:
            result = "Obesidade grau III"
        return result

    def exposed_equacao2grau(self, a, b, c):
        print("Requisição: Equação de 2° Grau")
        raizEq = []
        # Trabalhando exclusivamente com Bhaskara
        if ( a != 0 and b != 0 and c != 0): # Equação Completa.
            # Identificando o delta
            delta = pow((b),2) - (4 * (a) * (c))
           
            if (delta > 0 ): # Possui duas soluções reais distintas para x1​ e x2
                print("Delta > 0")
                # Identificando as raizes
                x1 = Fraction(-b + math.sqrt(delta), (2*a))
                x2 = Fraction(-b - math.sqrt(delta), (2*a))

                if x1.denominator == 1:
                    raizEq.append(x1.numerator)
                else:
                    raizEq.append(x1)
                if x2.denominator == 1:
                    raizEq.append(x2.numerator)
                else:
                    raizEq.append(x2)

                return raizEq

            elif(delta == 0): # Possui uma solução real (uma raiz dupla) que é igual para x1​ e x2
                print("Delta == 0")
                x1 = Fraction(-b, (2 * a))

                if x1.denominator == 1:
                    raizEq.apped(x1.numerator)
                else:
                    raizEq.apped(x1)

                return raizEq

            elif(delta < 0): # Não possui soluções reais, mas duas soluções complexas conjugadas, uma para x1​ e outra para x2​"
                print("Delta < 0")
                pass

    def exposed_palindromo(self, palavra):
        print("Requisição: Políndromo")
        if palavra == palavra[::-1]:
            result = "é um Palíndromo!\n"
        else: 
            result = "não é um Palíndromo!\n"
        return result

if __name__ == "__main__":
    server = ThreadedServer(MyApps, port = 18812)
    print('Servidor online')
    server.start()