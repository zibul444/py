class lalalas:
    outFile = open('out.csv', 'w')
    i = 1
    l = '1'
    while(i <= 9):
        outFile.write(l + '\n')
        l = l + '1'
        i = i + 1

    outFile.close()
