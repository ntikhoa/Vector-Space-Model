from Query import processQuery
from BuildTermDocument import docTermMatrix
from ScanDir import totalFiles, onlyFiles
import numpy as np
import math

# for multithreading maybe in the future
# print(len(onlyFiles))
# index = int(len(docTermMatrix) / 4)
# print(len(docTermMatrix))
# print(0, index)
# print(index, index * 2)
# print(index * 2, index * 3)
# print(index * 3, len(docTermMatrix))

# suggestion query: pc ps4 ps5
# query = input("Enter query: ")


def ranking_return(query):
    query = processQuery(query)

    queryVector = []
    for k in docTermMatrix:
        if (k in query):
            queryVector.append(1)
        else:
            queryVector.append(0)

    queryVector = np.asarray(queryVector)
    unitQueryVector = queryVector / np.linalg.norm(queryVector)

    ranking = []

    for i in range(totalFiles):
        file = onlyFiles[i]
        docVector = []
        for k in docTermMatrix:
            if file in docTermMatrix[k]:
                docVector.append(docTermMatrix[k][file])
            else:
                docVector.append(0)

        docVector = np.asarray(docVector)
        unitDocVector = docVector / np.linalg.norm(docVector)
        dot_product = np.dot(unitDocVector, docVector)
        angle = np.arccos(dot_product)
        if (math.isnan(angle)):
            angle = 0
        ranking.append((file, angle))

    for i in range(len(ranking)):
        for j in range(i + 1, len(ranking)):
            if (ranking[j][1] > ranking[i][1]):
                temp = ranking[j]
                ranking[j] = ranking[i]
                ranking[i] = temp

    return ranking
