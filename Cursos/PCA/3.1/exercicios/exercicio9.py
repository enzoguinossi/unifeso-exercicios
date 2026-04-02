class Compra:
    def __init__(self, valor: str) -> None:
        self.__valor: float = self._tratar_valor(valor)
        self.__desconto: float = self._tratar_desconto()
        self.__valor_liquido: float = self._calcular_valor_liquido()

    def _tratar_valor(self, valor: str) -> float:
        valor = valor.replace(".", "").replace(",", ".").strip()
        if not valor:
            raise ValueError("Valor não pode ser vazio.")
        try:
            return float(valor)
        except ValueError:
            raise ValueError("Valor inválido!")

    def _tratar_desconto(self) -> float:
        desconto = 0
        if self.__valor > 100:
            desconto = self.__valor * 0.1
        return desconto


    def _calcular_valor_liquido(self) -> float:
        if not self.__desconto:
            return self.__valor
        return self.__valor - self.__desconto

    @property
    def valor(self) -> float:
        return self.__valor

    @property
    def desconto(self) -> float:
        return self.__desconto

    @property
    def valor_liquido(self) -> float:
        return self.__valor_liquido

def main() -> None:
    try:
        valor_input: str = input("Digite o valor da compra: ")
        compra: Compra = Compra(valor_input)
        print(f"Valor da compra: R$ {compra.valor:.2f}")
        print(f"Desconto: R$ {compra.desconto:.2f}")
        print(f"Valor líquido: R$ {compra.valor_liquido:.2f}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()