#
DC_kerrUnit = []
EFISHGUnit = []
DC_kerrparallel =  []
DC_kerrparallelSU =  []
DC_kerrperpendicular = []
DC_kerrperpendicularSU = []
EFISHGparallel = []
EFISHGparallelSU = []
EFISHGperpendicular = []
EFISHGperpendicularSU = []
waveLength = []
#
inputFiles = input('Enter the Gaussian output file name : ')
print('')
#
nLinesg = 0
gLinesg = 0
DC_kerrLines = 0
EFISHGLines = 0
DC_kerrUL = []
DC_kerrparallelL = []
DC_kerrperpendicularL = []
DC_kerrUV = []
DC_kerrUVN = []
DC_kerrUnitT = []
DC_kerrparallelV = []
DC_kerrparallelT = []
DC_kerrperpendicularV = []
DC_kerrperpendicularT = []
EFISHGUL = []
EFISHGparallelL = []
EFISHGperpendicularL = []
EFISHGUV = []
EFISHGUVN = []
EFISHGUnitT = []
EFISHGparallelV = []
EFISHGparallelT = []
EFISHGperpendicularV = []
EFISHGperpendicularT = []
DC_kerrparallelT = []
waveL = 0
#
fLine = 0
#
with open(inputFiles,'r') as files:
    for lines in files:
        wordsInLines = lines.split()
        lenLine = len(wordsInLines)
        #
        nLinesg += 1
        for i in range(lenLine):
            #DC_kerr Gamma value reader
            if wordsInLines[i] == 'Gamma(-w;w,0,0)' and wordsInLines[i+1] == 'w=':
                DC_kerrLines += 1
                DC_kerrUL = DC_kerrUL + [nLinesg+1]
                DC_kerrparallelL = DC_kerrparallelL + [nLinesg+2]
                DC_kerrperpendicularL = DC_kerrperpendicularL + [nLinesg+3]
                waveL = wordsInLines[i+2].split(':')
            #EFISHG Gamma value reader
            elif wordsInLines[i] == 'Gamma(-2w;w,w,0)' and wordsInLines[i+1] == 'w=':
                EFISHGLines += 1
                EFISHGUL = EFISHGUL + [nLinesg+1]
                EFISHGparallelL = EFISHGparallelL + [nLinesg+2]
                EFISHGperpendicularL = EFISHGperpendicularL + [nLinesg+3]
with open(inputFiles,'r') as files:
    for lines in files:
        wordsInLines = lines.split()
        lenLine = len(wordsInLines)
        #
        gLinesg += 1
        #
        Leng = len(DC_kerrUL)
        #
        for m in range (Leng):
            if gLinesg == DC_kerrUL[m]:
                DC_kerrUV.append(wordsInLines)
            elif gLinesg == DC_kerrparallelL[m]:
                DC_kerrparallelV.append(wordsInLines)
            elif gLinesg == DC_kerrperpendicularL[m]:
                DC_kerrperpendicularV.append(wordsInLines)
            elif gLinesg == EFISHGUL[m]:
                EFISHGUV.append(wordsInLines)
            elif gLinesg == EFISHGparallelL[m]:
                EFISHGparallelV.append(wordsInLines)
            elif gLinesg == EFISHGperpendicularL[m]:
                EFISHGperpendicularV.append(wordsInLines)
#Units
for x in range (len(DC_kerrUV)):
    for y in range (len(DC_kerrUV[x])):
        if DC_kerrUV[x][y][0] == '(' and DC_kerrUV[x][y][len(DC_kerrUV[x][y])-1] == ')':
            DC_kerrUVN.append(DC_kerrUV[x][y])
        elif DC_kerrUV[x][y][0] == '(' and DC_kerrUV[x][y][len(DC_kerrUV[x][y])-1] != ')':
            for z in range (y+1,len(DC_kerrUV[x])):
                if DC_kerrUV[x][z][len(DC_kerrUV[x][z])-1] == ')':
                    DC_kerrUVN.append(DC_kerrUV[x][y]+DC_kerrUV[x][z])
                    break
