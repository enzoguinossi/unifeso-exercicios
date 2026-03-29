class MediaNotas:

    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def calcular_media(self):
        return (self.n1 + self.n2 + self.n3) / 3


def main():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))

    media = MediaNotas(n1, n2, n3)

    print("Média:", media.calcular_media())


if __name__ == "__main__":
    main()