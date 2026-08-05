class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco

    def set_quantidade(self, quantidade):
        if quantidade >= 0:
            self.__quantidade = quantidade

    def calcular_totalp(self):
        return self.__preco * self.__quantidade


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto.get_nome().lower() == nome.lower():
                self.produtos.remove(produto)
                return True
        return False

    def listar_produtos(self):
        if not self.produtos:
            print("\nCarrinho vazio.\n")
        else:
            print("\nProdutos no carrinho: ")
            for produto in self.produtos:
                print(f"Produto: {produto.get_nome()} | Preço: {produto.get_preco()} | Quantidade: {produto.get_quantidade()}")
            print()

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.calcular_totalp()
        return total


def main():
    carrinho = CarrinhoDeCompras()

    while True:
        print("\n===Menu do Carrinho===")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Calcular total")
        print("5. Sair")

        opcao = input("\nEscolha uma opção (1-5): ")

        if opcao == "1":
            nome = input("\nNome do produto: ")
            preco = float(input("Preço: R$ "))
            quantidade = int(input("Quantidade: "))

            produto = Produto(nome, preco, quantidade)

            carrinho.adicionar_produto(produto)

            print("\nProduto adicionado no carrinho com sucesso!\n")

        elif opcao == "2":
            nome = input("\nNome do produto a remover: ")

            if carrinho.remover_produto(nome):
                print("\nProduto removido com sucesso!\n")
            else:
                print("\nProduto não encontrado.\n")

        elif opcao == "3":
            carrinho.listar_produtos()

        elif opcao == "4":
            total = carrinho.calcular_total()
            print(f"\nTotal da compra: R$ {total:.2f}\n")

        elif opcao == "5":
            print("\nEncerrando o programa...\n")
            break

        else:
            print("\nOpção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()
