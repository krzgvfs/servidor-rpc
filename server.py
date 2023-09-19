import math
import rpyc
from fraction import Fraction
from rpyc.utils.server import ThreadedServer 

class MyApps(rpyc.Service):
    def exposed_imc(self, idade, altura, peso):
        imc = peso / (pow(altura, 2))

        if (imc < 18.5):
            result = "Magreza"
        elif (imc >= 18.5 and imc <= 24.9):
            result = "Normal"
        elif (imc >= 25 and imc <= 29.9):
            result = "Sobrepeso"
        elif (imc >= 30 and imc <= 34.9):
            result = "Obesidade grau I"
        elif (imc >= 35 and imc <= 39.9):
            result = "Obesidade grau II"
        elif( imc > 40):
            result = "Obesidade grau III"
        return result
    
    def exposed_equacao2grau(self, a, b, c):
        # Trabalhando exclusivamente com Bhaskara
        
        # Equação de 2° Grau
        if ( a != 0 and b != 0 and c != 0):
            print("Solicitado: Equação Completa")
            # Identificando o delta
            delta = pow((b),2) - (4 * (a) * (c))
           
            if (delta > 0 ): # Possui duas soluções reais distintas para x1​ e x2
                print("Delta > 0")
                # Identificando as raizes
                x1 = Fraction(-b + math.sqrt(delta), (2*a))
                x2 = Fraction(-b - math.sqrt(delta), (2*a))

                if x1.denominator == 1:
                    raizPositiva = x1.numerator
                else:
                    raizPositiva = x1
                if x2.denominator == 1:
                    raizNegativa = x2.numerator
                else:
                    raizNegativa = x2

                return raizPositiva, raizNegativa

            elif(delta == 0): # Possui uma solução real (uma raiz dupla) que é igual para x1​ e x2
                print("Delta == 0")
                x1 = Fraction(-b, (2 * a))

                if x1.denominator == 1:
                    raizPositiva = x1.numerator
                else:
                    raizPositiva = x1

                return raizPositiva

            elif(delta < 0): # Não possui soluções reais, mas duas soluções complexas conjugadas, uma para x1​ e outra para x2​"
                print("Delta < 0")
                ## Essa eu não vou desenrolar não kkkkk
        


    def exposed_palindromo(self, text):
        pass

if __name__ == "__main__":
    server = ThreadedServer(MyApps, port = 18812)
    print('Servidor online')
    server.start()