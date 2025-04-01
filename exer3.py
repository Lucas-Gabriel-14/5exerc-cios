import datetime

class Funcionario:
    def __init__(self, identificacao, sobrenome, nome, data_nasc, data_adm, salario):
        self.id = identificacao
        self.sobrenome = sobrenome
        self.nome = nome
        self.data_nascimento = data_nasc  
        self.data_admissao = data_adm   
        self.salario = salario


    def idade(self):
        ano_atual = datetime.datetime.now().year
        return ano_atual - self.data_nascimento[2]

    def tempo_de_casa(self):
        ano_atual = datetime.datetime.now().year
        return ano_atual - self.data_admissao[2]

    def aumento_de_salario(self):
        anos = self.tempo_de_casa()
        if anos < 5:
            percentual = 0.02
        elif anos < 10:
            percentual = 0.05
        else:
            percentual = 0.10
        self.salario += self.salario * percentual

    def mostrar_funcionario(self):
        print(f"Número pessoal: {self.id}")
        print(f"Sobrenome: {self.sobrenome}")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade()}")
        print(f"Tempo de casa: {self.tempo_de_casa()}")
        print(f"Salário em € : {self.salario:.1f}")

if __name__ == "__main__":
    agente = Funcionario(
        identificacao='007',
        sobrenome='Bond',
        nome='James',
        data_nasc=(11, 11, 1970),
        data_adm=(7, 4, 1995),
        salario=7500
    )
    
    agente.aumento_de_salario()
    agente.mostrar_funcionario()