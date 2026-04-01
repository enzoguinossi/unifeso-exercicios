import re

class Temperatura:
    def __init__(self, valor_texto: str) -> None:
        self.__valor: float = self._validar_e_tratar(valor_texto)

    def _validar_e_tratar(self, texto: str) -> float:
        limpo = texto.strip().replace(',', '.')

        limpo = re.sub(r'[^0-9.-]', '', limpo)
        
        try:
            return float(limpo)
        except ValueError:
            raise ValueError("Valor de temperatura inválido.")

    @property
    def valor(self) -> float:
        return self.__valor

    @property
    def classificacao(self) -> str:
        if self.__valor < 15:
            return "Frio"
        elif self.__valor < 25:
            return "Agradável"
        return "Quente"

def main() -> None:
    entrada: str = input("Escreva a temperatura a ser analisada: ")
    try:
        temp: Temperatura = Temperatura(entrada)
        print(f"O clima está {temp.classificacao} ({temp.valor}°C)")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
