import re
import os
import json
from utils.lists import flat_map
from ScanDir import totalFiles, onlyFiles
import math

docTermMatrix = {}
cachedWords = []


# Load index.txt first and save into docTermMatrix variable
# If the file does not exist, build the docTermMatrix
# convert the docTermMatrix into json and save it in index.txt
if os.path.exists('./index.txt'):
    fromJson = open("./index.txt", "r", encoding="utf-16").read()
    docTermMatrix = json.loads(fromJson)
else:
    stopwords = open("./stopwords.txt", "r", encoding="utf-16").read().split('\n')

    for i in range(totalFiles):
        f = open("./news_dataset/" + onlyFiles[i], "r", encoding="utf-16")

        lines = (f.read().split('\n'))
        lines = list(map(lambda x: x.lower(), lines))
        lines = list(map(lambda x: re.sub('[^A-Za-záàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ0-9 ]+', ' ', x), lines))

        words = list(flat_map(lines, lambda x: x.split()))
        words = list(filter(lambda x: x != '', words))
        words = list(filter(lambda x: x not in stopwords, words))
        cachedWords.append(words)

        wordsDictionary = dict.fromkeys(words)
        words = list(wordsDictionary)

        for word in words:
            if (word not in docTermMatrix):
                docTermMatrix[word] = {}

        print("Scan file:", str(i), "/", str(totalFiles))

    print(len(docTermMatrix))
    input("Confirm")
    for key in docTermMatrix:
        for i in range(len(cachedWords)):
            count = cachedWords[i].count(key)
            if (count != 0):
                docTermMatrix[key][onlyFiles[i]] = count / len(cachedWords[i])
            print(key, ":", str(i), "/", len(cachedWords))

    i = 0
    for key in docTermMatrix:
        idf = float((1.0 * totalFiles) / (1.0 * len(docTermMatrix[key])))
        idf = 1 + math.log2(idf)

        for doc in docTermMatrix[key]:
            docTermMatrix[key][doc] = round(docTermMatrix[key][doc] * idf, 5)

        print("calculating:", i, "/", str(len(docTermMatrix)))
        i += 1

    toJson = json.dumps(docTermMatrix, ensure_ascii=False)
    f = open("index.txt", "w", encoding="utf-16")
    f.write(toJson)
    f.close()

    print("BUILD INDEX DONE")
