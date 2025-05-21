# 14. Tabuada de 1 a 10 (usando dois for)

for i in range(1, 11):
    print(f"\nTabuada do {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")