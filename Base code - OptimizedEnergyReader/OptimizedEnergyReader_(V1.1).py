import csv
#
#Programmed to read optimized energy values of a Gaussian out files
#
print('')
print('*****************************')
print('***Optimized Energy Reader***')
print('*****************************')
print('')
#
BOEHF = []
BOEeV = []
tNo = []
BS = []
#
#Main Menu of the Programme
#
def MainManu():
    print('~~~Main Menu~~~')
    print('')
    print('01. New output file')
    print('02. The optimized energies of the output files')
    print('03. Create data file')
    print('04. Exit')
    print('')
    Iput = int(input('Enter Option ==> '))
    print('')
    #
    if Iput == 1:
        #
        inputFile = input('Enter the Gaussian output file name : ')
        print('')
        trialNumber = int(input('Trial Number : '))
        tNo.append(trialNumber)
        print('')
        basisSet = input('Basis set used : ')
        BS.append(basisSet)
        #
        nLines = 0
        scfLines = 0
        fLine = 0
        fEnHF = 0
        fEneV = 0
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
        fEnHF = enHF[len(enHF)-1]
        fEneV = eneV[len(eneV)-1]
        BOEHF.append(fEnHF)
        BOEeV.append(fEneV)
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
                print('Final Optimized Energy = ', fEnHF,' Hartrees per particle')
                print('Final Optimized Energy = ', fEneV,' Electronvolts')
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
        MainManu()
    elif Iput == 2:
        nlen = len(BOEHF)
        for k in range(nlen):
            print('')
            print('For The Basis Set ==> ',BS[k])
            print('')
            print('    Trial No.',tNo[k],'Optimized Energy ==>')
            print('')
            print('                         ',BOEHF[k],' Hartrees per particle')
            print('                         ',BOEeV[k],' Electronvolts')
        MainManu()
    elif Iput == 3:
        print('')
        dataFileName = input('Enter name for the data file ==> ')
        print('')
        with open(dataFileName,'w',newline='') as dFile:
            thewriter = csv.writer(dFile)
            thewriter.writerow(['Trial Number','Basis Set','Energy (Hartrees/Particle)','Energy (eV)'])
            nlen = len(BOEHF)
            for n in range(nlen):
                thewriter.writerow([tNo[n],BS[n],BOEHF[n],BOEeV[n]])
        print(dataFileName,' is Created!!!')
        MainManu()
    elif Iput == 4:
        print('')
        print('Exit Programme')
    else:
        print('You have entered a wrong option!!!')
        print('Pleace try again')
        MainManu()
MainManu()
