import re

class Aluno:
    def __init__(self, nome: str, nota_texto: str) -> None:
        self.__nome: str = self._tratar_nome(nome)
        self.__nota: float = self._tratar_nota(nota_texto)

    def _tratar_nota(self, texto: str) -> float:
        limpo = texto.strip().replace(',', '.')
        limpo = re.sub(r'[^0-9.]', '', limpo)
        
        if not limpo:
            raise ValueError("Nota inválida.")
        
        valor = float(limpo)
        if not (0 <= valor <= 10):
            raise ValueError("Nota deve estar entre 0 e 10.")
        return valor

    def _tratar_nome(self, texto: str) -> str:
        limpo = texto.strip().title()
        if not limpo:
            raise ValueError("Nome não pode ser vazio.")
        return limpo

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def nota(self) -> float:
        return self.__nota

    @property
    def situacao(self) -> str:
        if self.__nota < 4:
            return "Reprovado"
        elif self.__nota < 7:
            return "Recuperação"
        return "Aprovado"

def main() -> None:
    try:
        nome_entrada: str = input("Digite o nome do aluno: ")
        nota_entrada: str = input("Digite a nota final do aluno: ")
        
        aluno: Aluno = Aluno(nome_entrada, nota_entrada)
        print(f"A situação do aluno {aluno.nome} é {aluno.situacao} (Nota: {aluno.nota})")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
