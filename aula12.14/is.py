class Pet:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.fome = 0
        self.sede = 0
        self.comida = 300

    # Os GETs
    def get_nome(self):
        return self.nome
    
    def get_peso(self):
        return self.peso
    
    def get_fome(self):
        return self.fome
    
    def get_sede(self):
        return self.sede
    
    # Os SETs

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_peso(self, novo_peso):
        self.peso = novo_peso

    def set_fome(self, nova_fome):
        self.fome += nova_fome
        while self.fome >= 99:
            diferenca = self.fome - 10
            print(f'Vc deve alimentar pelo menos { diferenca } a/o { self.nome }')
            nova_comida = int(input('Quanto de comida você quer dar para seu pet?'))
            self.comida -= nova_comida
            self.fome -= nova_comida
            self.peso -= 2

    def set_sede(self, nova_sede):
        self.sede = nova_sede


    def imprimir(self):
        print(f'Olá, me chamo { self.nome }')
        print(f'Estou pesando { self.peso }Kg')
        print(f'MInha fome está { self.fome }')
        print(f'Minha sede está { self.sede }')

caozinho = Pet('Bodo', 10)

caozinho.imprimir()

caozinho.set_fome(50)
caozinho.imprimir()
caozinho.set_fome(60)
caozinho.imprimir()