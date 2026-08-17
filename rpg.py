class Personagem:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def atacar(self):
        print(f"\n{self.nome} realiza um ataque genérico.\n")


class Guerreiro(Personagem):
    def __init__(self, nome, nivel, forca):
        super().__init__(nome, nivel)
        self.forca = forca

    def atacar(self):
        print(f"\n{self.nome} ataca com sua espada! (Força: {self.forca})\n")


class Mago(Personagem):
    def __init__(self, nome, nivel, mana):
        super().__init__(nome, nivel)
        self.mana = mana

    def atacar(self):
        print(f"\n{self.nome} lança uma bola de fogo! (Mana: {self.mana})\n")



def main():
    personagem = Personagem("Aventureiro", 1)
    guerreiro = Guerreiro("Darius", 5, 90)
    mago = Mago("Gandalf", 10, 100)

    lista_personagens = [personagem, guerreiro, mago]

    print("\n---Ação dos Personagens---")
    for p in lista_personagens:
        p.atacar()


if __name__ == "__main__":
    main()