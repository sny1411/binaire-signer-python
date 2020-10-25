def complementUn(nbreBin):
    """renvoie le complément à 1 d'un nombre binaire
    entrée: nbreBin de type str
    sortie: r de type int """
    r = ''
    for i in nbreBin:
        if i == '0':
            r += '1'
        else:
            r += '0'
    return r

def conversionBinaire(nbreDecimal): #fonction repris d'un exercice avant
    """convertie decimal en binaire
    entrées: nbreDecimal du type int
    sortie: nbreBin du type string"""
    nbreBin = ''
    while nbreDecimal != 0:
        nbreBin = str(nbreDecimal % 2) + nbreBin
        nbreDecimal = nbreDecimal // 2
    return nbreBin

def soustractionBinaire(binA,binB,bit):
    """soustraie binA par binB (deux nombre binaire)
    entrée: binA et binB du type str et bit de type int (bit -> le nbre de bit sur lequel est coder le nombre)
    sortie: result de type str"""
    retenue = 0
    soust = 0
    result = ''

    for i in range(bit):
        soust = int(binA[bit - 1 -i]) - int(binB[bit - 1 - i]) - retenue
        if soust == 0:
            result = '0' + result
            retenue = 0
        elif soust == 1:
            result = '1' + result
            retenue = 0
        elif soust == -1:
            result = '1' + result
            retenue = 1
    return result


def sommeBin(binA, binB,bit):
    """fait la somme de deux nombre binaire
    entrée: binA et binB de type str et bit de type int
    sortie: result de type str"""
    retenue = 0
    add = 0
    result = ''
    for i in range(bit):
        add = int(binA[(bit - 1)- i]) + int(binB[(bit - 1)- i]) + retenue
        if add == 0:
            result = '0' + result
            retenue = 0
        elif add == 1:
            result = '1' + result
            retenue = 0
        elif add == 2:
            result = '0' + result
            retenue = 1
        elif add == 3:   
            result = '1' + result
            retenue = 1
        else:
            print("oula, gros probleme x)")
    return result


def conversionBinaireSign(n,bit):
    """convertie de la base 10 au binaire signé
    entrée: n et bit de type int
    sortie: result de type str"""
    result = ''
    n = str(n)
    if n[0] != '-': #si n est positif
        result = conversionBinaire(int(n))
        for i in range(bit - len(result)):
            result = '0' + result
    else: # sinon (n est négatif)
        result = conversionBinaire(int(n[1:]))
        for i in range(bit - len(result)):
            result = '0' + result
        result = complementUn(result)
        unEnBinaire = '1'
        for i in range(bit - len(unEnBinaire)):
            unEnBinaire = '0' + unEnBinaire
        result = sommeBin(result,unEnBinaire,bit)
    return result

def sommeBinSign(a,b,bit):
    """fait la somme de deux nombre binaire signé ^^
    entrée: a,b et bit de type int
    sortie: tuple avec result de type str et le signe de type str également"""
    binA = conversionBinaireSign(a , bit)
    binB = conversionBinaireSign(b , bit)
    result = sommeBin(binA,binB,bit)
    if result[0] == '1':
        binUn = '1'
        for i in range(bit - len(binUn)):
            binUn = '0' + binUn
        return complementUn(soustractionBinaire(result, binUn , bit)) , '-'
    else:
        return result , '+'
        


a = int(input("entre un nbre -> "))
b = int(input("entre un autre nbre -> "))
bit = int(input("sur cmb de bit doit etre coder les nbre? "))

result, signe = sommeBinSign(a,b,bit)
print("le resultat est donc : {}{}".format(signe,result))