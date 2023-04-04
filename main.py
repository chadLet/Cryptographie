# Création de notre alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
            'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ',
            "'", 'é', 'ç', 'à', ',', '.', ':', '/', '!', '(', ')', '?', '"', 'ê',
            'ô', '#', '1', '2', '3', '4', '5', '7', '8', '9', '0', '*', '-', '_',
            '~', '=', '+', '%', '£', '$', '^', ';', '<', '>']

# Entrée de la phrase à crypter
phrase = input("Insérez une phrase à crypter: ")


# Fonction cryptant la phrase par méthode de chiffre affine
def code(x):
    new_phrase = ""
    for i in x:
        if str(i) in alphabet:
            index = alphabet.index(str(i))
            new_index = 3 * index + 4
            if new_index >= len(alphabet):
                while new_index >= len(alphabet):
                    new_index -= len(alphabet)
            new_phrase += alphabet[new_index]
    return new_phrase


# Fonction décryptant la phrase par méthode de chiffre affine (inverse)
def uncode(x):
    ancient_phrase = ""
    for i in x:
        if str(i) in alphabet:
            index = alphabet.index(str(i))
            index -= 4
            if index < 0:
                index += len(alphabet)
            new_index = index * -30
            if new_index <= -len(alphabet):
                while new_index <= -len(alphabet):
                    new_index += len(alphabet)
            ancient_phrase += alphabet[new_index]
    return ancient_phrase


# Affichage des résultats
print(code(phrase))
coded = input("Insérez une phrase à décrypter: ")
print(uncode(coded))
