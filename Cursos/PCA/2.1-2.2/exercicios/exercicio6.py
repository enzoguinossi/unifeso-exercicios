class ConversorMoeda:

    def __init__(self, valor_brl, taxa):
        self.valor_brl = valor_brl
        self.taxa = taxa

    def converter(self):
        return self.valor_brl / self.taxa


def main():
    valor = float(input("Digite o valor em reais: "))
    taxa = float(input("Digite a cotação do dólar: "))

    conversor = ConversorMoeda(valor, taxa)

    print("Valor em dólares:", conversor.converter())


if __name__ == "__main__":
    main()