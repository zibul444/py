import re

class SplitterBinar:

    outputFile = open('out.csv', 'br')
    inputFileName = 'inputFile'
    inputFile = open(inputFileName, 'bw')

    # print('__-__' + outputFile)
    countLine = 0
    countFile = 0

    # bitMup = -1
    # bitMupValue = ''

    firstLine = ''
    print(bytearray(outputFile.read()))
    # for buf in outputFile:
    #
    #     print(bytearray(buf))
    #     inputFile.write(buf)
    #     if re.search('cr', str(buf)):
    #         print(str(buf))
    #         print(str(buf))
    #         inputFile.write(buf)
            # if countLine == 0 and buf == 'константа начала файла в utf-8':
            # if countLine == 0:
            # bitMup = 1
            # bitMupValue = buf


            # ищем вхождения переноса строк