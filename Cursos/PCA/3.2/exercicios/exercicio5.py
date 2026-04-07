from typing import List


class ColecaoNumeros:
    def __init__(self) -> None:
        self.__numeros: List[int] = []

    def adicionar(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("Apenas números inteiros positivos são permitidos.")
        self.__numeros.append(valor)
    @property
    def soma_total(self) -> int:
        return sum(self.__numeros)


class AppSomaCLI:
    def __init__(self) -> None:
        self.__colecao: ColecaoNumeros = ColecaoNumeros()

    def executar(self) -> None:
        print("--- SOMADOR DE NÚMEROS POSITIVOS ---")
        print("Digite '0' para encerrar e ver a soma.\n")

        while True:
            entrada: str = input("Digite um número inteiro positivo: ").strip()

            try:
                numero: int = int(entrada)

                if numero == 0:
                    break

                self.__colecao.adicionar(numero)
            except ValueError as e:
                if "invalid literal for int()" in str(e):
                    print("Erro: Por favor, digite um número inteiro válido.")
                else:
                    print(f"Erro: {e}")
        print(f"\nA soma total dos números digitados é: {self.__colecao.soma_total}")

def main() -> None:
    app: AppSomaCLI = AppSomaCLI()
    app.executar()

if __name__ == "__main__":
    main()

