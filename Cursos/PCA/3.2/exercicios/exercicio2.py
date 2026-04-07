class Contador:
    @staticmethod
    def contar(intervalo: str):
        try:
            intervalo = int(intervalo)
        except ValueError:
            raise ValueError("Valor inválido.")

        i : int = 0
        while i < intervalo:
            print(i + 1)
            i += 1

def main() -> None:
    entrada: str = input("Escreva a quantidade de números à serem contados: ")
    try:
        Contador.contar(entrada)
    except ValueError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()