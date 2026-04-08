import math
import sys


class ClassificadorNumero:
    @staticmethod
    def e_primo(numero: int):
        if numero <= 1:
            return False

        for i in range(2, int(math.sqrt(numero)) + 1):
            if numero % i == 0:
                return False

        return True

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

            print(f"\nNúmeros primos até {n}\n")

            for i in range(2, n+1, +1):
                if ClassificadorNumero.e_primo(i):
                    print(i)
            sys.exit()

        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()