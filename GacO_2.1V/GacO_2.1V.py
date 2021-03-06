#
#
#
from os import walk
import os
import pandas
import csv
import xlsxwriter
import math
import statistics
#
#
#
def start():
    print('')
    print('                                  ********************')
    print('                                  *    GacO 2.1V     *')
    print('                                  ********************')
    print('')
    print('----------------------------------------------------------------------------------------')
    print('')
    print('Welcome!!! GacO 2.1V is a programme which can use to find Gaussian out file results,')
    print('')
    print('     ==> Optimized energy values in both Hartrees per particle and Electronvolts units.')
    print('     ==> DC kerr(-w;w,0,0) parallel and perpendicular gamma values.')
    print('     ==> EFISHG(-2w;w,w,0) parallel and perpendicular gamma values.')
    print('     ==> Create csv data files.')
    print('     ==> Calculate average, standard deviation and standard error for different trials.')
    print('     ==> Create graphs of Gamma Values VS Wave Length.')
    print('')
    print("Whats new in GacO 2.1V,")
    print('')
    print('     ==> Highest positive and negative peak finder for the gamma values.')
    print('     ==> Minor bugs fixed.')
    print('')
    print('----------------------------------------------------------------------------------------')
    print('')
#
#
#
def wrongOption():
    print('')
    print('You have entered a wrong option!!!')
    print('Pleace try again')
    print('')
#
#
#
def endProgramme():
    print('')
    print('....End Programme....')
    print('')
#
#
#
def back():
    print('')
    print('....Back....')
    print('')
#
#
#
def help():
    print('')
    print('--------------------------------------------------------------------------------------------------------------')
    print('')
    print('                                            ++++++++++++++++')
    print('                                            +     Help     +')
    print('                                            ++++++++++++++++')
    print('')
    print('+ GacO 2.1V is a programme that is mainly focusing on finding the optimized energy values,')
    print('  parallel and perpendicular gamma values of a Gaussian output file.')
    print('+ Also calculates the average, standard deviation and standard error for different trials.')
    print('+ GacO 2.1V creates graphs of Gamma Values VS Wave Length.')
    print('+ Python 3.7 is the base code of the GacO 2.1V programme.')
    print('+ GacO 2.1V consist of 1431 Python code lines.')
    print('')
    print('How to enter a Gaussian output file ? ')
    print('  + Gaussian output file and the GacO 2.1V programme must be in the same directory.')
    print('  + When entering the file name use the ".out" extension.')
    print('  + For a file name with no ".out" extension or a non-existing file, the programme will crash.')
    print('')
    print('How to create a data file ? ')
    print('  + This option will create a "xyz.csv" file in the same directory.')
    print('  + When entering the file name use the ".csv" extension with the file name.')
    print('  + Do not use symbols for the "xyz.csv" file name.')
    print('  + For a file name without no ".csv" extention, the programme will only generate a simple data file.')
    print('')
    print('Limitaions of options ?')
    print('  + Only restrict to numbers(ex: 0,1,2,3,...).')
    print('  + Do not enter letters(ex: a,b,c....) symbols (ex: #,$,%....).')
    print('')
    print('What is automated calculations feature ?')
    print('  + Automated calculations option will calculate and produce final "xyz.csv" and graph file.')
    print('  + This feature requires a specific path for the "xyz.out" files.')
    print('')
    print('How to create the folder path for "Automated calculations" ?')
    print('  + Create a folder and place the "GacO_2.1V.exe".')
    print('  + Within the same folder, create new folders with the name of the molecules (ex: BP2_Gamma_Calculation).')
    print('  + Within the newly created folders create four new folders.')
    print('  + Name them as "Results_And_Graphs","T1","T2","T3".')
    print('')
    print('How to use automated calculations feature ?')
    print('  + Enter the name of the molecule (ex: BP0,BP2,...).')
    print('  + The molecule name must be in capital letters.')
    print('')
    print('How to use highest positive and negative peak feature ?')
    print('  + Enter the name of the "xyz.csv" file which contains the average values (ex: BP0_EFISHG_Perpendicular.csv)')
    print('  + Suggested wavelengths can be used for further calculations.')
    print('')
    print('--------------------------------------------------------------------------------------------------------------')
    print('')
