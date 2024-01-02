class Automovel:
    def __init__ (self, placa):
        self.placa = placa
    def get_placa(self):
        return self.placa
    def dirigir(self, velocidade):
        print(f'Estou dirigindo a {velocidade} km/h')

carro = Automovel('DHA-3268')
print(carro.get_placa())
carro.dirigir(310)

moto = Automovel('WEB-1510')
print(moto.get_placa())
moto.dirigir(142)

caminhao = Automovel('COD-8899')
print(caminhao.get_placa())
caminhao.dirigir(182)