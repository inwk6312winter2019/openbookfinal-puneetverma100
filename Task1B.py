

def printTopWords(file):
    '''
    Finds top 20 most frequently occurring terms in a file. 
    Input file expected to come from reducer.py output. Returns output in plain text file, 'book1.txt' 
    '''

    fullArray = []
    numArray = []
    file = open("book1.txt")
    for line in file.readlines():
        line = line.strip()
        fullArray = fullArray + [line]    #create list with all lines as elements
    for element in sorted(fullArray):
        numArray = numArray + [int(element[element.find(",")+1:])]    #extract numbers from elements
    numArray.sort(reverse=True)      #sort numbers into descending order
    for element in fullArray:
        for num in numArray[0:19]:    #find items in fullarray whose final digits match those of the first 20 of the numarray     
            if int(element[element.find(",")+1:]) == num:    
                if element in fullArray:
                    fullArray.remove(element)    #remove element in order to prevent multiple instances of the same element being printed
                    print(element) 
