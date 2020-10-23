#program

text = input("Escreva o texto para o seu ficheiro: ")
file = open("texto.txt", "w")
file.write(text)
file.close()
file = open("texto.txt", "r")
print(len(file.readline()))
