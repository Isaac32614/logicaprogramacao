#Exercicio1:
def Ex_1():
    n1=int(input("Digite a primeira nota"))
    n2 = int(input("Digite a segunda nota"))
    n3 = int(input("Digite a terceira nota"))
    mediaNota = (n1+n2+n3)/3
    return (F"Média do aluno é",int(mediaNota))
Ex_1()


#Exercicio2:
N = int(input("Digite o tamanho da lista: "))
lista = []
def Ex_2():
  i = 0
  while i < N:
    num = input()
    lista.append(num)
    i += 1
  return lista
Ex_2()


#Exercicio3:
def Ex_3():
  entrada = input("Digite 'a' para Globo, 'b' para SBT e 'z' ou 'Z' para encerrar o programa: ")
  while entrada != 'z':
    if entrada == 'Z':
      break
    elif entrada == 'a':
      print("Globo")
    elif entrada == 'b':
      print("SBT")
    else:
      print("Invalido")
    entrada = input()
Ex_3()


#Exercicio4:
def Ex_4():
  i = 0
  lista = input("Digite as médias dos alunos: ")
  list = lista.split()
  media_mn = []
  while i < len(list):
    if int(list[i]) < 7:
      media_mn.append(list[i])
    i += 1
    if len(media_mn) < 0.25 * len(list):
      return "Professor Coxa"
    else:
     return "Professor Padrão"
Ex_4()

