n = int(input("Rentrez le nombre de table de multiplication que vous voulez : "))

assert n > 0

for i in range(1, n + 1):
    for y in range(1,11):
        print(f"Table de {i}")
        print(f"{i} * {y} = {i * y}")
