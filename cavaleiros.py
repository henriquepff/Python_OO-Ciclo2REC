class Personagem:
    def __init__(self, nome, constelacao):
        self.nome = nome
        self.constelacao = constelacao

    def apresentar(self):
        print(f"{self.nome}, cavaleiro da constelação de {self.constelacao}.")


class CavaleiroBronze(Personagem):
    def __init__(self, nome, constelacao, poder_luta):
        super().__init__(nome, constelacao)
        self.poder_luta = poder_luta

    def golpe_especial(self):
        print(f"\n{self.nome} executa seu golpe especial com poder de luta {self.poder_luta}!\n")


class CavaleiroOuro(Personagem):
    def __init__(self, nome, constelacao, casa_zoodiaco):
        super().__init__(nome, constelacao)
        self.casa_zoodiaco = casa_zoodiaco

    def defender_casa(self):
        print(f"\n{self.nome} defende a casa de {self.casa_zoodiaco} com honra!\n")



class CavaleiroHibrido(CavaleiroBronze, CavaleiroOuro):
    def __init__(self, nome, constelacao, poder_luta, casa_zoodiaco):
        self.nome = nome
        self.constelacao = constelacao
        self.poder_luta = poder_luta
        self.casa_zoodiaco = casa_zoodiaco

    def golpe_especial(self):
        print(f"\n{self.nome} realiza um golpe híbrido com poder de luta {self.poder_luta}!\n")

    def defender_casa(self):
        print(f"\n{self.nome} protege a casa de {self.casa_zoodiaco} com poder total!\n")


def main():
    personagens = []

    while True:
        print("\n==========MENU===========")
        print("1- Cadastrar cavaleiro")
        print("2- Listar personagens")
        print("3- Executar habilidades")
        print("4- Sair")

        opcao = input("\nEscolha uma opção (1-4): ")

        if opcao == "1":
            print("\nTipo de cavaleiro: ")
            print("1. Cavaleiro de Bronze")
            print("2. Cavaleiro de Ouro")
            print("3. Cavaleiro Híbrido")

            tipo = input("\nTipo: ")

            if tipo == "1":
                nome = input("\nNome: ")
                constelacao = input("Constelação: ")
                poder = input("Poder de luta: ")

                personagem = CavaleiroBronze(nome, constelacao, poder)

            elif tipo == "2":
                nome = input("\nNome: ")
                constelacao = input("Constelação: ")
                casa = input("Casa do Zoodíaco: ")
                
                personagem = CavaleiroOuro(nome, constelacao, casa)

            elif tipo == "3":
                nome = input("\nNome: ")
                constelacao = input("Constelação: ")
                poder = input("Poder de luta: ")
                casa = input("Casa do Zoodíaco: ")
                                
                personagem = CavaleiroHibrido(nome, constelacao, poder, casa)

            else:
                print("\nTipo inválido!\n")
                continue

            personagens.append(personagem)

            print("\nCavaleiro cadastrado com sucesso.\n")

        elif opcao == "2":
            if not personagens:
                print("\nNenhum personagem cadastrado.\n")
            else:
                print("\n---Personagens---")
                for p in personagens:
                    p.apresentar()
                print()

        elif opcao == "3":
            if not personagens:
                print("\nNenhum personagem cadastrado.\n")
            else:
                print("\n---Habilidades---")
                for p in personagens:
                    print(f"\n{p.nome}: ")
                    if isinstance(p, CavaleiroBronze):
                        p.golpe_especial()
                    if isinstance(p, CavaleiroOuro):
                        p.defender_casa()
            
                        
        elif opcao == "4":
            print("\nEncerrando programa...\n")
            break
        else:
            print("\nOpção inválida!\n")


if __name__ == "__main__":
    main()
