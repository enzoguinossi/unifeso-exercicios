import re

class Numero:
    def __init__(self, valor_texto: str) -> None:
        self.__valor: float = self._tratar_valor(valor_texto)

    def _tratar_valor(self, texto: str) -> float:
        limpo = texto.strip().replace(',', '.')
        # Permite dígitos, ponto decimal e sinal de menos
        limpo = re.sub(r'[^0-9.-]', '', limpo)
        
        try:
            return float(limpo)
        except ValueError:
            raise ValueError("Valor numérico inválido.")

    @property
    def valor(self) -> float:
        return self.__valor

    @property
    def sinal(self) -> str:
        if self.__valor > 0:
            return "positivo"
        elif self.__valor < 0:
            return "negativo"
        return "neutro"

def main() -> None:
    try:
        entrada: str = input("Digite o número a ser checado: ")
        numero_obj: Numero = Numero(entrada)
        print(f"O número {numero_obj.valor} é {numero_obj.sinal}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
