class Gamer:
    def __init__(self, nome, nick, plataforma="PC"):
        self.nome = nome
        self.nick = nick
        self.plataforma = plataforma
        self.lista = []

    def add_jogo(self, *nomes):
        # extend adiciona cada elemento da tupla *nomes direto na lista
        self.lista.extend(nomes)

    def ordenar(self):
        self.lista.sort(key=str.lower)

    def exibir_ficha(self):
        # Usa self.lista em vez de self.jogos
        jogos_formatados = ", ".join(self.lista) if self.lista else "Nenhum"

        print("┌" + "─" * 38 + "┐")
        print(f"│ {'FICHA DO GAMER':^36} │")
        print("├" + "─" * 38 + "┤")
        print(f"│ Nome       : {self.nome:<23} │")
        print(f"│ Nick       : {self.nick:<23} │")
        print(f"│ Plataforma : {self.plataforma:<23} │")
        print(f"│ Total Jogos: {len(self.lista):<23} │")
        print("├" + "─" * 38 + "┤")
        print(f"│ Jogos      : {jogos_formatados:<23} │")
        print("└" + "─" * 38 + "┘")
        
#Exemplo:

jogador = Gamer('Anderson','Derson_003')
jogador.add_jogo('God of War','Minecraft',)
jogador.exibir_ficha()