#
#Programmed to read perpendicular and parallel values of DC kerr and EFISHG
#
def parallelPerpendicularGammaReader():
    print('')
    print('                        *******************************************')
    print('                        ***Parallel & Perpendicular Gamma Reader***')
    print('                        *******************************************')
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
        print('')
        print('~~~Parallel & Perpendicular Gamma Reader Menu~~~')
        print('')
        print('01. New output file')
        print('02. Create data file')
        print('03. Create graphs')
        print('04. Final calculations and graphs')
        print('05. Highest positive & negative peaks')
        print('06. Back')
        print('')
        Iputg = int(input('Enter Option ==> '))
        print('')
        #
        if Iputg == 1:
            #
            print('')
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
                    stringValue = EFISHGparallelV[len(EFISHGparallelV)-1][i]
                    stringValue = stringValue.replace('D','E')
                    EFISHGparallel.append(stringValue)
                    stringValue = EFISHGperpendicularV[len(EFISHGperpendicularV)-1][i]
                    stringValue = stringValue.replace('D','E')
                    EFISHGperpendicular.append(stringValue)
                    stringValue = DC_kerrparallelV[len(DC_kerrparallelV)-1][i]
                    stringValue = stringValue.replace('D','E')
                    DC_kerrparallel.append(stringValue)
                    stringValue = DC_kerrperpendicularV[len(DC_kerrperpendicularV)-1][i]
                    stringValue = stringValue.replace('D','E')
                    DC_kerrperpendicular.append(stringValue)
                    stringValue = EFISHGparallelV[len(EFISHGparallelV)-1][i]
                    stringValue = stringValue.replace('D','E')
                    EFISHGparallelT.append(stringValue)
                    stringValue = EFISHGperpendicularV[len(EFISHGperpendicularV)-1][i]
                    stringValue = stringValue.replace('D','E')
                    EFISHGperpendicularT.append(stringValue)
                    stringValue = DC_kerrparallelV[len(DC_kerrparallelV)-1][i]
                    stringValue = stringValue.replace('D','E')
                    DC_kerrparallelT.append(stringValue)
                    stringValue = DC_kerrperpendicularV[len(DC_kerrperpendicularV)-1][i]
                    stringValue = stringValue.replace('D','E')
                    DC_kerrperpendicularT.append(stringValue)
                    if i == 2:
                        stringValue = EFISHGparallelV[len(EFISHGparallelV)-1][i]
                        stringValue = stringValue.replace('D','E')
                        EFISHGparallelSU.append(stringValue)
                        stringValue = EFISHGperpendicularV[len(EFISHGperpendicularV)-1][i]
                        stringValue = stringValue.replace('D','E')
                        EFISHGperpendicularSU.append(stringValue)
                        stringValue = DC_kerrparallelV[len(DC_kerrparallelV)-1][i]
                        stringValue = stringValue.replace('D','E')
                        DC_kerrparallelSU.append(stringValue)
                        stringValue = DC_kerrperpendicularV[len(DC_kerrperpendicularV)-1][i]
                        stringValue = stringValue.replace('D','E')
                        DC_kerrperpendicularSU.append(stringValue)
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
                    print('')
                    PPGamma_Menu()
                elif iPutg == 3:
                    back()
                else:
                    wrongOption()
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
                thewriter.writerow(['Trial Number','Wave Length (nm)','DC kerr Parallel (10**-36 esu)','DC kerr Perpendicular (10**-36 esu)','EFISHG Parallel (10**-36 esu)','EFISHG Perpendicular (10**-36 esu)'])
                nlen = len(Tnumber)
                for n in range(nlen):
                    waveLength[n] = (waveLength[n].split('nm'))[0]
                    thewriter.writerow([Tnumber[n],waveLength[n],DC_kerrparallelSU[n],DC_kerrperpendicularSU[n],EFISHGparallelSU[n],EFISHGperpendicularSU[n]])
            print('')
            print(dataFileName,' is Created!!!')
            print('')
            PPGammaMainManu()
        elif Iputg == 3:
            sFinalFileCreator()
            PPGammaMainManu()
        elif Iputg == 4:
            finalFileCreator()
            PPGammaMainManu()
        elif Iputg == 5:
            HighestNPP()
            PPGammaMainManu()
        elif Iputg == 6:
            back()
        else:
            wrongOption()
            PPGammaMainManu()
    PPGammaMainManu()
#
#Programmed to read optimized energy values of a Gaussian out files
#
def optimizedEnergyReader():
    print('')
    print('                              *****************************')
    print('                              ***Optimized Energy Reader***')
    print('                              *****************************')
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
        print('')
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
            print('')
            inputFile = input('Enter the Gaussian output file name : ')
            print('')
            trialNumber = int(input('Trial Number : '))
            tNo.append(trialNumber)
            print('')
            basisSet = input('Basis set used : ')
            print('')
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
                print('')
                #
                if iPut == 1:
                    print('')
                    print('Number of Optimized Energy values = ',scfLines)
                    print('')
                    OER_Menu()
                elif iPut == 2:
                    print('')
                    print('Optimized energies of the molecule ==> ')
                    print('')
                    print('Hartrees per particle            Electronvolts')
                    for i in range(len(enHF)):
                        print(enHF[i],'                 ',eneV[i])
                    print('')
                    OER_Menu()
                elif iPut == 3:
                    print('')
                    print('Final Optimized Energy = ', fEnHF,' Hartrees per particle')
                    print('Final Optimized Energy = ', fEneV,' Electronvolts')
                    print('')
                    OER_Menu()
                elif iPut == 4:
                    back()
                else:
                    wrongOption()
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
                print('')
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
            print('')
            MainManu()
        elif Iput == 4:
            back()
        else:
            wrongOption()
            MainManu()
    MainManu()
