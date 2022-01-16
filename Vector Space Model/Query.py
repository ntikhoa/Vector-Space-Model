def processQuery(query):
    statements = query.split()
    statements = list(map(lambda x: x.strip(), statements))
    statements = list(map(lambda x: x.lower(), statements))
    print(statements)
    return statements
