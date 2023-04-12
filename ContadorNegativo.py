count = 0
for i in range(10):
    testNumber = int(input("Digite qualquer numero: "))
    if testNumber < 0:
        count += 1

print(count)
