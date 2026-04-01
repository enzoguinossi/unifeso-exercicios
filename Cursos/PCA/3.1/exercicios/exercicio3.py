class Pessoa:
    def __init__(self, nome: str, idade: str):
        self.nome = nome.strip().title()
        self.idade: int = self._tratar_idade(idade)

    def _tratar_idade(self, texto: str):
        if isinstance(texto, int):
            return texto
        if not texto:
            raise ValueError("Idade não pode ser vazia!")
        try:
            return int(texto)
        except ValueError:
            raise ValueError("Idade inválida")

    @property
    def tipo_ingresso(self) -> str:
        if (self.idade < 12):
            return "meia infantil"
        elif(self.idade < 18):
            return "meia estudantil"
        elif(self.idade < 60):
            return "inteira"
        else:
            return "meia idoso"

def main() -> None:
    while True:
        nome = input("Digite o nome: ")
        if not nome.strip():
            print("Nome não pode ser vazio!")
            continue

        idade = input("Digite a idade: ")

        try:
            pessoa = Pessoa(nome, idade)
            break
        except ValueError as e:
            print(e)

    print(f"Pessoa: {pessoa.nome}, Tipo de Ingresso: {pessoa.tipo_ingresso}")

if __name__ == "__main__":    
    main()