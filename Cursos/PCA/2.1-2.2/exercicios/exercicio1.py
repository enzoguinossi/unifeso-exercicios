class Calculadora:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        return self.num1 + self.num2

    def subtracao(self):
        return self.num1 - self.num2

    def multiplicacao(self):
        return self.num1 * self.num2

    def divisao(self):
        if self.num2 == 0:
            return "Divisão por zero não permitida"
        return self.num1 / self.num2


def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    calc = Calculadora(num1, num2)

    print("Soma:", calc.soma())
    print("Subtração:", calc.subtracao())
    print("Multiplicação:", calc.multiplicacao())
    print("Divisão:", calc.divisao())


if __name__ == "__main__":
    main()