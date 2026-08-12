class Funcionario:
    def __init__(self, nome, salariob):
        self.nome = nome
        self.salariob = salariob

    def calcular_salario(self):
        return self.salariob

    def exibir_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Salário: R$ {self.salariob:.2f}")



class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, salariob, comissao):
        super().__init__(nome, salariob)
        self.comissao = comissao

    def calcular_salario(self):
        return self.salariob + self.comissao

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Comissão: R$ {self.comissao:.2f}")
        print(f"Salário Total: R$ {self.calcular_salario():.2f}")


def main():
    func1 = Funcionario("Maria", 3000)
    func2 = FuncionarioComissionado("João", 2500, 800)

    func1.exibir_dados()
    print("---------------------")
    func2.exibir_dados()
    print()



if __name__ == "__main__":
    main()