for x in range (len(EFISHGUV)):
    for y in range (len(EFISHGUV[x])):
        if EFISHGUV[x][y][0] == '(' and EFISHGUV[x][y][len(EFISHGUV[x][y])-1] == ')':
            EFISHGUVN.append(EFISHGUV[x][y])
        elif EFISHGUV[x][y][0] == '(' and EFISHGUV[x][y][len(EFISHGUV[x][y])-1] != ')':
            for z in range (y+1,len(EFISHGUV[x])):
                if EFISHGUV[x][z][len(EFISHGUV[x][z])-1] == ')':
                    EFISHGUVN.append(EFISHGUV[x][y]+EFISHGUV[x][z])
                    break
#
#Final parallel and perpendicular gamma values
#
for i in range (len(EFISHGparallelV[len(EFISHGparallelV)-1])):
    if i == 0 :
        continue
    else:
        EFISHGparallel.append(EFISHGparallelV[len(EFISHGparallelV)-1][i])
        EFISHGperpendicular.append(EFISHGperpendicularV[len(EFISHGperpendicularV)-1][i])
        DC_kerrparallel.append(DC_kerrparallelV[len(DC_kerrparallelV)-1][i])
        DC_kerrperpendicular.append(DC_kerrperpendicularV[len(DC_kerrperpendicularV)-1][i])
        EFISHGparallelT.append(EFISHGparallelV[len(EFISHGparallelV)-1][i])
        EFISHGperpendicularT.append(EFISHGperpendicularV[len(EFISHGperpendicularV)-1][i])
        DC_kerrparallelT.append(DC_kerrparallelV[len(DC_kerrparallelV)-1][i])
        DC_kerrperpendicularT.append(DC_kerrperpendicularV[len(DC_kerrperpendicularV)-1][i])
        if i == 2:
            EFISHGparallelSU.append(EFISHGparallelV[len(EFISHGparallelV)-1][i])
            EFISHGperpendicularSU.append(EFISHGperpendicularV[len(EFISHGperpendicularV)-1][i])
            DC_kerrparallelSU.append(DC_kerrparallelV[len(DC_kerrparallelV)-1][i])
            DC_kerrperpendicularSU.append(DC_kerrperpendicularV[len(DC_kerrperpendicularV)-1][i])
#
waveLength.append(waveL[0])
#
#Final units
#
starts = (len(EFISHGparallelT))*(-1)
#
while starts< 0:
    DC_kerrUnit.append(DC_kerrUVN[starts])
    EFISHGUnit.append(EFISHGUVN[starts])
    DC_kerrUnitT.append(DC_kerrUVN[starts])
    EFISHGUnitT.append(EFISHGUVN[starts])
    starts += 1
#
#
#PPGamma value reader menu
#
def PPGamma_Menu():
    print('')
    print('~~~Gamma Reader~~~')
    print('')
    print('01. DC kerr parallel and perpendicular gamma values')
    print('02. EFISHG parallel and perpendicular gamma values')
    print('03. Back')
    print('')
    #
    iPut = int(input('Enter Option ==> '))
    #
    if iPut == 1:
        print('')
        print('DC kerr parallel gamma values ==> ')
        print('')
        #
        for i in range(len(DC_kerrparallelT)):
            print('              ',DC_kerrparallelT[i],' ',DC_kerrUnitT[i])
        #
        print('')
        print('DC kerr perpendicular gamma values ==> ')
        print('')
        #
        for i in range(len(DC_kerrperpendicularT)):
            print('              ',DC_kerrperpendicularT[i],' ',DC_kerrUnitT[i])
        #
        PPGamma_Menu()
    elif iPut == 2:
        print('')
        print('EFISHG parallel gamma values ==> ')
        print('')
        #
        for i in range(len(EFISHGparallelT)):
            print('              ',EFISHGparallelT[i],' ',EFISHGUnitT[i])
        #
        print('')
        print('EFISHG perpendicular gamma values ==> ')
        print('')
        #
        for i in range(len(EFISHGperpendicularT)):
            print('              ',EFISHGperpendicularT[i],' ',EFISHGUnitT[i])
        #
        PPGamma_Menu()
    elif iPut == 3:
        print('')
        print('Back')
    else:
        print('')
        print('You have entered a wrong option!!!')
        print('Pleace try again')
        PPGamma_Menu()
#
PPGamma_Menu()
#
