from os import listdir
from os.path import isfile, join

onlyFiles = [f for f in listdir('./news_dataset') if isfile(join('./news_dataset', f))]

totalFiles = 2000
print(totalFiles)