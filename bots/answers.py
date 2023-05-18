def readfile(file):
    text_file = open(file, "r")
    data = text_file.read()
    text_file.close()
    print(data)
    return data