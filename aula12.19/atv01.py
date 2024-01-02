class Televisao:
    def __init__(self, tamanho, canal):
        self.tamanho = tamanho
        self.canal = canal
        self.ligar_desligar = False

    def ligar(self):
        self.ligar_desligar = True

    def desligar(self):
        self.ligar_desligar = False

    def get_canal(self):
        return self.canal
    
    def set_canal(self, novo_canal):
        if self.ligar_desligar == False:
            print('Canal não pode ser alterado! Televisão desligada.')
        else:
            self.canal == novo_canal

    def pressionar_botao(self, tipo_de_botao):
        self.botao = tipo_de_botao
        if self.botao == 'Ligar' and self.canal >= 1:
            print('TV ligada')
            self.ligar()
        elif self.botao == 'Desligar':
            self.desligar()

tv = Televisao('garande', 2000000000)
tv.pressionar_botao('Ligar')
tv.set_canal(1)
print(f'Canal: {tv.get_canal()}') 