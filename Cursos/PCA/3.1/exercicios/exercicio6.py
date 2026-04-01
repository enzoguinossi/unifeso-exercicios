import re
from typing import List

class Comparador:
    def __init__(self, numeros_texto: List[str]) -> None:
        self.__numeros: List[float] = [self._tratar_valor(n) for n in numeros_texto]

    def _tratar_valor(self, texto: str) -> float:
        limpo = texto.strip().replace(',', '.')
        # Permite dígitos, ponto decimal e sinal de menos
        limpo = re.sub(r'[^0-9.-]', '', limpo)
        
        try:
            return float(limpo)
        except ValueError:
            raise ValueError(f"Valor '{texto}' inválido.")

    @property
    def numeros(self) -> List[float]:
        return self.__numeros

    @property
    def resultado_comparacao(self) -> str:
        if len(self.__numeros) < 2:
            return "Quantidade insuficiente de números para comparar."
        
        n1, n2 = self.__numeros[0], self.__numeros[1]
        
        if n1 == n2:
            return "Ambos os números são iguais."
        elif n1 > n2:
            return f"O número {n1} é maior que {n2}."
        return f"O número {n2} é maior que {n1}."

def main() -> None:
    try:
        entradas: List[str] = []
        for i in range(2):
            entradas.append(input(f"Digite o número {i + 1} a ser analisado: "))
        
        comparador: Comparador = Comparador(entradas)
        print(comparador.resultado_comparacao)
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
