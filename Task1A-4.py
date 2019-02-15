# Function name: character_word_count - Returns: A Dicionary containing words in the book as key and the character count as the values.
def character_word_count ('book1.txt'):
    """ Makes a list of the words in the file filename and the number of times
    each word appears. This program is modified from one by Mark Summerfield in
    his excellent book, "Programming in Python 3" """

    text_file = open('book1.txt')     # open the file for reading
    
    # Set up an empty dictionary to start a standard design pattern loop
    words_dic = {}
    
    # This loop adds each word to the dictionary and updates its count. Change 
    # all words to lower case so Horse and horse are seen as the same word.
    for line in text_file:         # step through each line in the text file
        for word in line.lower().split():   # split into a list of words
            word = word.strip("'?,.;!-/\"") # strip out the stuff we ignore
            if word not in words_dic:
                words_dic[word] = 0      # add word to words with 0 count
            words_dic[word] = words_dic[word] + 1    # add 1 to the count
    
    text_file.close() 
