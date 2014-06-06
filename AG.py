

def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def orBits(l1,l2):
    result = []
    for i in range(len(l1)):
        result += [l1[i]|l2[i]]
    return result

def xorBits(l1,l2):
    result = []
    for i in range(len(l1)):
        result += [l1[i]^l2[i]]
    return result

def andBits(l1,l2):
    result = []
    for i in range(len(l1)):
        result += [l1[i]&l2[i]]
    return result

def toHex(l):
    chars = ''
    for b in range(len(l) / 4):
        hexa = l[b*4:(b+1)*4]
        chars += getLetras("".join([str(bit) for bit in hexa]))
    return chars

letras=['A','B','C','D','E','F']
def getLetras(s):
    r = ''
    num= int(s,2)
    if num > 9:
        r = letras[num - 10]
    else:
        r = str(num)
    return r


def algGenetico(clave):
    iteraciones = promedioAscii(clave) % len(clave)
    aBits = tobits(clave)
    while(iteraciones >= 0):
        dezp = (iteraciones)%len(aBits)
        aBits = aBits[dezp:] + aBits[:dezp]
        m1 = aBits[:len(aBits)/2]
        m2 = aBits[len(aBits)/2:]
        
        xorResult = xorBits(m1,m2)
        orResult = orBits(m1,m2)
        
        if iteraciones%2 == 0:
            aBits = xorResult + orResult
        else:
            aBits = orResult + xorResult     
        iteraciones -= 1
    print(frombits(aBits))

def promedioAscii(s):
    suma = 0
    for c in s:
        suma += ord(c)
    return suma/len(s)

def imprimir(pala, m1, m2, xorR,orR, it):
    print("Binario, it: ", it)
    print(frombits(pala))
    #impLine(pala)
    print("m1: ")
    impLine(m1)
    print("m2: ")
    impLine(m2)
    print("xor: ")
    impLine(xorR)
    print("or: ")
    impLine(orR)
def impLine(l):
    b=''
    for bit in l:
        b += str(bit) + " "
    print(b)
    print("-"*len(b))
