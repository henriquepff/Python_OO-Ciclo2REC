class Livro:
    def __init__(self, titulo, autor, id_livro):
        self.__titulo = titulo
        self.__autor = autor
        self.__id_livro = id_livro

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_id_livro(self):
        return self.__id_livro

    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    def set_autor(self, novo_autor):
        self.__autor = novo_autor

    def set_id_livro(self, novo_id_livro):
        self.__id_livro = novo_id_livro

class Usuario:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__livros_emprestados = []

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula

    def emprestar_livro(self, livro):
        self.__livros_emprestados.append(livro)
        print(f"\n{self.__nome} pegou emprestado o livro '{livro.get_titulo()}'.\n")

    def devolver_livro(self, id_livro):
        for livro in self.__livros_emprestados:
            if livro.get_id_livro() == id_livro:
                self.__livros_emprestados.remove(livro)
                print(f"\n{self.__nome} devolveu o livro '{livro.get_titulo()}'.\n")
                return
        print(f"\n{self.__nome} não possui um livro com o ID {id_livro}.\n")

    def listar_livros_emprestados(self):
        if not self.__livros_emprestados:
            print("\nNenhum livro emprestado.\n")
        else:
            print("\nLivros emprestados: ")
            for livro in self.__livros_emprestados:
                print(f"- {livro.get_titulo()} ({livro.get_id_livro()})")
            print()

def main():
    livros = []
    usuarios = []

    while True:
        print("\n==========BIBLIOTECA===========")
        print("1- Cadastrar livro")
        print("2- Cadastrar usuário")
        print("3- Emprestar livro")
        print("4- Devolver livro")
        print("5- Listar livros emprestados")
        print("0- Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            titulo = input("\nTítulo: ")
            autor = input("Autor: ")
            id_livro = int(input("ID do livro: "))

            livro = Livro(titulo, autor, id_livro)

            livros.append(livro)

            print("\nLivro cadastrado com sucesso!\n")

        elif opcao == "2":
            nome = input("\nNome: ")
            matricula = input("Matrícula: ")
            
            usuario = Usuario(nome, matricula)
            
            usuarios.append(usuario)
            
            print("\nUsuário cadastrado com sucesso!\n")

        elif opcao == "3":
            if len(usuarios) == 0:
                print("\nCadastre um usuário antes de realizar empréstimos.\n")
                continue
            if len(livros) == 0:
                print("\nNão há livros cadastrados.\n")
                continue

            matricula = input("\nMatrícula do usuário: ")

            usuario = None
            for u in usuarios:
                if u.get_matricula() == matricula:
                    usuario = u
            if usuario is None:
                print("\nUsuário não encontrado!\n")
                continue

            id_livro = int(input("\nID do livro: "))

            livro = None
            for l in livros:
                if l.get_id_livro() == id_livro:
                    livro = l
            if livro is None:
                print("\nLivro não encontrado!\n")
            else: 
                usuario.emprestar_livro(livro)

        elif opcao == "4":
            if len(usuarios) == 0:
                print("\nCadastre um usuário antes de devolver livros.\n")
                continue

            matricula = input("\nMatrícula do usuário: ")
            
            usuario = None
            for u in usuarios:
                if u.get_matricula() == matricula:
                    usuario = u

            if usuario is None:
                print("\nUsuário não encontrado!\n")
                continue
            
            id_livro = int(input("\nID do livro: "))

            usuario.devolver_livro(id_livro)
                        
        elif opcao == "5":
            if len(usuarios) == 0:
                print("\nCadastre um usuário antes de listar empréstimos.\n")
                continue
            
            matricula = input("\nMatrícula do usuário: ")
                        
            usuario = None
            for u in usuarios:
                if u.get_matricula() == matricula:
                    usuario = u
            
            if usuario is None:
                print("\nUsuário não encontrado!\n")
            else:
                usuario.listar_livros_emprestados()


        elif opcao == "0":
            print("\nEncerrando programa...\n")
            break
        else:
            print("\nOpção inválida!\n")


if __name__ == "__main__":
    main()
