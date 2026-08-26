from abc import ABC, abstractmethod

class VeiculoTransporte(ABC):
    def __init__(self, placa, capacidade):
        self.placa = placa
        self.capacidade = capacidade

    @abstractmethod
    def calcular_custo(self):
        pass


class Onibus(VeiculoTransporte):
    def __init__(self, placa, capacidade, consumo_km):
        super().__init__(placa, capacidade)
        self.consumo_km = consumo_km

    def calcular_custo(self):
        return self.consumo_km * 6.00


class Metro(VeiculoTransporte):
    def __init__(self, placa, capacidade, consumo_energia_km):
        super().__init__(placa, capacidade)
        self.consumo_energia_km = consumo_energia_km

    def calcular_custo(self):
        return self.consumo_energia_km * 0.80


def main():

    veiculos = []

    while True:
        print("\n===MENU===")
        print("1. Cadastrar Ônibus"),
        print("2. Cadastrar Metrô")
        print("3. Mostrar custos operacionais")
        print("4. Sair")

        opcao = input("\nEscolha uma opção (1-4): ")

        if opcao == "1":
            print("\nCadastro de Ônibus: ")

            try:
                placa = input("Placa: ").strip()

                if placa == "":
                    raise ValueError("A placa não pode estar vazia.")

                capacidade = int(input("Capacidade de passageiros: "))

                if capacidade <= 0:
                    raise ValueError("A capacidade deve ser positiva.")

                consumo = float(input("Consumo por km (litros/km): "))

                if consumo <= 0:
                    raise ValueError("O consumo deve ser positivo.")

                veiculos.append(Onibus(placa, capacidade, consumo))

                print("\nÔnibus cadastrado com sucesso!\n")

            except ValueError as e:
                print(f"\nErro: {e}\n")

        elif opcao == "2":
            print("\nCadastro de Metrô: ")
            
            try:
                placa = input("Identificação: ").strip()
            
                if placa == "":
                    raise ValueError("A identificação não pode estar vazia.")
            
                capacidade = int(input("Capacidade de passageiros: "))
            
                if capacidade <= 0:
                    raise ValueError("A capacidade deve ser positiva.")
            
                consumo = float(input("Consumo por km (kWh/km): "))
            
                if consumo <= 0:
                    raise ValueError("O consumo deve ser positivo.")
            
                veiculos.append(Metro(placa, capacidade, consumo))
            
                print("\nMetrô cadastrado com sucesso!\n")
            
            except ValueError as e:
                print(f"\nErro: {e}\n")

        elif opcao == "3":
            if not veiculos:
                print("\nNenhum veículo cadastrado.\n")
            else:
                print("\n---Custos Operacionais por KM---")
                for v in veiculos:
                    tipo = "Ônibus" if isinstance(v, Onibus) else "Metrô"
                    custo = v.calcular_custo()
                    print(f"{tipo} {v.placa}: R$ {custo:.2f} por km")
                print()


        elif opcao == "4":
            print("\nEncerrando o sistema...\n")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")



if __name__ == "__main__":
    main()


