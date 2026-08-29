from rich import print


class Arquivo:

    def __init__(self, nome: str, bytes: int):
        self.name = nome
        self.bytes = bytes
        self._extensao = "arquivo"
        self._programa = "programa padrão"

    @property
    def mb(self) -> float:
        return self.bytes / 1000000

    @property
    def nome_completo(self) -> str:
        return f'"{self.name}.{self._extensao}" {self.mb:.2f}MB'

    def abrir(self):
        print("Abrindo o Arquivo Padrão")


class Pdf(Arquivo):

    def __init__(self, nome, bytes):
        super().__init__(nome=nome, bytes=bytes)
        self._extensao = "pdf"
        self._programa = "Adobe Reader"

    def abrir(self):
        print(
            f'Abrindo o Arquivo "{self.name}.{self._extensao}" ({self.mb:.2f}MB) no {self._programa}'
        )


class Doc(Arquivo):

    def __init__(self, nome, bytes):
        super().__init__(nome=nome, bytes=bytes)
        self._extensao = "docx"
        self._programa = "Microsoft Word"

    def abrir(self):
        print(
            f'Abrindo o Arquivo "{self.name}.{self._extensao}" ({self.mb:.2f}MB) no {self._programa}'
        )


arquivo1 = Pdf("contrato", 250000)
arquivo2 = Doc("prova", 1300000)


def abrir_arquivo(obj):
    try:
        obj.abrir()
    except Exception as e:
        print(f"Não foi possível abrir! Erro: {e}")


abrir_arquivo(arquivo1)
abrir_arquivo(arquivo2)

# Testando:
print(arquivo1.nome_completo)
print(arquivo2.nome_completo)