class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []  

    def __add__(self, produto):
        if isinstance(produto, Produto):
            novo_carrinho = CarrinhoDeCompras()
            novo_carrinho.produtos = self.produtos.copy()
            novo_carrinho.produtos.append(produto)
            return novo_carrinho
        raise TypeError("Apenas objetos da classe Produto podem ser adicionados.")

    def total(self):
        return sum(p.preco for p in self.produtos)

    def __str__(self):
        linhas = [f"{p.nome}: R$ {p.preco:.2f}" for p in self.produtos]
        lista_formatada = "\n".join(linhas)
        divisor = "-=" * 20
        return f"{lista_formatada}\n{divisor}\nTotal: R$ {self.total():.2f}"


# Criando os objetos Produto independentes
p1 = Produto("Camiseta", 50.0)
p2 = Produto("Tênis", 200.0)

# Criando o Carrinho e agregando os produtos a ele
carrinho = CarrinhoDeCompras()
carrinho = carrinho + p2
carrinho = carrinho + p1

print(carrinho)

