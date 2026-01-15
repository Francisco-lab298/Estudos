class Vendedor():
        def __init__(self, nome):
            self.nome = nome
            self.vendas = 0
            
        def vendeu(self, vendas):
            self.vendas = vendas
            
        def bateu_meta(self, meta):
            if self.vendas > meta:
                print(self.nome, "bateu a meta")
            else:
                print(self.nome, "não bateu a meta")
            


vendedor1 = Vendedor("Chico")
vendedor1.vendeu(1000)
vendedor1.bateu_meta(600)

vendedor2 = Vendedor("cisco")
vendedor2.vendeu(500)
vendedor2.bateu_meta(600)