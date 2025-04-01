class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    def _validar_preco(self, preco):
        return preco > 0

    def alterar_preco(self, novo_preco):
        if self._validar_preco(novo_preco):
            self.__preco = novo_preco
        else:
            print("Erro: O preço deve ser maior que zero.")

    def vender(self, quantidade):
        if quantidade <= self.__estoque:
            self.__estoque -= quantidade
        else:
            print("Erro: Estoque insuficiente!")

    def reabastecer(self, quantidade):
        self.__estoque += quantidade

    def exibir_detalhes(self):
        print(f"Produto: {self.__nome}")
        print(f"Preço: {self.__preco:.1f}")
        print(f"Estoque: {self.__estoque}")

    def __str__(self):
        return f"Produto: {self.__nome}"


if __name__ == "__main__":
    p = Produto("Caderno", 15.50, 10)
    print(p)            
    
    p.alterar_preco(-5)     
    p.alterar_preco(20)
    
    p.vender(5)
    p.vender(10)        
    
    p.reabastecer(15)
    p.exibir_detalhes()     