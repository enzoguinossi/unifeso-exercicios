import re

class Aluno:
    def __init__(self, nome: str, nota: str | int | float):
        self.nome:str = self._tratar_nome(nome)
        self.nota:float = self._tratar_nota(nota)

    def _tratar_nota(self, texto: str | float | int) -> float:
        if isinstance(texto, (int, float)):
            return float(texto)
        
        texto = texto.strip()
        texto = texto.replace('.', '')  
        texto = texto.replace(',', '.')
        texto = re.sub(r'[^0-9.]', '', texto)

        if not texto:
            raise ValueError("Nota inválida")
        return float(texto)

    def _tratar_nome(self, texto: str) -> str:
        texto = texto.strip()
        if not texto:
            raise ValueError("Nome não pode ser vazio")
        texto = texto.title()
        return texto

    @property
    def situacao(self) -> str:
        if(self.nota < 4):
            return "Reprovado"
        elif(self.nota < 7):
            return "Recuperação"
        else: 
            return "Aprovado"



def main() -> None:
    nome_aluno: str = input("Digite o nome do aluno:")
    while True:
        nota_aluno: str = input("Digite a nota final do aluno:")
        try:
            aluno: Aluno = Aluno(nome_aluno,nota_aluno)
            break
        except ValueError:
            print("Valor inválido! Tente novamente.")
            
    print(f"A situação do aluno {aluno.nome} é {aluno.situacao}")

main()