class Automovel:
    def __init__(self, placa, cor):
        self.__placa = placa
        self.__cor = cor
    def get_placa(self):
        return self.__placa
    def get_cor(self):
        return self.__cor
    def set_cor(self, nova_cor):
        self.__cor = nova_cor
    def dirigir(self, velocidade):
        print(f'Estou dirigindo a {velocidade} km/h')

carro = Automovel('FDS-2211', 'preto')
moto = Automovel('DDD-088', 'branca')
caminhao = Automovel('SCN-112', 'azul')

# chamadas GET
print(f'A cor do carro é { carro.get_cor() }')
print(f'A cor da moto é { moto.get_cor() }')
print(f'A cor do caminão é { caminhao.get_cor() }')

# Chamadas SET
carro.set_cor('vermelho')
moto.set_cor('cinza')
caminhao.set_cor('marrom')

# novas chamadas GET
print(f'A nova cor da moto é { moto.get_cor() }')
print(f'A nova cor do carro é { carro.get_cor() }')
print(f'A nova cor do caminão é { caminhao.get_cor() }')
