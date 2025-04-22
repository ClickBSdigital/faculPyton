# 86 - Verifique se um número termina com o dígito 5
num = int(input("Digite um número: "))

if str(num)[-1] == '5':
    print("O número termina com 5.")
else:
    print("O número não termina com 5.")
