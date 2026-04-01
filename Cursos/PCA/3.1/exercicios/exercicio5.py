class Numero(float):
    @property
    def sinal(self):
        if self > 0:
            return "positivo"
        elif self < 0:
            return "negativo"
        else:
            return "neutro"

def main():
    numero = Numero(float(input("Digite o número à ser checado: ")))
    print(f"O numero {numero} é {numero.sinal}")

main()