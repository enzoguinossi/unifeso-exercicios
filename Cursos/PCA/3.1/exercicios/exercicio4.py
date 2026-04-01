import re

class Residencia:
    def __init__(self, consumo_texto: str) -> None:
        self.__consumo: float = self._tratar_consumo(consumo_texto)

    def _tratar_consumo(self, texto: str) -> float:
        limpo = texto.strip().replace(',', '.')
        limpo = re.sub(r'[^0-9.]', '', limpo)
        
        if not limpo:
            raise ValueError("Valor de consumo inválido.")
        
        valor = float(limpo)
        if valor < 0:
            raise ValueError("Consumo não pode ser negativo.")
        return valor

    @property
    def consumo(self) -> float:
        return self.__consumo

    @property
    def classificacao(self) -> str:
        if self.__consumo < 100:
            return "Baixo"
        elif self.__consumo < 200:
            return "Médio"
        return "Alto"

def main() -> None:
    try:
        consumo_input: str = input("Digite o consumo de energia em kwH: ")
        residencia: Residencia = Residencia(consumo_input)
        print(f"Consumo: {residencia.consumo} kWh")
        print(f"Classificação: {residencia.classificacao}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
