class ConversorTemperatura:

    def __init__(self, celsius):
        self.celsius = celsius

    def converter(self):
        return self.celsius * 1.8 + 32


def main():
    c = float(input("Digite a temperatura em Celsius: "))

    conversor = ConversorTemperatura(c)

    print("Temperatura em Fahrenheit:", conversor.converter())


if __name__ == "__main__":
    main()