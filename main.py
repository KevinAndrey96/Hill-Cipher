import numpy as np;
import math
def imprimir_matriz(charar):
    for i in range(2):
        for j in range(2):
            print(int(charar[i][j]), "\t", end='')
        print("\n");

Rta=int(input("Cifrado de Hill.\n\n1. Cifrar\n2. Descifrar\n\nRta: "))
if Rta==1:
    #Solicitar Datos
    Texto = input("Por favor introduzca el texto a cifrar: ");
    Texto = Texto.upper().strip().replace(" ", "");
    print("Por favor introduzca la clave (matriz 2x2)");
    Clave = np.empty((4, 4));
    msj="";
    m_crip=np.zeros((math.ceil(len(Texto)/2),2))

    for i in range(2):
        for j in range(2):
            msj="Posición "+str(i)+","+str(j)+": ";
            Clave[i][j] = input(msj);

    imprimir_matriz(Clave)
    diccionario_letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4 , 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
    abecedario="ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    cipher="";
    i=0
    j=0
    while True:
        try:
            if (np.size(m_crip) / 2 == j):
                break
            print(Texto[i]," - ",Texto[i+1])
            m_crip[j][0]=diccionario_letras[Texto[i]]
            m_crip[j][1] = diccionario_letras[Texto[i+1]]
            i+=2
            j+=1

        except:
            print(Texto[i])
            m_crip[j][0] = diccionario_letras[Texto[i]]
            break
    #for i in range(m_crip.length)

    c1 = 0
    c2 = 0
    m1 = 0
    m1 = 0

    cipher=np.zeros(m_crip.shape)
    print("Texto Cifrado")

    for i in range(int(np.size(m_crip)/2)):

        m1 = m_crip[i][0]
        m2 = m_crip[i][1]
        c1 = Clave[0][0]*m1 + Clave[1][0]*m2
        c2 = Clave[0][1] * m1 + Clave[1][1] * m2
        cipher[i][0]=c1%26
        cipher[i][1] = c2%26

        #print(int(cipher[i][0]), " - ", int(cipher[i][1]))
        print(abecedario[int(cipher[i][0])],"",abecedario[int(cipher[i][1])]," ", end='')




else:
    #Descifrar
    # Solicitar Datos
    Texto = input("Por favor introduzca el texto a descifrar: ");
    Texto = Texto.upper().strip().replace(" ", "");
    print("Por favor introduzca la clave (matriz 2x2)");
    Clave = np.empty((4, 4));
    msj = "";
    m_crip = np.zeros((math.ceil(len(Texto) / 2), 2))

    for i in range(2):
        for j in range(2):
            msj="Posición "+str(i)+","+str(j)+": ";
            Clave[i][j] = input(msj);

    imprimir_matriz(Clave)
    diccionario_letras = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
                          'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
                          'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    #Inversa de una matriz A^-1=1/|A| * (A*)^T
    #Sacar determinante
    Determinante=Clave[0][0]*Clave[1][1]-Clave[0][1]*Clave[1][0]
    Adjunta=np.zeros((2,2))
    Adjunta[0][0] = Clave[1][1]
    Adjunta[1][1] = Clave[0][0]
    Adjunta[0][1] = -1*Clave[1][0]
    Adjunta[1][0] = -1*Clave[0][1]

    TAdj = np.zeros((2, 2))
    TAdj[0][0] = Adjunta[0][0]
    TAdj[1][1] = Adjunta[1][1]
    TAdj[0][1] = Adjunta[1][0]
    TAdj[1][0] = Adjunta[0][1]

    Determinante=Determinante%26
    InClave = np.zeros((2, 2))
    InClave[0][0]= ((1/Determinante)*TAdj[0][0])%26
    InClave[0][1] = ((1 / Determinante) * TAdj[0][1])%26
    InClave[1][0] = ((1 / Determinante) * TAdj[1][0])%26
    InClave[1][1] = ((1 / Determinante) * TAdj[1][1])%26

    """
    print("Determinante ",Determinante)
    print("Adjunta ")
    for i in range(2):
        for j in range(2):
            print(Adjunta[i][j], "\t", end='')
        print("\n");
    print("Adjunta Transpuesta")
    for i in range(2):
        for j in range(2):
            print(TAdj[i][j], "\t", end='')
        print("\n");

    print("Matriz Inversa de la clave ")
    for i in range(2):
        for j in range(2):
            print(InClave[i][j], "\t", end='')
        print("\n");
    """

    i = 0
    j = 0
    while True:
        try:
            if (np.size(m_crip) / 2 == j):
                break
            #print(Texto[i], " - ", Texto[i + 1])
            m_crip[j][0] = diccionario_letras[Texto[i]]
            m_crip[j][1] = diccionario_letras[Texto[i + 1]]
            i += 2
            j += 1

        except:
            print(Texto[i])
            m_crip[j][0] = diccionario_letras[Texto[i]]
            break
    # for i in range(m_crip.length)

    c1 = 0
    c2 = 0
    m1 = 0
    m1 = 0

    descipher = np.zeros(m_crip.shape)
    print("Texto Descifrado: ")
    for i in range(int(np.size(m_crip) / 2)):
        m1 = m_crip[i][0]
        m2 = m_crip[i][1]
        c1 = InClave[0][0] * m1 + InClave[1][0] * m2
        c2 = InClave[0][1] * m1 + InClave[1][1] * m2
        descipher[i][0] = c1 % 26
        descipher[i][1] = c2 % 26

        # print(int(cipher[i][0]), " - ", int(cipher[i][1]))
        print(abecedario[int(descipher[i][0])], "", abecedario[int(descipher[i][1])]," ", end='')

#VKFZRVWTIAZSMISGKA
