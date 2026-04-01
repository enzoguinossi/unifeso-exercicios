import re

class Residencia:
    def __init__(self, consumo: str) -> None:
        self.consumo: float = self._tratar_consumo(consumo)

    def _tratar_consumo(self, texto: str | float | int) -> float:
        if isinstance(texto, (int, float)):
            return float(texto)
        
        texto = texto.strip()
        texto = texto.replace('.', '')  
        texto = texto.replace(',', '.')
        texto = re.sub(r'[^0-9.]', '', texto)

        if not texto:
            raise ValueError("Valor de consumo inválido")
        return float(texto)
    
    @property
    def classificacao(self) -> str:
        if self.consumo < 100:
            return "Baixo"
        elif self.consumo < 200:
            return "Médio"
        else:
            return "Alto"

def main():
    consumo_input = input("Digite o consumo de energia em kwH: ")
    residencia = Residencia(consumo_input)
    print(f"Consumo: {residencia.consumo} kWh")
    print(f"Classificação: {residencia.classificacao}")

main()