#
#
#
def GacOMenu():
    #
    #GacO 2.1V Panel
    #
    print('')
    print('                                +++++++++++++++++++++++++')
    print('                                ++++ GacO 2.1V Panel ++++')
    print('                                +++++++++++++++++++++++++')
    print('')
    print('01. Optimized Energy Reader')
    print('02. Parallel & Perpendicular Gamma Reader')
    print('03. Automated Calculations')
    print('04. Help')
    print('05. End programme')
    #
    print('')
    inP = int(input('Enter Option ==> '))
    print('')
    #
    if inP == 1:
        optimizedEnergyReader()
        errorHandler(GacOMenu)
    elif inP == 2:
        parallelPerpendicularGammaReader()
        errorHandler(GacOMenu)
    elif inP == 3:
        automatedCalculation('GacO_2.1V.exe')
        errorHandler(GacOMenu)
    elif inP == 4:
        help()
        errorHandler(GacOMenu)
    elif inP == 5:
        endProgramme()
    else:
        wrongOption()
        errorHandler(GacOMenu)
#
#
#
def updateFile(fileName,newFileName):
    rows = []
    with open(fileName, 'r',newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
    rows[0][1] = 'Wave_Length'
    rows[0][2] = 'DC_kerr_Parallel'
    rows[0][3] = 'DC_kerr_Perpendicular'
    rows[0][4] = 'EFISHG_Parallel'
    rows[0][5] = 'EFISHG_Perpendicular'
    #
    with open(newFileName, 'w',newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)
#
#
#
def fileCreator(FileName,type,t1,t2,t3,waveLength,averageName,writeType,waveLengthName):
    with open(FileName,writeType,newline='') as dFile:
        thewriter = csv.writer(dFile)
        thewriter.writerow([])
        thewriter.writerow([waveLengthName,'Trial Number 1 (10**-36 esu)','Trial Number 2 (10**-36 esu)','Trial Number 3 (10**-36 esu)',averageName,'Standard Deviation (10**-36 esu)','Standard Error (SE) (10**-36 esu)','Percentage (Standard Deviation/|Average| x 100 %)'])
        nlen = len(waveLength)
        for n in range(nlen):
            stdVL = [t1[n],t2[n],t3[n]]
            stdV = statistics.stdev(stdVL)
            stdE = stdV/(math.sqrt(3))
            average = float((t1[n]+t2[n]+t3[n])/3.0)
            percentageV = (stdV/average)*100.0
            if percentageV < 0.0 :
                percentageV = percentageV * -1.0
            thewriter.writerow([waveLength[n],t1[n],t2[n],t3[n],average,stdV,stdE,percentageV])
#
#
#
def innerGraphCreator(workbook,worksheet,bold,Graph_Name,gammaType,heading_start,column_start_1,column_end_1,column_start_2,column_end_2,graphStart):
    y_axis_name = gammaType+' Gamma (10**-36 esu)'
    x_axis_name = 'Wave Length (nm)'
    headings = [x_axis_name, y_axis_name]
    Graph = pandas.read_csv(Graph_Name)
    WaveLength = Graph.Wave_Length.tolist()
    Average = Graph.Average.tolist()
    #
    data = [
        WaveLength,
        Average,
    ]
    #
    worksheet.write_row(heading_start, headings, bold)
    worksheet.write_column(column_start_1, data[0])
    worksheet.write_column(column_start_2, data[1])
    #
    chart1 = workbook.add_chart({'type': 'line'})
    #
    series_1  = '=Sheet1!'+column_start_1+':'+column_end_1
    series_2  = '=Sheet1!'+column_start_2+':'+column_end_2
    #
    chart1.add_series({
        'categories': series_1,
        'values':     series_2,
    })
    #
    newName = gammaType+' Gamma Vs Wave Length'
    chart1.set_title ({'name': newName})
    #
    chart1.set_x_axis({'name': 'Wave Length (nm)'})
    #
    chart1.set_y_axis({'name': y_axis_name})
    #
    chart1.set_style(11)
    #
    #worksheet.insert_chart(graphStart, chart1, {'x_offset': 40, 'y_offset': 30})
    #
    worksheet.insert_chart(graphStart, chart1, {'x_scale': 1.5, 'y_scale': 1.5})
#
#
#
def graphCreator(moleculeName,GF1,GF2,GF3,GF4,GFN1,GFN2,GFN3,GFN4):
    #
    newExcelName = moleculeName+'_Graphs.xlsx'
    workbook = xlsxwriter.Workbook(newExcelName)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1})
    #
    innerGraphCreator(workbook,worksheet,bold,GF1,GFN1,'A1','A2','A21','B2','B21','D1')
    innerGraphCreator(workbook,worksheet,bold,GF2,GFN2,'A25','A26','A45','B26','B45','D25')
    innerGraphCreator(workbook,worksheet,bold,GF3,GFN3,'A49','A50','A69','B50','B69','D49')
    innerGraphCreator(workbook,worksheet,bold,GF4,GFN4,'A73','A74','A93','B74','B93','D73')
    workbook.close()
