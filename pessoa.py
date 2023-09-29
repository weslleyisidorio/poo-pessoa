class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo, estado = 'vivo', estado_civil = 'solteiro', conjuge = None):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__estado_civil = estado_civil
        self.__conjuge = conjuge
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        pass

    @property
    def idade(self):
        if self.estado == 'vivo':
            return self.__idade
        return f'{self.nome} está morto.'
    
    @idade.setter
    def idade(self, idade):
        if idade == 1:
            self.__idade = idade 
        else:
            print('sem permissão')

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter  
    def peso(self, peso):
        if peso > 1:
            self.__peso = peso 
        else:
            print('Peso inválido!')

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura):
        if altura > self.__altura and altura > 0:
            self.__altura = altura

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def estado_civil(self):
        return self.__estado_civil
    
    @estado_civil.setter
    def estado_civil(self, estado):
        self.__estado_civil = estado

    @property
    def conjuge(self):
        return self.__conjuge
    
    @conjuge.setter
    def conjuge(self, conjuge):
        self.__conjuge = conjuge

    def envelhecer(self):
        if self.__estado == 'vivo':
            self.__idade += 1
            if self.idade < 21:
                self.__altura += 0.5
            else:
                print(f'{self.nome}  não pode crescer pois está com 21 anos ou mais.')
            
        else:
            print(f'Operação não realizada, {self.nome} está morto')

    def engordar(self, peso):
        if self.__estado == 'vivo':
            self.__peso += peso
        else:
            print(f'Operação não realizada, {self.nome} está morto')
        

    def emagrecer(self, peso):
        if self.__estado == 'vivo':
            self.__peso -= peso
        else:
            print(f'Operação não realizada, {self.nome} está morto')

    def crescer(self, altura):
        if self.__estado == 'vivo':
            if self.idade <= 21:
                self.__altura += altura
        else:
            print(f'Operação não realizada, {self.nome} está morto')

    def casar(self, pessoa):
        if self.__estado == 'vivo':
            if self.__estado_civil != 'casado(a)' and pessoa.__estado_civil != 'casado(a)' and self.__idade >= 18  and pessoa.__idade >= 18:
                self.__estado_civil = 'casado(a)'
                pessoa.__estado_civil = 'casado(a)'
                self.__conjuge = pessoa
                pessoa.__conjuge = self
                print(f'{self.nome} está casado com {pessoa.nome}')

            else: 
                if self.__estado_civil == 'casado(a)': 
                    print(f'Casamento não realizado. {self.nome} é casado')
                elif pessoa.__estado_civil == 'casado(a)':
                    print(f'Camento não realizado. {pessoa.nome} é casado')
                elif self.__idade < 18:
                    print(f'Casaento não permitido {self.nome} é de menor.')
                elif  pessoa.__idade < 18:
                    print(f'Casamento não permitido. {pessoa.nome} é de menor')

        else:
            print(f'Operação não permitida. {self.nome} está morto')

    def morrer(self):
        self.estado = 'morto'
        print(f'{self.nome} morreu.')
        if self.estado_civil == 'casado(a)':
            conje = self.conjuge
            conje.estado_civil = 'viúvo(a)'

def main():
    maria = Pessoa('Maria', 5, 20, 100, 'F')
    joao = Pessoa('João', 12, 40, 140, 'M')
    pedro = Pessoa('Pedro', 22, 65, 170, 'M')
    bia = Pessoa('Bia', 18, 55, 160, 'F')
    julia = Pessoa('Julia', 30, 65, 170, 'F')
    carlos = Pessoa('Carlos', 2, 11, 80, 'M')
    jonas = Pessoa('Jonas', 34, 70, 180, 'M')

    #maria.idade = 10 # Função não permite receber parametro
    print(f'{maria.nome} - idade: {maria.idade}')
    maria.envelhecer() #Maria cresce 0,5 cm não 5 cm
    print(f'Maria está com {maria.idade} anos e {maria.altura} cm de altura.')

    print('--------------------------------')

    print(f'{pedro.nome} - tem {pedro.altura} cm e {pedro.idade} anos.')
    pedro.envelhecer()

    print('--------------------------------')

    bia.casar(carlos)

    print('--------------------------------')

    pedro.casar(maria)

    print('--------------------------------')

    pedro.casar(julia)

    print('--------------------------------')

    pedro.casar(bia)

    print('--------------------------------')

    maria.morrer()

    print('--------------------------------')

    maria.engordar(1)

    print('--------------------------------')

    bia.casar(jonas)

    print('--------------------------------')

    bia.morrer()

    print('--------------------------------')

    pedro.morrer()

    print('--------------------------------')

    jonas.casar(julia)

    print('--------------------------------')

    pedro.casar(bia)

    print('--------------------------------')

    print(pedro.idade)

    print('--------------------------------')

    joao.idade = 50


if __name__ == '__main__':
     main()