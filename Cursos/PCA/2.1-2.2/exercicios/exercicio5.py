class Retangulo:

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)


def main():
    largura = float(input("Digite a largura: "))
    altura = float(input("Digite a altura: "))

    r = Retangulo(largura, altura)

    print("Área:", r.area())
    print("Perímetro:", r.perimetro())


if __name__ == "__main__":
    main()