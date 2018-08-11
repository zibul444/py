# метод поиска файлов в дерриктории по маске
import os
import re

directory = '/home/abcherkashin/Загрузки'
targetStart = re.compile(r'(^py{1,1})(\w+)')
targetAnd = re.compile(r'(.gz$)')

filesDirectory = os.listdir(directory)
sortedList = []
print(filesDirectory)

for currentFile in filesDirectory:
    if re.search(targetStart, currentFile) and re.search(targetAnd, currentFile):
        sortedList.append(currentFile)

print(sortedList)
