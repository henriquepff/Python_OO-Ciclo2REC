class AnalisadorTexto:
    def __init__(self, texto):
        self.texto = texto

    def tamanho_texto(self):
        return len(self.texto)

    def em_maiusculas(self):
        return self.texto.upper()

    def em_minusculas(self):
            return self.texto.lower()

    def contar_vogais(self):
        vogais = "aeiouAEIOU"
        contador = 0
        for caracter in self.texto:
            if caracter in vogais:
                contador += 1
        return contador

    def contem_ifb(self):
         return "IFB" in self.texto.upper()


def main():
    texto = input("\nDigite um texto: ")

    analisador = AnalisadorTexto(texto)

    print("\n===Análise do Texto===")
    print(f"Número de caracteres: {analisador.tamanho_texto()}")
    print(f"Em maiúsculas: {analisador.em_maiusculas()}")
    print(f"Em minúsculas: {analisador.em_minusculas()}")
    print(f"Número de vogais: {analisador.contar_vogais()}")

    if analisador.contem_ifb():
        print("A substring 'IFB' aparece no texto (independente de maiúsculas/minúsculas).\n")
    else:
        print("A substring 'IFB' NÃO aparece no texto.\n")

if __name__ == "__main__":
     main()