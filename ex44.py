class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Erro: Saldo insuficiente!")
        else:
            self.__saldo -= valor

    def exibir_saldo(self):
        return f"{self.__saldo:.2f}"

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, novo_nome):
        if not novo_nome.strip():
            print("Erro: Nome do titular não pode ser vazio!")
        else:
            self.__titular = novo_nome

    def __str__(self):
        return f"Conta de {self.titular}"

if __name__ == "__main__":
    c1 = ContaBancaria("Alice", 1000)
    print(c1)  
    
    c1.depositar(500)
    print(c1.exibir_saldo())  # 1500.00
    
    c1.sacar(2000)  
    
    c1.sacar(300)
    print(c1.exibir_saldo())  # 1200.00
    
    c1.titular = ""  