# faça um programa que verifica se uma letra 
# digitata é vogal ou consoante.
# letra = input("Digite uma letra: ").lower()

# if len(letra) != 1 or not letra.isalpha():
#     print("Entrada inválida. Digite apenas uma letra.")
# elif letra in "aeiou":
#     print("Vogal")
# else:
#     print("Consoante")

letra = input("Digite uma letra: ")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or \
   letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print("Vogal")
else:
    print("Consoante")
