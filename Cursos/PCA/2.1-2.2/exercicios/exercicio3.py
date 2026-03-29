class SomaLista:

    def __init__(self):
        self.numeros = []

    def adicionar_numero(self, numero):
        self.numeros.append(numero)

    def calcular_soma(self):
        return sum(self.numeros)


def main():
    lista = SomaLista()

    for i in range(3):
        num = float(input(f"Digite o {i+1}º número: "))
        lista.adicionar_numero(num)

    print("Soma dos números:", lista.calcular_soma())


if __name__ == "__main__":
    main()