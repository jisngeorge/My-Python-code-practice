with open("test.txt") as text_file:
    contents = text_file.read()
    print(contents.rstrip())