#
#
#
def finalFileCreator():
    print('')
    moleculeName = input('Enter name for the molecule ==> ')
    FileNameDCKP = moleculeName + '_DC_Kerr_Parallel.csv'
    FileNameDCKPP = moleculeName + '_DC_Kerr_Perpendicular.csv'
    FileNameEFISHGP = moleculeName + '_EFISHG_Parallel.csv'
    FileNameEFISHGPP = moleculeName + '_EFISHG_Perpendicular.csv'
    print('')
    #
    GFN1 = 'DC Kerr Parallel'
    GFN2 = 'DC Kerr Perpendicular'
    GFN3 = 'EFISHG Parallel'
    GFN4 = 'EFISHG Perpendicular'
    #
    type1 = 'DC Kerr Parallel Values'
    type2 = 'DC Kerr Perpendicular Values'
    type3 = 'EFISHG Parallel Values'
    type4 = 'EFISHG Perpendicular Values'
    #
    t1 = input('Trial 01 file name = ')
    t2 = input('Trial 02 file name = ')
    t3 = input('Trial 03 file name = ')
    print('')
    #
    T1 = 'temp_'+t1
    T2 = 'temp_'+t2
    T3 = 'temp_'+t3
    #
    updateFile(t1,T1)
    updateFile(t2,T2)
    updateFile(t3,T3)
    #
    Trial_Number_1 = pandas.read_csv(T1)
    Trial_Number_2 = pandas.read_csv(T2)
    Trial_Number_3 = pandas.read_csv(T3)
    #
    WaveLengths = Trial_Number_1.Wave_Length.tolist()
    #
    DCKP1 = Trial_Number_1.DC_kerr_Parallel.tolist()
    DCKPP1 = Trial_Number_1.DC_kerr_Perpendicular.tolist()
    EFISHGP1 = Trial_Number_1.EFISHG_Parallel.tolist()
    EFISHGPP1 = Trial_Number_1.EFISHG_Perpendicular.tolist()
    #
    DCKP2 = Trial_Number_2.DC_kerr_Parallel.tolist()
    DCKPP2 = Trial_Number_2.DC_kerr_Perpendicular.tolist()
    EFISHGP2 = Trial_Number_2.EFISHG_Parallel.tolist()
    EFISHGPP2 = Trial_Number_2.EFISHG_Perpendicular.tolist()
    #
    DCKP3 = Trial_Number_3.DC_kerr_Parallel.tolist()
    DCKPP3 = Trial_Number_3.DC_kerr_Perpendicular.tolist()
    EFISHGP3 = Trial_Number_3.EFISHG_Parallel.tolist()
    EFISHGPP3 = Trial_Number_3.EFISHG_Perpendicular.tolist()
    #
    waveLengthName = 'Wave_Length'
    averageName = 'Average'
    writeType = 'a'
    #
    fileCreator(FileNameDCKP,type1,DCKP1,DCKP2,DCKP3,WaveLengths,averageName,writeType,waveLengthName)
    fileCreator(FileNameDCKPP,type2,DCKPP1,DCKPP2,DCKPP3,WaveLengths,averageName,writeType,waveLengthName)
    fileCreator(FileNameEFISHGP,type3,EFISHGP1,EFISHGP2,EFISHGP3,WaveLengths,averageName,writeType,waveLengthName)
    fileCreator(FileNameEFISHGPP,type4,EFISHGPP1,EFISHGPP2,EFISHGPP3,WaveLengths,averageName,writeType,waveLengthName)
    graphCreator(moleculeName,FileNameDCKP,FileNameDCKPP,FileNameEFISHGP,FileNameEFISHGPP,GFN1,GFN2,GFN3,GFN4)
    #
    waveLengthName = 'Wave Length (nm)'
    averageName = 'Average (10**-36 esu)'
    writeType = 'w'
    #
    fileCreator(FileNameDCKP,type1,DCKP1,DCKP2,DCKP3,WaveLengths,averageName,writeType,waveLengthName)
    fileCreator(FileNameDCKPP,type2,DCKPP1,DCKPP2,DCKPP3,WaveLengths,averageName,writeType,waveLengthName)
    fileCreator(FileNameEFISHGP,type3,EFISHGP1,EFISHGP2,EFISHGP3,WaveLengths,averageName,writeType,waveLengthName)
    fileCreator(FileNameEFISHGPP,type4,EFISHGPP1,EFISHGPP2,EFISHGPP3,WaveLengths,averageName,writeType,waveLengthName)
    #
    excelFileName = moleculeName+'Graphs.xlsx'
    #
    print('Data files created : ')
    print('                     ',FileNameDCKP)
    print('                     ',FileNameDCKPP)
    print('                     ',FileNameEFISHGP)
    print('                     ',FileNameEFISHGPP)
    print('                     ',excelFileName)
    #
    os.remove(T1)
    os.remove(T2)
    os.remove(T3)
    #
    print('')
