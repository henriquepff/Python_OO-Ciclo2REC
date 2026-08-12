class Casa:
    class __Comodo:
        def __init__(self, nome, area):
            self.__nome = nome
            self.__area = area

        def get_nome(self):
            return self.__nome

        def get_area(self):
            return self.__area

        def set_nome(self, nome):
            self.__nome = nome

        def set_area(self, area):
            if area > 0:
                self.__area = area
            else:
                print("\nA área deve ser um número positivo.\n")

    def __init__(self):
        self.__comodos = []

    def adicionar_comodo(self, nome, area):
        comodo = self.__Comodo(nome, area)
        self.__comodos.append(comodo)

    def listar_comodos(self):
        if not self.__comodos:
            print("\nNenhum cômodo foi adicionado ainda.\n")
        else:
            print("\nCômodos da casa: ")
            for comodo in self.__comodos:
                print(f"- {comodo.get_nome()} ({comodo.get_area()} m²)")
            print()

    def calcular_area_total(self):
        total = 0
        for comodo in self.__comodos:
            total += comodo.get_area()
        return total


def main():
    casa = None

    while True:
        print("\n====MENU====")
        print("1. Criar nova casa")
        print("2. Adicionar cômodo")
        print("3. Listar cômodos")
        print("4. Calcular área total")
        print("5. Sair")

        opcao = input("\nEscolha uma opção (1-5): ")

        if opcao == "1":
            if casa is None:
                casa = Casa()
                print("\nCasa criada com sucesso\n")
            else:
                print("\nA casa já foi criado. Só é possível criar uma casa.\n")

        elif opcao == "2":
            if casa is None:
                print("\nCrie a casa primeiro.\n")
            else:
                nome = input("\nNome do cômodo: ")
                area = float(input("Área do cômodo (m²): "))

                casa.adicionar_comodo(nome, area)

                print("\nCômodo adicionado com sucesso.\n")

        elif opcao == "3":
            if casa is None:
                print("\nCrie a casa primeiro.\n")
            else:
                casa.listar_comodos()
            

        elif opcao == "4":
            if casa is None:
                print("\nCrie a casa primeiro.\n")
            else:
                total = casa.calcular_area_total()
                print(f"\nÁrea total da casa: {total:.2f} m²\n")

            
        elif opcao == "5":
            print("\nEncerrando o programa...\n")
            break

        else:
            print("\nOpção inválida! Tente novamente.\n")



if __name__ == "__main__":
    main()