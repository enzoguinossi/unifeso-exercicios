class ConversorDistancia:

    def __init__(self, km):
        self.km = km

    def para_metros(self):
        return self.km * 1000

    def para_centimetros(self):
        return self.km * 100000


def main():
    km = float(input("Digite a distância em km: "))

    conversor = ConversorDistancia(km)

    print("Metros:", conversor.para_metros())
    print("Centímetros:", conversor.para_centimetros())


if __name__ == "__main__":
    main()