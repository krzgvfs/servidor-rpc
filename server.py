import math
import rpyc
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
        
    def exposed_equacao2grau(self, text):
        pass
    def exposed_palindromo(self, text):
        pass

if __name__ == "__main__":
    server = ThreadedServer(MyApps, port = 18812)
    print('Servidor online')
    server.start()