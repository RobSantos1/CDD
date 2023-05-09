texto = "O rato roeu a roupa do rei de Roma"


def contVogais(texto):
    contador = 0
    for x in texto.lower()[::+1]:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            contador += 1

    print(contador)

contVogais(texto)