from Ranking import ranking


# suggestion query: pc ps4 ps5
print("Top documents")
for doc in ranking[0:20]:
    print(doc)