#
#
#
def sInnerGraphCreator(workbook,worksheet,bold,Graph_Name,gammaType1,gammaType2,gammaType3,gammaType4,heading_start,column_start_1,column_end_1,column_start_2,column_end_2,graphStart1,column_start_3,column_end_3,graphStart2,column_start_4,column_end_4,graphStart3,column_start_5,column_end_5,graphStart4):
    y_axis_name = gammaType1+' Gamma (10**-36 esu)'
    x_axis_name = 'Wave Length (nm)'
    headings = [x_axis_name, y_axis_name]
    Graph = pandas.read_csv(Graph_Name)
    WaveLength = Graph.Wave_Length.tolist()
    Gtype = Graph.DC_kerr_Parallel.tolist()
    #
    data = [
        WaveLength,
        Gtype,
    ]
    #
    worksheet.write_row(heading_start, headings, bold)
    worksheet.write_column(column_start_1, data[0])
    worksheet.write_column(column_start_2, data[1])
    #
    chart1 = workbook.add_chart({'type': 'line'})
    #
    series_1  = '=Sheet1!'+column_start_1+':'+column_end_1
    series_2  = '=Sheet1!'+column_start_2+':'+column_end_2
    #
    chart1.add_series({
        'categories': series_1,
        'values':     series_2,
    })
    #
    newName = gammaType1+' Gamma Vs Wave Length'
    chart1.set_title ({'name': newName})
    #
    chart1.set_x_axis({'name': 'Wave Length (nm)'})
    #
    chart1.set_y_axis({'name': y_axis_name})
    #
    chart1.set_style(11)
    #
    #worksheet.insert_chart(graphStart1, chart1, {'x_offset': 40, 'y_offset': 30})
    #
    worksheet.insert_chart(graphStart1, chart1, {'x_scale': 1.5, 'y_scale': 1.5})
    #
    #
    #
    y_axis_name = gammaType2+' Gamma (10**-36 esu)'
    Gtype = Graph.DC_kerr_Perpendicular.tolist()
    headings = [y_axis_name]
    #
    data = [
        WaveLength,
        Gtype,
    ]
    #
    worksheet.write_row('D1', headings, bold)
    worksheet.write_column(column_start_1, data[0])
    worksheet.write_column(column_start_3, data[1])
    #
    chart1 = workbook.add_chart({'type': 'line'})
    #
    series_1  = '=Sheet1!'+column_start_1+':'+column_end_1
    series_2  = '=Sheet1!'+column_start_3+':'+column_end_3
    #
    chart1.add_series({
        'categories': series_1,
        'values':     series_2,
    })
    #
    newName = gammaType2+' Gamma Vs Wave Length'
    chart1.set_title ({'name': newName})
    #
    chart1.set_x_axis({'name': 'Wave Length (nm)'})
    #
    chart1.set_y_axis({'name': y_axis_name})
    #
    chart1.set_style(11)
    #
    #worksheet.insert_chart(graphStart2, chart1, {'x_offset': 40, 'y_offset': 30})
    #
    worksheet.insert_chart(graphStart2, chart1, {'x_scale': 1.5, 'y_scale': 1.5})
    #
    #
    #
    y_axis_name = gammaType3+' Gamma (10**-36 esu)'
    Gtype = Graph.EFISHG_Parallel.tolist()
    headings = [y_axis_name]
    #
    data = [
        WaveLength,
        Gtype,
    ]
    #
    worksheet.write_row('E1', headings, bold)
    worksheet.write_column(column_start_1, data[0])
    worksheet.write_column(column_start_4, data[1])
    #
    chart1 = workbook.add_chart({'type': 'line'})
    #
    series_1  = '=Sheet1!'+column_start_1+':'+column_end_1
    series_2  = '=Sheet1!'+column_start_4+':'+column_end_4
    #
    chart1.add_series({
        'categories': series_1,
        'values':     series_2,
    })
    #
    newName = gammaType3+' Gamma Vs Wave Length'
    chart1.set_title ({'name': newName})
    #
    chart1.set_x_axis({'name': 'Wave Length (nm)'})
    #
    chart1.set_y_axis({'name': y_axis_name})
    #
    chart1.set_style(11)
    #
    #worksheet.insert_chart(graphStart3, chart1, {'x_offset': 40, 'y_offset': 30})
    #
    worksheet.insert_chart(graphStart3, chart1, {'x_scale': 1.5, 'y_scale': 1.5})
    #
    #
    #
    y_axis_name = gammaType4+' Gamma (10**-36 esu)'
    Gtype = Graph.EFISHG_Perpendicular.tolist()
    headings = [y_axis_name]
    #
    data = [
        WaveLength,
        Gtype,
    ]
    #
    worksheet.write_row('F1', headings, bold)
    worksheet.write_column(column_start_1, data[0])
    worksheet.write_column(column_start_5, data[1])
    #
    chart1 = workbook.add_chart({'type': 'line'})
    #
    series_1  = '=Sheet1!'+column_start_1+':'+column_end_1
    series_2  = '=Sheet1!'+column_start_5+':'+column_end_5
    #
    chart1.add_series({
        'categories': series_1,
        'values':     series_2,
    })
    #
    newName = gammaType4+' Gamma Vs Wave Length'
    chart1.set_title ({'name': newName})
    #
    chart1.set_x_axis({'name': 'Wave Length (nm)'})
    #
    chart1.set_y_axis({'name': y_axis_name})
    #
    chart1.set_style(11)
    #
    #worksheet.insert_chart(graphStart4, chart1, {'x_offset': 40, 'y_offset': 30})
    #
    worksheet.insert_chart(graphStart4, chart1, {'x_scale': 1.5, 'y_scale': 1.5})
#
#
#
def sGraphCreator(moleculeName,GF1,tNo):
    #
    newExcelName = 'Graphs_of_'+moleculeName+'_'+tNo+'.xlsx'
    workbook = xlsxwriter.Workbook(newExcelName)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1})
    #
    GFN1 = 'DC kerr Parallel'
    GFN2 = 'DC kerr Perpendicular'
    GFN3 = 'EFISHG Parallel'
    GFN4 = 'EFISHG Perpendicular'
    #
    sInnerGraphCreator(workbook,worksheet,bold,GF1,GFN1,GFN2,GFN3,GFN4,'B1','B2','B21','C2','C21','K1','D2','D21','K25','E2','E21','K49','F2','F21','K73')
    workbook.close()
