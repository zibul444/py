class Split:
    outputFile = open('out.csv', 'br')
    pattern = 'input'
    inputFile = ''
    constantLine = ''
    countLine = 0
    countFile = 1

    # outputFile.decode('utf-8').encode('cp1251')
    # print(outputFile.decode('utf-8'))

    for line in outputFile:

        if countLine == 0:
            inputFile = open(pattern + str(countFile), 'bw')
            constantLine = line
            inputFile.write(line)
        elif countLine % 3 == 0:
            inputFile.close()
            countFile = countFile + 1
            inputFile = open(pattern + str(countFile), 'bw')

            inputFile.write(constantLine)
            inputFile.write(line)
        else:
            inputFile.write(line)
        countLine = countLine + 1
    inputFile.close()
    outputFile.close()
