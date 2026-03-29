class Caixa:
    def __init__(self, comprimento, largura, altura):
        self.comprimento = comprimento
        self.largura = largura
        self.altura = altura

    def calcular_volume(self):
        return self.comprimento * self.largura * self.altura


def main():
    comprimento = float(input("Digite o comprimento: "))
    largura = float(input("Digite a largura: "))
    altura = float(input("Digite a altura: "))

    caixa = Caixa(comprimento, largura, altura)

    print("Volume da caixa:", caixa.calcular_volume())


if __name__ == "__main__":
    main()