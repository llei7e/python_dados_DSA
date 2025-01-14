import random
from os import system, name
# Códigos de cores ANSI
vermelho = "\033[91m"  # Vermelho
verde = "\033[92m"  # Verde
reset = "\033[0m"  # Resetar cor

# Função para limpar a tela a cada execução
def limpar_tela():
    
    # Windows
    if name == 'nt':
        _ = system('cls')
        
    # Linux ou Mac
    else:
        _ = system('clear')


# Função que desenha a forca
def display_hangman(chances):


    # Lista de estagios da forca
    stages = [
        # Estagio 6 final
        f""" {vermelho}
            --------
            |      |
            |      O
            |     /|\\
            |     / \\
            |  
           --- {reset}
        """,
        # Estagio 5 
        """
            --------
            |      |
            |      O
            |     /|\\
            |     / 
            |     
           ---
        """,
        # Estagio 4 
        """
            --------
            |      |
            |      O
            |     /|\\
            |    
            |    
           ---  
        """,
        # Estagio 3 
        """
            --------
            |      |
            |      O
            |     /|
            |      
            |    
           ---  
        """,
        # Estagio 2
        """
            --------
            |      |
            |      O
            |      |
            |      
            |    
           ---  
        """,
                # Estagio 1
        """
            --------
            |      |
            |      O
            |     
            |      
            |    
           ---  
        """,
        # Estagio 0
        """
            --------
            |      |
            |      
            |     
            |      
            |    
           ---  
        """
    ]
    return stages[chances]


# Função principal
def game():
    limpar_tela()
    print("\nBem-vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    
    # Lista de palavras para o jogo
    palavras = [
    "banana", "abacate", "uva", "morango", "laranja", "melancia", "cereja", "ameixa", "pêssego", "amora",
    "elefante", "girafa", "cachorro", "gato", "tigre", "leão", "panda", "jacaré", "rinoceronte", "macaco",
    "carro", "ônibus", "avião", "bicicleta", "trem", "moto", "barco", "navio", "patinete", "metrô",
    "casa", "apartamento", "escola", "hospital", "mercado", "igreja", "praça", "loja", "padaria", "cinema",
    "computador", "celular", "teclado", "mouse", "monitor", "fones", "internet", "impressora", "microfone", "drone"
    ]

    
    # Palavra escolhida aleatóriamente para o turno
    palavra = random.choice(palavras)
    
    # List comprehension para colocar os underline no lugar das letras
    letras_palavra = ['_' for letra in palavra]
    
    # Numero de chances
    chances = 6
    
    # Lista para as letras erradas
    letras_erradas = []
    
    # Loop enquanto as chances forem maiores que 0
    while chances > 0:
        # Print
        print(display_hangman(chances))
        print(" ".join(letras_palavra), "\n")
        print("Letras erradas:", " ".join(letras_erradas))
        
        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()
        print("\n\n\n")
        
        # Verifica se a letra já foi tentada
        if tentativa in letras_palavra or tentativa in letras_erradas:
            print("\n*** Você já tentou essa letra. Tente outra. ***\n")
            continue  # Volta para o início do loop
        
        # Condicional para verificar se a tentativa está na palavra
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_palavra[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
            
        # Condicional para verificar vitória
        if "_" not in letras_palavra:
            print(f"\n{verde}*** Você venceu! ***\nA palavra era: ", palavra.upper(), f"{reset}\n\n\n")
            break

    # Condicional para verificar derrota
    if "_" in letras_palavra:
        print(display_hangman(chances))
        print(f"\n{vermelho}*** Você perdeu! ***\nA palavra era: ", palavra.upper(), f"{reset}\n\n\n")



# Main
if __name__ == "__main__":
    game()
