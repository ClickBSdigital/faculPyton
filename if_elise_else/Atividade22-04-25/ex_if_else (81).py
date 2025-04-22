# 81 - Verifique se um número é primo
num = int(input("Digite um número: "))
eh_primo = True

if num < 2:
    eh_primo = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            eh_primo = False
            break

if eh_primo:
    print("O número é primo.")
else:
    print("O número não é primo.")
