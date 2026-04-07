import sys


class Autenticador:
    def __init__(self, usuario_correto: str = "admin", senha_correta: str = "senha123") -> None:
        self.__usuario_correto: str = usuario_correto
        self.__senha_correta: str = senha_correta

    def autenticar(self, usuario: str, senha: str) -> bool:
        return usuario == self.__usuario_correto and senha == self.__senha_correta

class AppLoginCLI:
    def __init__(self) -> None:
        self.__autenticador: Autenticador = Autenticador()

    def executar(self) -> None:
        for _ in range(3):
            usuario_input: str = input("Digite o nome de usuário: ").strip()
            senha_input: str = input("Digite a senha: ").strip()

            if self.__autenticador.autenticar(usuario_input, senha_input):
                print("\nLogin realizado com sucesso!")
                sys.exit(0)
            else:
                if not _ == 2:
                    print("\nUsuário ou senha incorretos. Tente novamente.\n")
        print("\nAcesso bloqueado. Muitas tentativas incorretas.\n")

def main() -> None:
    app: AppLoginCLI = AppLoginCLI()
    app.executar()

if __name__ == "__main__":
    main()