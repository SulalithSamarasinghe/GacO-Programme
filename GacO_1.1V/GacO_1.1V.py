#GacO_1.1V is a programme which can use to find the optimized energy values and
#DC kerr and EFISHG gamma values of a Gaussian out file.
#
import csv
#
print('')
print('********************')
print('*    GacO 1.1V     *')
print('********************')
print('')
print('Welcome!!! GacO 1.1V is a programme which can use to find Gaussian out file results,')
print('')
print('     ==> Optimized energy values in both Hartrees per particle and Electronvolts units')
print('     ==> DC kerr(-w;w,0,0) parallel and perpendicular gamma values')
print('     ==> EFISHG(-2w;w,w,0) parallel and perpendicular gamma values')
print('     ==> Create csv data files')
print('')
print('****************************************************************************************************************')
print('')
#
def GacOMenu():
    #
    #GacO 1.1V Panel
    #
    print('')
    print('+++++++++++++++++++++++++')
    print('++++ GacO 1.1V Panel ++++')
    print('+++++++++++++++++++++++++')
    print('')
    print('01. Optimized Energy Reader')
    print('02. Parallel & Perpendicular Gamma Reader')
    print('03. Help')
    print('04. End programme')
    #
    print('')
    inP = int(input('Enter Option ==> '))
    print('')
    #
    #Optimized Energy Reader
    #
    if inP == 1:
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
            print('04. Back')
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
                    print('04. Back')
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
                        print('Back')
                        print('')
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
                print('Back')
                print('')
            else:
                print('You have entered a wrong option!!!')
                print('Pleace try again')
                MainManu()
        MainManu()
        GacOMenu()
    #
    #Parallel & Perpendicular Gamma Reader
    #
    elif inP == 2:
        #
        #Programmed to read perpendicular and parallel values of DC kerr and EFISHG
        #
        print('')
        print('*******************************************')
        print('***Parallel & Perpendicular Gamma Reader***')
        print('*******************************************')
        print('')
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
        Tnumber =  []
        #
        #Main Menu of the PPGamma reader
        #
        def PPGammaMainManu():
            print('~~~Parallel & Perpendicular Gamma Reader Menu~~~')
            print('')
            print('01. New output file')
            print('02. Create data file')
            print('03. Back')
            print('')
            Iputg = int(input('Enter Option ==> '))
            print('')
            #
            if Iputg == 1:
                #
                inputFiles = input('Enter the Gaussian output file name : ')
                print('')
                trialNumbers = int(input('Trial Number : '))
                Tnumber.append(trialNumbers)
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
                    iPutg = int(input('Enter Option ==> '))
                    #
                    if iPutg == 1:
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
                    elif iPutg == 2:
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
                    elif iPutg == 3:
                        print('')
                        print('Back')
                        print('')
                    else:
                        print('You have entered a wrong option!!!')
                        print('Pleace try again')
                        PPGamma_Menu()
                #
                PPGamma_Menu()
                #
                PPGammaMainManu()
            elif Iputg == 2:
                print('')
                dataFileName = input('Enter name for the data file ==> ')
                print('')
                with open(dataFileName,'w',newline='') as dFile:
                    thewriter = csv.writer(dFile)
                    thewriter.writerow(['Trial Number','Wave Length','DC kerr Parallel (10**-36 esu)','DC kerr Perpendicular (10**-36 esu)','EFISHG Parallel (10**-36 esu)','EFISHG Perpendicular (10**-36 esu)'])
                    nlen = len(Tnumber)
                    for n in range(nlen):
                        thewriter.writerow([Tnumber[n],waveLength[n],DC_kerrparallelSU[n],DC_kerrperpendicularSU[n],EFISHGparallelSU[n],EFISHGperpendicularSU[n]])
                print('')
                print(dataFileName,' is Created!!!')
                print('')
                PPGammaMainManu()
            elif Iputg == 3:
                print('')
                print('Back')
            else:
                print('')
                print('You have entered a wrong option!!!')
                print('Pleace try again')
                PPGammaMainManu()
        PPGammaMainManu()
        GacOMenu()
    elif inP == 3:
        print('++++++++++++++++')
        print('+     Help     +')
        print('++++++++++++++++')
        print('')
        print('+ GacO 1.1V is a programme that is mainly focusing on finding the optimized energy values,')
        print('  parallel and perpendicular gamma values of a Gaussian output file.')
        print('+ Python 3.7 is the base code of the GacO 1.1V programme.')
        print('+ GacO 1.1V consist of 470 Python code lines.')
        print('')
        print('How to enter a Gaussian output file ? ')
        print('  + Gaussian output file and the GacO 1.1V programme must be in the same directory.')
        print('  + When entering the file name use the ".out" extension.')
        print('  + For a file name with no ".out" extension or a non-existing file, the programme will crash.')
        print('')
        print('How to create a data file ? ')
        print('  + This option will create a "xyz.csv" file in the same directory.')
        print('  + When entering the filr name use the ".csv" extension with the file name.')
        print('  + For a file name without no ".csv" extention, the programme will only generate a simple data file.')
        print('')
        print('Limitaions of options ?')
        print('  + Only restrict to numbers(ex: 0,1,2,3,...).')
        print('  + Do not enter letters(ex: a,b,c....) symbols (ex: #,$,%....).')
        print('')
        GacOMenu()
    elif inP == 4:
        print('')
        print('....End Programme....')
    else:
        print('You have entered a wrong option!!!')
        print('Pleace try again')
        GacOMenu()
GacOMenu()
