class Pessoa:
    def __init__(self, nome: str, idade_texto: str) -> None:
        self.__nome: str = self._tratar_nome(nome)
        self.__idade: int = self._tratar_idade(idade_texto)

    def _tratar_nome(self, texto: str) -> str:
        limpo = texto.strip().title()
        if not limpo:
            raise ValueError("Nome não pode ser vazio.")
        return limpo

    def _tratar_idade(self, texto: str) -> int:
        limpo = texto.strip()
        if not limpo:
            raise ValueError("Idade não pode ser vazia.")
        try:
            idade = int(limpo)
            if idade < 0:
                raise ValueError("Idade não pode ser negativa.")
            return idade
        except ValueError:
            raise ValueError("Idade inválida.")

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def tipo_ingresso(self) -> str:
        if self.__idade < 12:
            return "Meia Infantil"
        elif self.__idade < 18:
            return "Meia Estudantil"
        elif self.__idade < 60:
            return "Inteira"
        return "Meia Idoso"

def main() -> None:
    try:
        nome_entrada: str = input("Digite o nome: ")
        idade_entrada: str = input("Digite a idade: ")

        pessoa: Pessoa = Pessoa(nome_entrada, idade_entrada)
        print(f"Pessoa: {pessoa.nome}, Tipo de Ingresso: {pessoa.tipo_ingresso}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
