#Desenvolva um programa que leia pelo teclado os valores de uma matriz 3x3

import math
import numpy

matriz = numpy.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

print(matriz)

while True:
    print("1 --> Adição e subtração de outra matriz")
    print("2 --> Multiplicação e Divisão de um escalar")
    print("3 --> Multiplicação da matriz por um vetor")
    print("4 --> Multiplicação da matriz por outra matriz")
    print("5 --> Apresentar a transposta da matriz")

    opcao = int(input("\nDigite uma das opções a cima: "))

    if opcao == 1:
        matriz_2 = numpy.array([[2,5,8],
                               [3,6,9],
                               [4,7,1]])
        soma_matriz = matriz+matriz_2
        subtrai_matriz = matriz-matriz_2
        print("Soma das matrizes =")
        print(soma_matriz)
        print("Subtração das matrizes =")
        print(subtrai_matriz)
    
    elif opcao == 2:
        escalar = float(input("Digite o escalar: "))
        multiplica_escalar = matriz*escalar
        divide_escalar = matriz/escalar
        print("Multiplicação por escalar =")
        print(multiplica_escalar)
        print("Divisão por escalar =")
        print(divide_escalar)
    
    elif opcao == 3:
        vetor = numpy.array([1, 2, 3])
        resultado = matriz.dot(vetor)
        print("Matriz multiplicada pelo vetor =")
        print(resultado)
    
    elif opcao == 4:
        matriz_2 = numpy.array([[2, 5, 8],
                               [3, 6, 9],
                               [4, 7, 1]])
        resultado = matriz.dot(matriz_2)
        print("Matriz multiplicada por outra matriz =")
        print(resultado)
    
    elif opcao == 5:
        resultado = numpy.transpose(matriz)
        print("Matriz transposta =")
        print(resultado)