import re

class Temperatura:
    def __init__(self, temperatura: str):
        self.temperatura = self._tratar_temperatura(temperatura)

    def _tratar_temperatura(self, texto: str | float | int) -> float:
        if isinstance(texto, (int, float)):
                return float(texto)
            
        texto = texto.strip()
        texto = texto.replace('.', '')  
        texto = texto.replace(',', '.')
        texto = re.sub(r'[^0-9.]', '', texto)

        if not texto:
            raise ValueError("Nota inválida")
        return float(texto)
    
    @property
    def classificacao(self):
        if self.temperatura < 15:
            return "Frio"
        elif self.temperatura < 25:
            return "Agradável"
        else:
            return "Quente"

def main():
    temperatura = input("Escreva a temperatura à ser analisada: ")

    t: Temperatura = Temperatura(temperatura)

    print(f"O clima está {t.classificacao}")

main()