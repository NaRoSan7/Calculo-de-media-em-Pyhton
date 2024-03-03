print("\n")
print("Calculo de media!")
nome = input("Digite o nome do Aluno(a): ")

n1 = float(input("Digite a nota do 1º bimestre: "))
n2 = float(input("Digite a nota do 2º bimestre: "))
n3 = float(input("Digite a nota do 3º bimestre: "))
n4 = float(input("Digite a nota do 4º bimestre: "))

media = float((n1+n2+n3+n4)/4)

if media < 6 :
    print("O(A) Aluno(a): " + nome + ", Foi reprovado, com a media de :" + str(media) + ", Sinto muito :(")
else : 
    print("O(A) Aluno(a): " + nome + ", Foi Aprovado, com a media de : " + str(media) + ", Parabéns :D")