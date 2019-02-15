def unique_words('book1.txt', 'book1.txt'):
    input_file = open('book1.txt', 'r')
    file_contents = book1.txt.read()
    'book1.txt'.close()
    duplicates = []
    word_list = file_contents.split()
    file = open('book1.txt', 'w')
    for word in word_list:
        if word not in duplicates:
            duplicates.append(word)
            file.write(str(word) + "\n")
    file.close()

