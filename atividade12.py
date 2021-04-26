from random import randint
#1
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

print(max(num1, num2, num3))

#2
a_file = open("aluno.txt", "r")

list_of_lists = []
for line in a_file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_of_lists.append(line_list)

a_file.close()

print(list_of_lists)

#3
lista = [3, 6, 3, 2, 1]

print(sum(lista))

#4
lista = ["seu", "joao", "esta", "aqui"]

lista_str = ' '.join(map(str, lista))
print(lista_str)

#5

lista = [3,8,9,1,0,2]
for i in lista:
    if i%2 == 0:
        print(i)
        
 #7

print(sum(lista))

#8

lista_str = '|'.join(map(str, lista))
print(lista_str)

#9
lista.sort()
print(lista)

#10

lista.sort(reverse = True)
print(lista)

#11

lista2 = [4,5,2,0,9]
print(lista2)

#12

lista = [3, 6, 3, 2, 1]

b = lista[3:]

print(b)

#15

lista10 = []
c = 0
while c < 11:
    lista10.append(c)
    c+=1

print(lista10)

#16

lista20 = []
d = 0
while d <= 20:
    if d%2 == 0:
        lista20.append(d)
        d+=1
    else:
        d+=1
print(lista20)

#17

listaR = []
print( [ randint(0,10) for i in range(20) ])

#18
listaMM = ["alo", "Alo", "aLO", "alO"]
print( list( map( lambda x: x.upper(), listaMM ) ) )

#19

listaMN = ["alo ", " Alo ", " aLO ,"" al0"]
print( list( map(lambda x: x.lower().strip, listaMN)))
