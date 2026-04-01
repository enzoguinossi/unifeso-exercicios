from typing import List

def main():
    numeros: List[float] = []
    for i in range(2):
        numero = float(input(f"Digite o número {i + 1} à ser analisado: "))
        numeros.append(numero)

    if numeros[0] == numeros[1]:
        print("Ambos os números são iguaís")
    elif numeros[0] > numeros[1]:
        print(f"O número {numeros[0]} é maior que {numeros[1]}")
    else:
        print(f"O número {numeros[1]} é maior que {numeros[0]}")

main()