#
#
#
def sFinalFileCreator():
    print('')
    t1 = input('Enter the file name ==> ')
    mName = input('Molecule name       ==> ')
    tNo = input('Trial Number        ==> ')
    print('')
    #
    GFN1 = 'DC Kerr Parallel'
    GFN2 = 'DC Kerr Perpendicular'
    GFN3 = 'EFISHG Parallel'
    GFN4 = 'EFISHG Perpendicular'
    #
    type1 = 'DC Kerr Parallel Values'
    type2 = 'DC Kerr Perpendicular Values'
    type3 = 'EFISHG Parallel Values'
    type4 = 'EFISHG Perpendicular Values'
    #
    #
    T1 = 'Graphs_of_'+mName+'.csv'
    #
    updateFile(t1,T1)
    #
    sGraphCreator(mName,T1,tNo)
    #
    newT1 = 'Graphs_of_'+mName+'.xlsx'
    #
    print('Data files created : ')
    print('                     '+newT1)
    #
    os.remove(T1)
    #
    print('')
#
#
#
def automatedCalculation(proName):
    #
    print('')
    print('                               ****************************')
    print('                               ***Automated Calculations***')
    print('                               ****************************')
    print('')
    #
    print('')
    moName = input('Enter name for the molecule ==> ')
    print('')
    #
    new_path = os.path.abspath(proName)
    proName = '\\'+proName
    new_path = new_path.split(proName)[0]
    #
    #
    #
    def automatedParallelPerpendicularGammaReader(moName,tNo,save_path):
        #
        #
        #
        path = save_path+'\\'+moName+'_Gamma_Calculation\\'+tNo
        save_path = save_path+'\\'+moName+'_Gamma_Calculation\\'+'\\Results_And_Graphs'
        #
        #
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
        filenames = []
        GFNames = []
        for dirpath, dirnames, filenames in walk(path):
            continue
        def gaussianComFiles(files,comFileNames):
            for i in range(len(files)):
                if files[i].split('.')[1]=='out':
                    comFileNames.append(files[i])
        gaussianComFiles(filenames,GFNames)
        #
        #Main Menu of the PPGamma reader
        #
        def automatedPPGammaMainManu(inputFiles,trialNumbers,path):
            #
            Tnumber.append(trialNumbers)
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
                    stringValue = EFISHGparallelV[len(EFISHGparallelV)-1][i]
                    stringValue = stringValue.replace('D','E')
                    EFISHGparallel.append(stringValue)
                    stringValue = EFISHGperpendicularV[len(EFISHGperpendicularV)-1][i]
                    stringValue = stringValue.replace('D','E')
                    EFISHGperpendicular.append(stringValue)
                    stringValue = DC_kerrparallelV[len(DC_kerrparallelV)-1][i]
                    stringValue = stringValue.replace('D','E')
                    DC_kerrparallel.append(stringValue)
                    stringValue = DC_kerrperpendicularV[len(DC_kerrperpendicularV)-1][i]
                    stringValue = stringValue.replace('D','E')
                    DC_kerrperpendicular.append(stringValue)
                    stringValue = EFISHGparallelV[len(EFISHGparallelV)-1][i]
                    stringValue = stringValue.replace('D','E')
                    EFISHGparallelT.append(stringValue)
                    stringValue = EFISHGperpendicularV[len(EFISHGperpendicularV)-1][i]
                    stringValue = stringValue.replace('D','E')
                    EFISHGperpendicularT.append(stringValue)
                    stringValue = DC_kerrparallelV[len(DC_kerrparallelV)-1][i]
                    stringValue = stringValue.replace('D','E')
                    DC_kerrparallelT.append(stringValue)
                    stringValue = DC_kerrperpendicularV[len(DC_kerrperpendicularV)-1][i]
                    stringValue = stringValue.replace('D','E')
                    DC_kerrperpendicularT.append(stringValue)
                    if i == 2:
                        stringValue = EFISHGparallelV[len(EFISHGparallelV)-1][i]
                        stringValue = stringValue.replace('D','E')
                        EFISHGparallelSU.append(stringValue)
                        stringValue = EFISHGperpendicularV[len(EFISHGperpendicularV)-1][i]
                        stringValue = stringValue.replace('D','E')
                        EFISHGperpendicularSU.append(stringValue)
                        stringValue = DC_kerrparallelV[len(DC_kerrparallelV)-1][i]
                        stringValue = stringValue.replace('D','E')
                        DC_kerrparallelSU.append(stringValue)
                        stringValue = DC_kerrperpendicularV[len(DC_kerrperpendicularV)-1][i]
                        stringValue = stringValue.replace('D','E')
                        DC_kerrperpendicularSU.append(stringValue)
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
            #
        for k in range (0,len(GFNames)):
            filename = path+'\\'+GFNames[k]
            automatedPPGammaMainManu(filename,1,path)
            #
            #
            #
        dataFileName = save_path+'\\'+moName+'_'+tNo+'.csv'
        with open(dataFileName,'w',newline='') as dFile:
            thewriter = csv.writer(dFile)
            thewriter.writerow(['Trial Number','Wave Length (nm)','DC kerr Parallel (10**-36 esu)','DC kerr Perpendicular (10**-36 esu)','EFISHG Parallel (10**-36 esu)','EFISHG Perpendicular (10**-36 esu)'])
            nlen = len(Tnumber)
            for n in range(nlen):
                waveLength[n] = (waveLength[n].split('nm'))[0]
                thewriter.writerow([Tnumber[n],waveLength[n],DC_kerrparallelSU[n],DC_kerrperpendicularSU[n],EFISHGparallelSU[n],EFISHGperpendicularSU[n]])
        #
        #
        #
    automatedParallelPerpendicularGammaReader(moName,'T1',new_path)
    automatedParallelPerpendicularGammaReader(moName,'T2',new_path)
    automatedParallelPerpendicularGammaReader(moName,'T3',new_path)
    #
    #
    #
    def automatedfinalFileCreator(save_path,moName):
        #
        save_path = save_path+'\\'+moName+'_Gamma_Calculation\\'+'\\Results_And_Graphs'
        #
        FileNameDCKP = save_path+'\\'+moName + '_DC_Kerr_Parallel.csv'
        FileNameDCKPP = save_path+'\\'+moName + '_DC_Kerr_Perpendicular.csv'
        FileNameEFISHGP = save_path+'\\'+moName + '_EFISHG_Parallel.csv'
        FileNameEFISHGPP = save_path+'\\'+moName + '_EFISHG_Perpendicular.csv'
        #
        GFN1 = 'DC Kerr Parallel'
        GFN2 = 'DC Kerr Perpendicular'
        GFN3 = 'EFISHG Parallel'
        GFN4 = 'EFISHG Perpendicular'
        #
        type1 = 'DC Kerr Parallel Values'
        type2 = 'DC Kerr Perpendicular Values'
        type3 = 'EFISHG Parallel Values'
        type4 = 'EFISHG Perpendicular Values'
        #
        t1 = save_path+'\\'+moName+'_T1.csv'
        t2 = save_path+'\\'+moName+'_T2.csv'
        t3 = save_path+'\\'+moName+'_T3.csv'
        #
        T1 = save_path+'\\'+'temp_T1.csv'
        T2 = save_path+'\\'+'temp_T2.csv'
        T3 = save_path+'\\'+'temp_T3.csv'
        #
        updateFile(t1,T1)
        updateFile(t2,T2)
        updateFile(t3,T3)
        #
        Trial_Number_1 = pandas.read_csv(T1)
        Trial_Number_2 = pandas.read_csv(T2)
        Trial_Number_3 = pandas.read_csv(T3)
        #
        WaveLengths = Trial_Number_1.Wave_Length.tolist()
        #
        DCKP1 = Trial_Number_1.DC_kerr_Parallel.tolist()
        DCKPP1 = Trial_Number_1.DC_kerr_Perpendicular.tolist()
        EFISHGP1 = Trial_Number_1.EFISHG_Parallel.tolist()
        EFISHGPP1 = Trial_Number_1.EFISHG_Perpendicular.tolist()
        #
        DCKP2 = Trial_Number_2.DC_kerr_Parallel.tolist()
        DCKPP2 = Trial_Number_2.DC_kerr_Perpendicular.tolist()
        EFISHGP2 = Trial_Number_2.EFISHG_Parallel.tolist()
        EFISHGPP2 = Trial_Number_2.EFISHG_Perpendicular.tolist()
        #
        DCKP3 = Trial_Number_3.DC_kerr_Parallel.tolist()
        DCKPP3 = Trial_Number_3.DC_kerr_Perpendicular.tolist()
        EFISHGP3 = Trial_Number_3.EFISHG_Parallel.tolist()
        EFISHGPP3 = Trial_Number_3.EFISHG_Perpendicular.tolist()
        #
        waveLengthName = 'Wave_Length'
        averageName = 'Average'
        writeType = 'a'
        #
        newMoName = save_path+'\\'+moName
        #
        fileCreator(FileNameDCKP,type1,DCKP1,DCKP2,DCKP3,WaveLengths,averageName,writeType,waveLengthName)
        fileCreator(FileNameDCKPP,type2,DCKPP1,DCKPP2,DCKPP3,WaveLengths,averageName,writeType,waveLengthName)
        fileCreator(FileNameEFISHGP,type3,EFISHGP1,EFISHGP2,EFISHGP3,WaveLengths,averageName,writeType,waveLengthName)
        fileCreator(FileNameEFISHGPP,type4,EFISHGPP1,EFISHGPP2,EFISHGPP3,WaveLengths,averageName,writeType,waveLengthName)
        graphCreator(newMoName,FileNameDCKP,FileNameDCKPP,FileNameEFISHGP,FileNameEFISHGPP,GFN1,GFN2,GFN3,GFN4)
        #
        waveLengthName = 'Wave Length (nm)'
        averageName = 'Average (10**-36 esu)'
        writeType = 'w'
        #
        fileCreator(FileNameDCKP,type1,DCKP1,DCKP2,DCKP3,WaveLengths,averageName,writeType,waveLengthName)
        fileCreator(FileNameDCKPP,type2,DCKPP1,DCKPP2,DCKPP3,WaveLengths,averageName,writeType,waveLengthName)
        fileCreator(FileNameEFISHGP,type3,EFISHGP1,EFISHGP2,EFISHGP3,WaveLengths,averageName,writeType,waveLengthName)
        fileCreator(FileNameEFISHGPP,type4,EFISHGPP1,EFISHGPP2,EFISHGPP3,WaveLengths,averageName,writeType,waveLengthName)
        #
        excelFileName = save_path+'\\'+moName+'_Graphs.xlsx'
        #
        os.remove(T1)
        os.remove(T2)
        os.remove(T3)
        #
    automatedfinalFileCreator(new_path,moName)
    #
    fileName1 =  moName+'_T1.csv'
    fileName2 =  moName+'_T2.csv'
    fileName3 =  moName+'_T3.csv'
    fileName4 =  moName+'_DC_Kerr_Parallel.csv'
    fileName5 =  moName+'_DC_Kerr_Perpendicular.csv'
    fileName6 =  moName+'_EFISHG_Parallel.csv'
    fileName7 =  moName+'_EFISHG_Perpendicular.csv'
    fileName8 =  moName+'_Graphs.xlsx'
    #
    print('Data files created : ')
    print('                     ',fileName1)
    print('                     ',fileName2)
    print('                     ',fileName3)
    print('                     ',fileName4)
    print('                     ',fileName5)
    print('                     ',fileName6)
    print('                     ',fileName7)
    print('                     ',fileName8)
    print('')
