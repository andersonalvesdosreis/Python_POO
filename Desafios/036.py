class Pagamento:
    def __init__(self,vlr:int|float):
        self._valor = vlr

class Boleto(Pagamento):
    def pagar(self):
        print(f'Pagamento COMFIRMADO de R${self._valor} via Boleto!')

class Pix(Pagamento):
    def pagar(self):
        print(f'Pagamento COMFIRMADO de R${self._valor} via Pix!')

class Credito(Pagamento):
    def pagar(self):
        print(f'Pagamento COMFIRMADO de R${self._valor} via Cartão de Crédito!')

#Duck Typing

def finalizar_compra(classe, valor):
    try:
        pagamento1 = classe(valor)
        return pagamento1.pagar()
    except Exception as e:
        print(f"Não foi possível realizar o pagamento! Erro: {e}")

finalizar_compra(Boleto,2000)
finalizar_compra(Pix,4000)
finalizar_compra(Credito,90231)
