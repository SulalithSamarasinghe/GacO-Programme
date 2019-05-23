#Programmed to read optimized energy values of a Gaussian out files
print('')
print('***Optimized Energy Reader***')
print('')
#
inputFile = input('Enter the Gaussian .out file name : ')
#
nLines = 0
scfLines = 0
fLine = 0
fEn = 0
enHF = []
eneV = []
optEn = []
#
with open(inputFile,'r') as file:
    for line in file:
        wordsInLine = line.split()
        lenLine = len(wordsInLine)
        #
        nLines += 1
        for i in range(lenLine):
            if wordsInLine[i] == 'SCF' and wordsInLine[i+1] == 'Done:':
                scfLines += 1
                fLine = nLines
                optEn = optEn + [wordsInLine[i+4]]
#
#Optimized Energies of the file in hartrees pre particle and electronvolt
for i in range(len(optEn)):
    enHF = enHF + [float(optEn[i])]
    eneV = eneV + [enHF[i]*27.0]
#
#Final Optimized Energy of the file
fEn = enHF[len(enHF)-1]
#
#Optimized Energy Reader Menu Function as OER_Menu
#
def OER_Menu():
    print('')
    print('~~~Optimized Energy Reader Menu~~~')
    print('')
    print('01. Number of optimized energy values in the file')
    print('02. All the optimized energy values of the molecule')
    print('03. Final optimized energy of the molecule')
    print('04. Exit menu')
    print('')
    #
    iPut = int(input('Enter Option ==> '))
    #
    if iPut == 1:
        print('')
        print('Number of Optimized Energy values = ',scfLines)
        OER_Menu()
    elif iPut == 2:
        print('')
        print('Optimized energies of the molecule ==> ')
        print('')
        print('Hartrees per particle            Electronvolts')
        for i in range(len(enHF)):
            print(enHF[i],'                 ',eneV[i])
        OER_Menu()
    elif iPut == 3:
        print('')
        print('Final Optimized Energy = ', enHF[len(enHF)-1],' Hartrees per particle')
        print('Final Optimized Energy = ', eneV[len(eneV)-1],' Electronvolts')
        OER_Menu()
    elif iPut == 4:
        print('')
        print('Exit menu')
    else:
        print('You have entered a wrong option!!!')
        print('Pleace try again')
        OER_Menu()
#
OER_Menu()
#
