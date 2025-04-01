class Domino:
    def __init__(self, a=0, b=0):
        self.face_a = a
        self.face_b = b
    
    def mostrar_pontos(self):
        print(f"Pontos: ({self.face_a}|{self.face_b})")
    
    def valor(self):
        return self.face_a + self.face_b
    
    def __str__(self):
        return f"({self.face_a}, {self.face_b})"

def criar_domino():
    print("\nCriar nova peça de dominó:")
    a = int(input("Pontos da face A (0-6): "))
    b = int(input("Pontos da face B (0-6): "))
    return Domino(a, b)
    
if __name__ == "__main__":
    pecas = []
    
    while True:
        print("\nMenu Dominó:")
        print("1. Criar peça")
        print("2. Ver todas as peças")
        print("3. Calcular valor total")
        print("4. Sair")
        
        opcao = input("Escolha: ")
        
        if opcao == "1":
            pecas.append(criar_domino())
            print("Peça criada com sucesso!")
        
        elif opcao == "2":
            print("\nPeças no jogo:")
            for i, peca in enumerate(pecas, 1):
                print(f"Peça {i}: {peca}")
        
        elif opcao == "3":
            total = sum(peca.valor() for peca in pecas)
            print(f"\nValor total de todas as peças: {total}")
        
        elif opcao == "4":
            print("Fim do programa!")
            break
        
        else:
            print("Opção inválida!")