#
#
#
def HighestNPP():
    print('')
    inFileName = input('Enter file name: ')
    InFileName = inFileName[0:(len(inFileName)-4)]
    FileName = InFileName.split('_')
    fileTN = ''
    for i in range(0,len(FileName)):
        fileTN = fileTN+FileName[i]+' '
    AVL = []
    WL = []
    newAVL = []
    newWL =[]
    with open(inFileName,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        next(csv_reader)
        for line in csv_reader:
            AVL.append(line[4])
            WL.append(line[0])
    #
    #
    #
    for i in range(0,len(AVL)):
        newAVL.append(float(AVL[i]))
        newWL.append(float(WL[i]))
    #
    #
    #
    minV = min(newAVL)
    maxV = max(newAVL)
    minVP = 0
    maxVP = 0
    for j in range(0,len(newAVL)):
        if minV == newAVL[j]:
            minVP = j
        elif maxV == newAVL[j]:
            maxVP = j
    positiveP = []
    negativeP = []
    for p in range(0,len(newAVL)):
        if  newAVL[p] >= 0:
            positiveP.append(newAVL[p])
        else:
            negativeP.append(newAVL[p])
    maxV = max(positiveP)
    minV = min(negativeP)
    print('')
    print('For '+fileTN)
    print('')
    print('Highest positive peak,')
    print('                      Gamma value = ',maxV,'10**-36 esu')
    print('                      Wavelength  = ',newWL[maxVP],'nm')
    print('')
    print('+ Further calculations are suggested to find the highest positive peak.')
    print('+ Suggested wavelengths are,')
    print('                           ',newWL[maxVP]-20.0,'nm')
    print('                           ',newWL[maxVP]-10.0,'nm')
    print('                           ',newWL[maxVP]+10.0,'nm')
    print('                           ',newWL[maxVP]+20.0,'nm')
    print('')
    print('Highest negative peak,')
    print('                      Gamma value = ',minV,'10**-36 esu')
    print('                      Wavelength  = ',newWL[minVP],'nm')
    print('')
    print('+ Further calculations are suggested to find the highest positive peak.')
    print('+ Suggested wavelengths are,')
    print('                           ',newWL[minVP]-20.0,'nm')
    print('                           ',newWL[minVP]-10.0,'nm')
    print('                           ',newWL[minVP]+10.0,'nm')
    print('                           ',newWL[minVP]+20.0,'nm')
    print('')
#
#
#
def errorHandler(func):
    try:
        func()
    except ValueError:
        print('')
        print('ValueError occurred!')
        print('You have enterd a character string/symbols or none.')
        print('Please only enter numbers.')
        print('')
        errorHandler(func)
    except ZeroDivisionError:
        print('')
        print('ZeroDivisionError occurred!')
        print('You have divided the number by zero!')
        print('Please only enter numbers.')
        print('')
        errorHandler(func)
    except FileNotFoundError:
        print('')
        print('FileNotFoundError occurred!')
        print('This file do not exist in the file path!')
        print('Please check again.')
        print('')
        errorHandler(func)
    except PermissionError:
        print('')
        print('PermissionError occurred!')
        print('Cannot start a xyz.csv file name with symbols!')
        print('Enter a valid name.')
        print('')
        errorHandler(func)
    except AttributeError:
        print('')
        print('AttributeError occurred!')
        print('Your Files have already been created!')
        print('Please check again.')
        print('')
        errorHandler(func)
    except:
        print('')
        print('An unknown error occurred!')
        print('')
        errorHandler(func)
#
#GacOProgramme_2.1V
#
def GacOProgramme():
    start()
    errorHandler(GacOMenu)
#
#
#
GacOProgramme()
