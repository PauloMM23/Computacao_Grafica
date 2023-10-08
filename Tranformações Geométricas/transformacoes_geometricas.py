import numpy as np

def translacao_matriz(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

def rotacao_matriz(angulo):
    cos_theta = np.cos(angulo)
    sin_theta = np.sin(angulo)
    return np.array([
        [cos_theta, -sin_theta, 0],
        [sin_theta, cos_theta, 0],
        [0, 0, 1]
    ])

def escala_matriz(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

def tranformacao(matriz, matT):
    return np.dot(matriz, matT)

def main():
    matT = np.identity(3)
    
    while True:
        print("1 --> Translação")
        print("2 --> Rotação")
        print("3 --> Escala")
        print("4 --> Próximo passo")

        opcao = int(input("\nEscolha uma das opções a cima: "))
        
        if opcao == 1:
            tx = float(input("Digite o valor de tx: "))
            ty = float(input("Digite o valor de ty: "))
            transformacao_matriz = translacao_matriz(tx, ty)
            matT = tranformacao(transformacao_matriz, matT)
            
        elif opcao == 2:
            angulo = np.radians(float(input("Digite o ângulo de rotação em graus: ")))
            transformacao_matriz = rotacao_matriz(angulo)
            matT = tranformacao(transformacao_matriz, matT)

        elif opcao == 3:
            sx = float(input("Digite o fator de escala sx: "))
            sy = float(input("Digite o fator de escala sy: "))
            transformacao_matriz = escala_matriz(sx, sy)
            matT = tranformacao(transformacao_matriz, matT)
            
        elif opcao == 4:
            break
    
    x = float(input("Digite o valor de X: "))
    y = float(input("Digite o valor de Y: "))
    ponto = np.array([x, y, 1])
    ponto_transformado = np.dot(matT, ponto)
    
    print("\nMatriz final:")
    print(matT)
    print("\nPontos transformados:", ponto_transformado[:2])

if __name__ == "__main__":
    main()