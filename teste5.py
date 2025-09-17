media = 0
for n in range(4):
    nota = int(input("Digite a media: "))
    media+=nota
total = media/4
if total>=60:
    print("Aprovado")
else:
    print("Reprovado")