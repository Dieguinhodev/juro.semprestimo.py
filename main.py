# bloco de aprentação do programa
print ("este programa e para calcular juros de emprestimo")
print ("trabalhamos com emprestimo de 2, 6, 12, 24 meses")

# bloco de entrada de dados

print ("1- emprestimo de 2 meses:")
print ("2- emprestimo de 6 meses:")
print ("3- emprestimo de 12 meses:")
print ("4 emprestimo de 24 meses:")
t = int(input("digite uma opção:"))

c = float(input("digite um valor:"))

# bloco de processamentos


if t == 1:
    j = c *0.069* 2
    print(j)
else:
    if t == 2:
        j = c *7.14*6
        print(j)
    else:
        if t == 3:
            j = c *9.21*12
            print(j)
        else:
            if t == 4:
                j = c *12.46*24
                print(j)