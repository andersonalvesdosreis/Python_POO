class Produto:
    def __init__(self,nome,preco=0):
        self.nome = nome
        self.preco = float(preco)

    def etiqueta(self):
        print(f"{'Produto':<20} | {'Valor (R$)':>10}")
        print("-" * 33)
        print(f"{self.nome:<20} | R$ {self.preco:>8.2f}")

produto = Produto('Pastel',10)
produto.etiqueta()