class ControleRemoto:
    def __init__(self, cor, tamanho, marca, qtd_pilhas, infra_vermelho):
        self.botao = None
        self.cor = cor
        self.tamanho = tamanho
        self.marca = marca
        self.qtd_pilhas = qtd_pilhas
        self.painel = False
        self.infra_vermelho = infra_vermelho
        self.temperatura = 0

    # metodos
    def ligar(self):
        self.painel = True

    def desligar(self):
        self.painel = False

    def set_temperatura(self, nova_temperatura):
        if self.painel == False:
            print('Temperatura não pode ser alterada. Ar Desligado')
        else:
            self.temperatura = nova_temperatura


    def get_temperatura(self):
        return self.temperatura  
     
    def pressionar_botao(self, tipo_de_botao):
        self.botao = tipo_de_botao
        if self.botao == 'Ligar' and self.canal == 0:
            print('Ar está ligado')
            self.ligar()
        elif self.botao == 'Desligar':
            print('Ar está desligado')
            self.set_temperatura(0)
            self.desligar()
        
controle = ControleRemoto('branco', 'medio', 'elgin', 2, True)

controle.pressionar_botao('Ligar')

controle.set_temperatura(20)

print(controle.get_temperatura())

controle.pressionar_botao('Desligar')

print(controle.get_temperatura( ))