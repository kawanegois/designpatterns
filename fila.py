from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def imprimir_documento(self, documento):
        pass


class Fila:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance._fila = []
            cls.__instance._strategy = FirstComeFirstServedStrategy()
        return cls.__instance

    def __init__(self):
        pass

    def imprimir_documento(self, documento):
        self._strategy.imprimir_documento(documento)

    def remover_documento(self):
        documento = self._fila.pop(0)
        self._strategy.remover_documento(documento)

    def remover_todos_documentos(self):
        self._fila.clear()
        self._strategy.remover_todos_documentos()


class FirstComeFirstServedStrategy(Strategy):
    def imprimir_documento(self, documento):
        print(f"Imprimindo documento {documento} na ordem de chegada")

    def remover_documento(self, documento):
        print(f"Removendo documento {documento} na ordem de chegada")

    def remover_todos_documentos(self):
        print("Removendo todos os documentos na ordem de chegada")


if __name__ == "__main__":
    fila = Fila()
    documentos = ["documento 1", "documento 2", "documento 3"]
    for documento in documentos:
        fila.imprimir_documento(documento)
    fila.remover_todos_documentos()
