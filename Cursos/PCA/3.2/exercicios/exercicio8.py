from typing import Generator


class Fibonacci:
    @staticmethod
    def gerar_sequencia_ate(intervalo : int) -> Generator[int]:
        a, b = 0,1
        for i in range(intervalo):
            yield a
            a, b = b, a + b

def main() -> None:
    n: int
    while True:
        try:
            while True:
                try:
                    n = int(input("Digite um número inteiro positivo: "))
                    break
                except ValueError:
                    print("Por favor, digite um número inteiro válido.")

            if n <= 0:
                raise ValueError("O número deve ser positivo!")

            print(f"\nSequência de Fibonacci até {n}\n")

            for numero in Fibonacci.gerar_sequencia_ate(n):
                print(numero)
            break

        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()