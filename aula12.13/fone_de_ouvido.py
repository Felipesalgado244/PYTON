class FoneDeOuvido:
    def get_volume(self):
        print('entrei no GET')
        return self.__volume
    def set_volume(self, novo_volume):
        print(f'entrei no SET com o valor de { novo_volume }')
        self.__volume = novo_volume

    volume = property(get_volume, set_volume)

fone = FoneDeOuvido()

fone.volume = 200

print(fone.volume)