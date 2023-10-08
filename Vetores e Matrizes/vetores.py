#Desenvolva um programa que leia pelo teclado os valores x, y e z de um vetor de 3 dimensões

import math
import numpy as np

def escolher_vetores():
    x = float(input("Digite um valor para X: "))
    y = float(input("Digite um valor para Y: "))
    z = float(input("Digite um valor para Z: "))
    return np.array([x, y, z])

def calcular_tamanho_vetor(vetor):
    tamanho_vetor = np.linalg.norm(vetor)
    return tamanho_vetor

def normalizar_vetor(vetor):
    vetor_normalizado = vetor / np.linalg.norm(vetor)
    return vetor_normalizado

def adicionar_vetor(vetor1, vetor2):
    adicionar = vetor1 + vetor2
    return adicionar

def subtrair_vetor(vetor1, vetor2):
    subtrair = vetor1 - vetor2
    return subtrair

def multiplicar_por_escalar(vetor, escalar):
    multiplicar = vetor * escalar
    return multiplicar

def dividir_por_escalar(vetor, escalar):
    dividir = vetor / escalar
    return dividir

def calcular_produto_escalar(vetor1, vetor2):
    calcular_escalar = np.dot(vetor1, vetor2)
    return calcular_escalar

vetor = escolher_vetores()

while True:
    print("\n1 --> Calcular tamanho do Vetor")
    print("2 --> Normalizar Vetor")
    print("3 --> Adicionar outro Vetor")
    print("4 --> Subtrair outro Vetor")
    print("5 --> Ler valor escalar e Multiplicar pelo Vetor")
    print("6 --> Ler valor escalar e Dividir pelo Vetor")
    print("7 --> Calcular produto escalar")

    opcao = int(input("\nDigite uma das opções a cima: "))

    if opcao == 1:
        tamanho_vetor = calcular_tamanho_vetor(vetor)
        print("Tamanho do Vetor =", tamanho_vetor)

    elif opcao == 2:
        vetor_normalizado = normalizar_vetor(vetor)
        print("Vetor Normalizado =", vetor_normalizado)

    elif opcao == 3:
        adiciona_vetor = escolher_vetores()
        vetor_resultante = adicionar_vetor(vetor, adiciona_vetor)
        print("Adição realizada =", vetor_resultante)

    elif opcao == 4:
        subtrai_vetor = escolher_vetores()
        vetor_resultante = subtrair_vetor(vetor, subtrai_vetor)
        print("Subtração realizada =", vetor_resultante)

    elif opcao == 5:
        escalar = float(input("Digite o valor do escalar para multiplicar: "))
        vetor_resultante = multiplicar_por_escalar(vetor, escalar)
        print("Multiplicação realizada =", vetor_resultante)

    elif opcao == 6:
        escalar = float(input("Digite o valor do escalar para dividir: "))
        vetor_resultante = dividir_por_escalar(vetor, escalar)
        print("Divisão realizada =", vetor_resultante)

    elif opcao == 7:
        novo_vetor = escolher_vetores()
        produto_escalar = calcular_produto_escalar(vetor, novo_vetor)
        print("Resultado Produto escalar =", produto_escalar)

    else:
        print("\nOpção inválida, tente uma opção listada abaixo.")