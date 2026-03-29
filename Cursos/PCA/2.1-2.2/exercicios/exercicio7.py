class Produto:
    def __init__(self, preco, desconto, imposto):
        self.preco = preco
        self.desconto = desconto
        self.imposto = imposto

    def calcular_preco_final(self):
        valor_desconto = self.preco * (self.desconto / 100)
        valor_imposto = self.preco * (self.imposto / 100)
        return self.preco - valor_desconto + valor_imposto


def main():
    preco = float(input("Digite o preço do produto: "))
    desconto = float(input("Digite o desconto (%): "))
    imposto = float(input("Digite o imposto (%): "))

    produto = Produto(preco, desconto, imposto)

    print("Preço final:", produto.calcular_preco_final())


if __name__ == "__main__":
    main()